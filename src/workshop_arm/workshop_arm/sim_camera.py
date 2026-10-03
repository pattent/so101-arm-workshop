"""A pretend overhead camera for the simulation.

It looks at what's on the table in MoveIt's planning scene and draws the picture a
real camera hanging above the table would see (with a little noise and blur, like
a cheap webcam). It publishes:
    /camera/image_raw     sensor_msgs/Image
    /camera/camera_info   sensor_msgs/CameraInfo

Run:  ros2 run workshop_arm sim_camera
View: ros2 run rqt_image_view rqt_image_view /camera/image_raw
"""

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo, Image

from moveit_msgs.srv import GetPlanningScene
from workshop_arm.arm import BIN_HEIGHT, BIN_SIZE, BLOCK_SIZE, objects_in_scene, scene_request
from workshop_arm.table import (
    CAMERA_FOCAL, CAMERA_HEIGHT, CAMERA_HEIGHT_PX, CAMERA_WIDTH, CAMERA_X, CAMERA_Y,
)

TABLE_BGR = (150, 180, 200)    # light wood
BIN_FLOOR_BGR = (120, 120, 120)
RIM_WIDTH = 0.008              # bin rim thickness, meters


def table_to_pixel(x, y, z):
    """Where a point on/above the table shows up in the image (pinhole camera model)."""
    distance = CAMERA_HEIGHT - z            # how far the point is below the camera
    u = CAMERA_WIDTH / 2 - CAMERA_FOCAL * (y - CAMERA_Y) / distance
    v = CAMERA_HEIGHT_PX / 2 - CAMERA_FOCAL * (x - CAMERA_X) / distance
    return u, v


def draw_square(image, x, y, z, size, bgr):
    u, v = table_to_pixel(x, y, z)
    half = CAMERA_FOCAL * size / (CAMERA_HEIGHT - z) / 2
    cv2.rectangle(image, (round(u - half), round(v - half)), (round(u + half), round(v + half)),
                  bgr, thickness=-1)


class SimCamera(Node):

    def __init__(self):
        super().__init__('sim_camera')
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 1)
        self.info_pub = self.create_publisher(CameraInfo, '/camera/camera_info', 1)
        self.scene_client = self.create_client(GetPlanningScene, '/get_planning_scene')
        self.objects = {}
        self.pending = None
        self.rng = np.random.default_rng()
        self.create_timer(0.2, self.take_picture)   # 5 pictures per second

    def take_picture(self):
        # Ask MoveIt what's on the table (the answer arrives later, in on_scene).
        if self.pending is None and self.scene_client.service_is_ready():
            self.pending = self.scene_client.call_async(scene_request())
            self.pending.add_done_callback(self.on_scene)

        image = np.full((CAMERA_HEIGHT_PX, CAMERA_WIDTH, 3), TABLE_BGR, dtype=np.uint8)
        # The robot's base, for reference.
        u, v = table_to_pixel(0.0, 0.0, 0.05)
        cv2.circle(image, (round(u), round(v)), 40, (60, 60, 60), thickness=-1)

        bins = [o for o in self.objects.values() if o['kind'] == 'bin']
        blocks = [o for o in self.objects.values() if o['kind'] == 'block']
        for obj in bins:
            top = obj['z'] + BIN_HEIGHT / 2
            draw_square(image, obj['x'], obj['y'], top, BIN_SIZE, to_bgr(obj['color']))
            draw_square(image, obj['x'], obj['y'], top, BIN_SIZE - 2 * RIM_WIDTH, BIN_FLOOR_BGR)
        for obj in sorted(blocks, key=lambda o: o['z']):
            top = obj['z'] + BLOCK_SIZE / 2
            draw_square(image, obj['x'], obj['y'], top, BLOCK_SIZE, to_bgr(obj['color']))

        # Make it look like a real (cheap) camera.
        image = cv2.GaussianBlur(image, (5, 5), 0)
        noise = self.rng.normal(0, 6, image.shape)
        image = np.clip(image + noise, 0, 255).astype(np.uint8)

        stamp = self.get_clock().now().to_msg()
        self.image_pub.publish(to_image_msg(image, stamp))
        self.info_pub.publish(camera_info(stamp))

    def on_scene(self, future):
        self.pending = None
        if future.result() is not None:
            self.objects = objects_in_scene(future.result().scene)


def to_bgr(rgb):
    r, g, b = rgb
    return (int(b * 255), int(g * 255), int(r * 255))


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
