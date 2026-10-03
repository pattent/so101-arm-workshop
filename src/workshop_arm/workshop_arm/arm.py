"""A simple, beginner-friendly way to move the SO-101 arm.

    from workshop_arm import Arm

    arm = Arm()
    arm.go_to('rest')                 # a saved pose: 'rest', 'zero', 'extended'
    arm.move_joints(0, -45, 90, 45, 0)  # five joint angles, in degrees
    arm.move_to(0.25, 0.0, 0.10)      # gripper position in meters (x, y, z)
    arm.open_gripper()
    arm.close_gripper()
    print(arm.where_am_i())

    arm.add_block('red_block', 0.25, -0.10, color='red')   # show objects in RViz
    arm.add_bin('red_bin', 0.15, 0.20, color='red')
    arm.grab('red_block')       # the block now moves with the gripper
    arm.release()               # ...and drops where the gripper is

    arm.shutdown()

Under the hood this sends ROS 2 action goals to MoveIt (for the arm) and to the
gripper controller, and adds objects to MoveIt's "planning scene" (the robot's
picture of the world). It works the same with the simulated arm and the real one.
"""

import math

import rclpy
from rclpy.action import ActionClient
from rclpy.duration import Duration
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import Buffer, TransformListener

from control_msgs.action import ParallelGripperCommand
from geometry_msgs.msg import Pose
from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import (
    AttachedCollisionObject,
    CollisionObject,
    Constraints,
    JointConstraint,
    MoveItErrorCodes,
    ObjectColor,
    PlanningScene,
    PlanningSceneComponents,
    PositionConstraint,
)
from moveit_msgs.srv import ApplyPlanningScene, GetPlanningScene
from shape_msgs.msg import SolidPrimitive
from std_msgs.msg import ColorRGBA

# Names that come from the SO-101 MoveIt config (so101_arm.srdf).
PLANNING_GROUP = 'manipulator'
BASE_FRAME = 'base_link'
GRIPPER_FRAME = 'gripper_frame_link'
JOINT_NAMES = ['shoulder_pan', 'shoulder_lift', 'elbow_flex', 'wrist_flex', 'wrist_roll']
SAVED_POSES = {
    'zero': [0, 0, 0, 0, 0],
    'rest': [0, -90, 90, 43, 0],
    'extended': [0, 90, -90, 0, 0],
}

# Gripper joint range, in radians.
GRIPPER_OPEN = 1.5
GRIPPER_CLOSED = -0.16
# Gripper parts that are allowed to touch a block it is holding.
GRIPPER_LINKS = ['gripper_link', 'gripper_frame_link', 'moving_jaw_so101_v1_link']

# Objects on the table (sizes in meters). The table top is at z = 0.
BLOCK_SIZE = 0.025
BIN_SIZE = 0.10
BIN_HEIGHT = 0.01
COLORS = {
    'red': (0.9, 0.1, 0.1),
    'green': (0.1, 0.8, 0.2),
    'blue': (0.1, 0.3, 0.9),
    'yellow': (0.95, 0.85, 0.1),
    'gray': (0.5, 0.5, 0.5),
}


class Arm:
    """Move the SO-101 arm and gripper with simple Python commands."""

    def __init__(self, namespace='follower', speed=0.5):
        if not rclpy.ok():
            rclpy.init()
        self.node = Node('workshop_arm')
        self.speed = speed  # 0.0 (slowest) to 1.0 (full speed)

        self._move_client = ActionClient(self.node, MoveGroup, '/move_action')
        self._gripper_client = ActionClient(
            self.node, ParallelGripperCommand,
            f'/{namespace}/gripper_controller/gripper_cmd')

        self._scene_client = self.node.create_client(ApplyPlanningScene, '/apply_planning_scene')
        self._get_scene_client = self.node.create_client(GetPlanningScene, '/get_planning_scene')
        self._bins = {}        # name -> (x, y)
        self._colors = {}      # object name -> color name
        self._holding = None   # name of the block in the gripper, if any

        self._tf_buffer = Buffer()
        self._tf_listener = TransformListener(self._tf_buffer, self.node)

        self._log('Waiting for MoveIt and the gripper controller...')
        if not self._move_client.wait_for_server(timeout_sec=30.0):
            raise RuntimeError('MoveIt is not running. Did you start the launch file?')
        if not self._gripper_client.wait_for_server(timeout_sec=30.0):
            raise RuntimeError('The gripper controller is not running.')
        self._log('Arm ready!')

    # ----- Arm motions ---------------------------------------------------

    def go_to(self, pose_name):
        """Move to a saved pose by name, e.g. 'rest'."""
        if pose_name not in SAVED_POSES:
            raise ValueError(f'Unknown pose {pose_name!r}. Try one of: {list(SAVED_POSES)}')
        self._log(f'Going to {pose_name!r}')
        return self.move_joints(*SAVED_POSES[pose_name])

    def move_joints(self, shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll):
        """Move every arm joint to an angle, in degrees."""
        angles = [shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll]
        goal = Constraints()
        for name, degrees in zip(JOINT_NAMES, angles):
            goal.joint_constraints.append(JointConstraint(
                joint_name=name,
                position=math.radians(degrees),
                tolerance_above=0.01,
                tolerance_below=0.01,
                weight=1.0,
            ))
        return self._plan_and_move(goal)

    def move_to(self, x, y, z):
        """Move the gripper to a point (in meters) measured from the robot's base.

        x is forward, y is to the robot's left, z is up.
        """
        self._log(f'Moving gripper to x={x:.3f} y={y:.3f} z={z:.3f}')
        target = Pose()
        target.position.x, target.position.y, target.position.z = float(x), float(y), float(z)
        target.orientation.w = 1.0

        region = PositionConstraint()
        region.header.frame_id = BASE_FRAME
        region.link_name = GRIPPER_FRAME
        region.constraint_region.primitives.append(
            SolidPrimitive(type=SolidPrimitive.SPHERE, dimensions=[0.005]))
        region.constraint_region.primitive_poses.append(target)
        region.weight = 1.0

        return self._plan_and_move(Constraints(position_constraints=[region]))

    # ----- Gripper -------------------------------------------------------

    def open_gripper(self):
        return self.set_gripper(1.0)

    def close_gripper(self):
        return self.set_gripper(0.0)

    def set_gripper(self, amount_open):
        """Set the gripper from 0.0 (closed) to 1.0 (fully open)."""
        amount_open = min(max(amount_open, 0.0), 1.0)
        position = GRIPPER_CLOSED + amount_open * (GRIPPER_OPEN - GRIPPER_CLOSED)
        self._log(f'Gripper {amount_open:.0%} open')

        goal = ParallelGripperCommand.Goal()
        goal.command.name = ['gripper']
        goal.command.position = [position]
        result = self._send_and_wait(self._gripper_client, goal)
        return result is not None

    # ----- Blocks and bins (shown in RViz) --------------------------------

    def add_block(self, name, x, y, color='red'):
        """Put a small cube on the table at (x, y)."""
        self._add_box(name, x, y, BLOCK_SIZE / 2, [BLOCK_SIZE] * 3, color)
        # The gripper has to touch blocks to pick them up, so MoveIt shouldn't
        # treat them as obstacles.
        self._allow_collisions(name)

    def add_bin(self, name, x, y, color='gray'):
        """Put a flat bin (a colored square) on the table at (x, y)."""
        self._bins[name] = (x, y)
        self._add_box(name, x, y, BIN_HEIGHT / 2, [BIN_SIZE, BIN_SIZE, BIN_HEIGHT], color)

    def grab(self, name):
        """Close the gripper and attach the block, so it moves with the arm."""
        self.close_gripper()
        held = AttachedCollisionObject()
        held.link_name = GRIPPER_FRAME
        held.touch_links = GRIPPER_LINKS
        held.object = self._box(name, GRIPPER_FRAME, 0.0, 0.0, 0.0, [BLOCK_SIZE] * 3)

        scene = PlanningScene(is_diff=True)
        scene.robot_state.is_diff = True
        scene.robot_state.attached_collision_objects.append(held)
        scene.world.collision_objects.append(
            CollisionObject(id=name, operation=CollisionObject.REMOVE))
        self._apply_scene(scene)
        self._holding = name

    def release(self):
        """Open the gripper and drop the block below it (onto a bin, if there is one)."""
        self.open_gripper()
        if self._holding is None:
            return
        name, self._holding = self._holding, None

        detach = AttachedCollisionObject(link_name=GRIPPER_FRAME)
        detach.object.id = name
        detach.object.operation = CollisionObject.REMOVE
        scene = PlanningScene(is_diff=True)
        scene.robot_state.is_diff = True
        scene.robot_state.attached_collision_objects.append(detach)
        self._apply_scene(scene)

        x, y, _ = self.where_am_i()
        z = BLOCK_SIZE / 2
        for bin_x, bin_y in self._bins.values():
            if abs(x - bin_x) < BIN_SIZE / 2 and abs(y - bin_y) < BIN_SIZE / 2:
                z += BIN_HEIGHT
        self._add_box(name, x, y, z, [BLOCK_SIZE] * 3, self._colors[name])

    # ----- Where is the arm? ---------------------------------------------

    def where_am_i(self):
        """Return the gripper's (x, y, z) position in meters, from the robot's base."""
        end = self.node.get_clock().now() + Duration(seconds=2.0)
        while self.node.get_clock().now() < end:
            rclpy.spin_once(self.node, timeout_sec=0.1)
            if self._tf_buffer.can_transform(BASE_FRAME, GRIPPER_FRAME, Time()):
                t = self._tf_buffer.lookup_transform(BASE_FRAME, GRIPPER_FRAME, Time())
                p = t.transform.translation
                return round(p.x, 3), round(p.y, 3), round(p.z, 3)
        raise RuntimeError('Could not find the gripper position (is the robot running?)')

    def shutdown(self):
        self.node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

    # ----- Behind the scenes ---------------------------------------------

    def _plan_and_move(self, goal_constraints):
        goal = MoveGroup.Goal()
        request = goal.request
        request.group_name = PLANNING_GROUP
        request.goal_constraints.append(goal_constraints)
        request.num_planning_attempts = 5
        request.allowed_planning_time = 5.0
        request.max_velocity_scaling_factor = self.speed
        request.max_acceleration_scaling_factor = self.speed
        goal.planning_options.plan_only = False

        result = self._send_and_wait(self._move_client, goal)
        if result is None:
            return False
        if result.error_code.val != MoveItErrorCodes.SUCCESS:
            self._log(f'MoveIt could not do that (error code {result.error_code.val}). '
                      'The target may be out of reach.')
            return False
        return True

    def _send_and_wait(self, client, goal):
        send_future = client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self.node, send_future)
        handle = send_future.result()
        if not handle.accepted:
            self._log('The goal was rejected.')
            return None
        result_future = handle.get_result_async()
        rclpy.spin_until_future_complete(self.node, result_future)
        return result_future.result().result

    def _box(self, name, frame, x, y, z, size):
        box = CollisionObject(id=name, operation=CollisionObject.ADD)
        box.header.frame_id = frame
        box.primitives.append(SolidPrimitive(type=SolidPrimitive.BOX, dimensions=list(size)))
        pose = Pose()
        pose.position.x, pose.position.y, pose.position.z = float(x), float(y), float(z)
        pose.orientation.w = 1.0
        box.primitive_poses.append(pose)
        return box

    def _add_box(self, name, x, y, z, size, color):
        if color not in COLORS:
            raise ValueError(f'Unknown color {color!r}. Try one of: {list(COLORS)}')
        self._colors[name] = color
        r, g, b = COLORS[color]
        scene = PlanningScene(is_diff=True)
        scene.world.collision_objects.append(self._box(name, BASE_FRAME, x, y, z, size))
        scene.object_colors.append(ObjectColor(id=name, color=ColorRGBA(r=r, g=g, b=b, a=1.0)))
        self._apply_scene(scene)

    def _allow_collisions(self, name):
        request = GetPlanningScene.Request()
        request.components.components = PlanningSceneComponents.ALLOWED_COLLISION_MATRIX
        acm = self._call(self._get_scene_client, request).scene.allowed_collision_matrix
        if name not in acm.default_entry_names:
            acm.default_entry_names.append(name)
            acm.default_entry_values.append(True)
        self._apply_scene(PlanningScene(is_diff=True, allowed_collision_matrix=acm))

    def _apply_scene(self, scene):
        self._call(self._scene_client, ApplyPlanningScene.Request(scene=scene))

    def _call(self, client, request):
        if not client.wait_for_service(timeout_sec=10.0):
            raise RuntimeError(f'Service {client.srv_name} is not available. Is MoveIt running?')
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self.node, future)
        return future.result()

    def _log(self, text):
        self.node.get_logger().info(text)
