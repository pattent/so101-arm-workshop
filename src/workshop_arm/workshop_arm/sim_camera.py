"""A simulated overhead camera, drawn live with MuJoCo.

It builds its 3D arm from the same robot description MoveIt and RViz use
(/follower/robot_description), so there is only one model of the arm. Every frame it
copies the arm's joint angles (/follower/joint_states) onto it, puts the blocks and bins
where MoveIt says they are, and renders what a camera hanging above the table would see:
the arm (which can block the view!), lighting, shadows and perspective. It publishes:
    /camera/image_raw     sensor_msgs/Image
    /camera/camera_info   sensor_msgs/CameraInfo

Run:  ros2 run workshop_arm sim_camera
View: ros2 run rqt_image_view rqt_image_view /camera/image_raw

MuJoCo is only used as a camera here: MoveIt and ros2_control still move the arm.
"""

import math
import re
from pathlib import Path

import mujoco
import numpy as np
import rclpy
from ament_index_python.packages import get_package_share_directory
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, QoSProfile
from sensor_msgs.msg import CameraInfo, Image, JointState
from std_msgs.msg import String

from moveit_msgs.msg import PlanningSceneComponents
from moveit_msgs.srv import GetPlanningScene
from workshop_arm.arm import BIN_HEIGHT, BIN_SIZE, BLOCK_SIZE, objects_in_scene
from workshop_arm.table import (
    CAMERA_FOCAL, CAMERA_HEIGHT, CAMERA_HEIGHT_PX, CAMERA_WIDTH, CAMERA_X, CAMERA_Y,
)

FRAMES_PER_SECOND = 15
MAX_BLOCKS = 12
MAX_BINS = 6
RIM_WIDTH = 0.008
TABLE_RGBA = [0.80, 0.72, 0.60, 1]
BIN_FLOOR_RGBA = [0.45, 0.45, 0.45, 1]
HIDDEN = [0.0, 0.0, -1.0]   # unused blocks/bins wait under the table
GRIPPER_FRAME = 'gripper_frame_link'   # held blocks sit here


def urdf_for_mujoco(urdf):
    """Make a ROS robot description loadable by MuJoCo."""
    # package://so101_description/meshes/x.stl -> /full/path/to/so101_description/meshes/x.stl
    urdf = re.sub(r'package://([^/]+)/',
                  lambda m: Path(get_package_share_directory(m.group(1))).as_posix() + '/', urdf)
    # Keep the visual meshes, and keep every link (even fixed ones) as its own body.
    options = '<mujoco><compiler discardvisual="false" fusestatic="false"/></mujoco>'
    return urdf.replace('</robot>', options + '</robot>')


def build_model(urdf):
    """The robot from its URDF + a table, an overhead camera, and spare blocks and bins."""
    spec = mujoco.MjSpec.from_string(urdf_for_mujoco(urdf))
    # The URDF has every part twice: a visual mesh and a collision mesh. Only draw the
    # visual one (group 3 is hidden by default).
    for geom in spec.geoms:
        if geom.contype:
            geom.group = 3
    spec.visual.global_.offwidth = CAMERA_WIDTH
    spec.visual.global_.offheight = CAMERA_HEIGHT_PX
    world = spec.worldbody

    world.add_geom(name='table', type=mujoco.mjtGeom.mjGEOM_PLANE, size=[1, 1, 0.01],
                   rgba=TABLE_RGBA)
    world.add_light(pos=[0.3, 0.3, 1.5], dir=[-0.2, -0.2, -1], diffuse=[0.5, 0.5, 0.5],
                    castshadow=True)

    # Looking straight down. Image "up" is the robot's forward (+x), image "right" is -y.
    fovy = math.degrees(2 * math.atan(CAMERA_HEIGHT_PX / 2 / CAMERA_FOCAL))
    world.add_camera(name='overhead', pos=[CAMERA_X, CAMERA_Y, CAMERA_HEIGHT],
                     quat=[math.sqrt(0.5), 0, 0, -math.sqrt(0.5)], fovy=fovy)

    def no_contact(geom):
        geom.contype = 0
        geom.conaffinity = 0

    for i in range(MAX_BLOCKS):
        body = world.add_body(name=f'block{i}', mocap=True, pos=HIDDEN)
        no_contact(body.add_geom(name=f'block{i}', type=mujoco.mjtGeom.mjGEOM_BOX,
                                 size=[BLOCK_SIZE / 2] * 3))
    for i in range(MAX_BINS):
        body = world.add_body(name=f'bin{i}', mocap=True, pos=HIDDEN)
        no_contact(body.add_geom(name=f'bin{i}', type=mujoco.mjtGeom.mjGEOM_BOX,
                                 size=[BIN_SIZE / 2, BIN_SIZE / 2, BIN_HEIGHT / 2]))
        floor = BIN_SIZE / 2 - RIM_WIDTH
        no_contact(body.add_geom(type=mujoco.mjtGeom.mjGEOM_BOX, pos=[0, 0, 0.0005],
                                 size=[floor, floor, BIN_HEIGHT / 2], rgba=BIN_FLOOR_RGBA))
    return spec.compile()


class SimCamera(Node):

    def __init__(self):
        super().__init__('sim_camera')
        self.model = None      # built once the robot description arrives
        self.rng = np.random.default_rng()

        self.objects = {}      # what MoveIt says is on the table
        self.held = []         # names of blocks in the gripper
        self.colors = {}       # remembered colors (held blocks lose theirs in the scene)
        self.pending = None

        latched = QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self.create_subscription(String, '/follower/robot_description', self.on_robot, latched)
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)
        self.scene_client = self.create_client(GetPlanningScene, '/get_planning_scene')
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 1)
        self.info_pub = self.create_publisher(CameraInfo, '/camera/camera_info', 1)
        self.create_timer(1.0 / FRAMES_PER_SECOND, self.take_picture)
        self.create_timer(0.1, self.ask_for_scene)

    def on_robot(self, msg):
        self.model = build_model(msg.data)
        self.data = mujoco.MjData(self.model)
        self.renderer = mujoco.Renderer(self.model, CAMERA_HEIGHT_PX, CAMERA_WIDTH)
        self.get_logger().info('Got the robot description, camera is live.')

    def on_joints(self, msg):
        if self.model is None:
            return
        for name, position in zip(msg.name, msg.position):
            try:
                self.data.qpos[self.model.joint(name).qposadr[0]] = position
            except KeyError:
                pass

    def ask_for_scene(self):
        if self.pending is None and self.scene_client.service_is_ready():
            request = GetPlanningScene.Request()
            request.components.components = (
                PlanningSceneComponents.WORLD_OBJECT_GEOMETRY
                | PlanningSceneComponents.OBJECT_COLORS
                | PlanningSceneComponents.ROBOT_STATE_ATTACHED_OBJECTS)
            self.pending = self.scene_client.call_async(request)
            self.pending.add_done_callback(self.on_scene)

    def on_scene(self, future):
        self.pending = None
        if future.result() is None:
            return
        scene = future.result().scene
        self.objects = objects_in_scene(scene)
        self.held = [a.object.id for a in scene.robot_state.attached_collision_objects]
        for name, obj in self.objects.items():
            self.colors[name] = obj['color']

    def take_picture(self):
        if self.model is None:
            return
        mujoco.mj_kinematics(self.model, self.data)   # where every arm part is
        self.place_objects()
        mujoco.mj_kinematics(self.model, self.data)
        mujoco.mj_camlight(self.model, self.data)     # where the camera and lights are

        self.renderer.update_scene(self.data, camera='overhead')
        rgb = self.renderer.render()
        noise = self.rng.normal(0, 3, rgb.shape)               # a little webcam grain
        bgr = np.clip(rgb[:, :, ::-1] + noise, 0, 255).astype(np.uint8)

        stamp = self.get_clock().now().to_msg()
        self.image_pub.publish(to_image_msg(bgr, stamp))
        self.info_pub.publish(camera_info(stamp))

    def place_objects(self):
        blocks = [(n, o) for n, o in self.objects.items() if o['kind'] == 'block']
        bins = [(n, o) for n, o in self.objects.items() if o['kind'] == 'bin']

        held_at = self.data.body(GRIPPER_FRAME).xpos
        blocks += [(n, {'x': held_at[0], 'y': held_at[1], 'z': held_at[2],
                        'color': self.colors.get(n, (0.5, 0.5, 0.5))}) for n in self.held]

        for prefix, items, limit in (('block', blocks, MAX_BLOCKS), ('bin', bins, MAX_BINS)):
            for i in range(limit):
                body = self.model.body(f'{prefix}{i}')
                if i < len(items):
                    _, obj = items[i]
                    self.data.mocap_pos[body.mocapid[0]] = [obj['x'], obj['y'], obj['z']]
                    self.model.geom(f'{prefix}{i}').rgba = [*obj['color'], 1.0]
                else:
                    self.data.mocap_pos[body.mocapid[0]] = HIDDEN


def to_image_msg(image, stamp):
    msg = Image()
    msg.header.stamp = stamp
    msg.header.frame_id = 'camera'
    msg.height, msg.width = image.shape[:2]
    msg.encoding = 'bgr8'
    msg.step = msg.width * 3
    msg.data = image.tobytes()
    return msg


def camera_info(stamp):
    info = CameraInfo()
    info.header.stamp = stamp
    info.header.frame_id = 'camera'
    info.width, info.height = CAMERA_WIDTH, CAMERA_HEIGHT_PX
    f, cx, cy = CAMERA_FOCAL, CAMERA_WIDTH / 2, CAMERA_HEIGHT_PX / 2
    info.k = [f, 0.0, cx, 0.0, f, cy, 0.0, 0.0, 1.0]
    info.p = [f, 0.0, cx, 0.0, 0.0, f, cy, 0.0, 0.0, 0.0, 1.0, 0.0]
    info.distortion_model = 'plumb_bob'
    info.d = [0.0] * 5
    return info


def main():
    rclpy.init()
    rclpy.spin(SimCamera())


if __name__ == '__main__':
    main()
