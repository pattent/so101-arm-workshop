"""ROS node that finds blocks in the camera image.

Subscribes:
    /camera/image_raw     sensor_msgs/Image
    /camera/camera_info   sensor_msgs/CameraInfo
Publishes:
    /detected_blocks      visualization_msgs/MarkerArray   (one marker per block, in meters;
                                                             the marker's `ns` is its color)
    /vision/debug_image   sensor_msgs/Image                (camera image with labels drawn on)

Run:  ros2 run workshop_arm block_detector
View: ros2 run rqt_image_view rqt_image_view /vision/debug_image
"""

import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo, Image
from visualization_msgs.msg import Marker, MarkerArray

from workshop_arm.arm import BLOCK_SIZE, COLORS
from workshop_arm.vision import draw_blocks, find_blocks, pixel_to_table


class BlockDetector(Node):

    def __init__(self):
        super().__init__('block_detector')
        self.camera_info = None
        self.create_subscription(CameraInfo, '/camera/camera_info', self.on_camera_info, 1)
        self.create_subscription(Image, '/camera/image_raw', self.on_image, 1)
        self.blocks_pub = self.create_publisher(MarkerArray, '/detected_blocks', 1)
        self.debug_pub = self.create_publisher(Image, '/vision/debug_image', 1)

    def on_camera_info(self, msg):
        self.camera_info = msg

    def on_image(self, msg):
        if self.camera_info is None:
            return
        image = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)

        # The camera matrix K holds the focal length and the image center.
        k = self.camera_info.k
        focal, center_u, center_v = k[0], k[2], k[5]

        blocks = find_blocks(image)
        for b in blocks:
            b['x'], b['y'] = pixel_to_table(b['u'], b['v'], focal, center_u, center_v)

        self.blocks_pub.publish(self.to_markers(blocks, msg.header.stamp))
        debug = Image()
        debug.header = msg.header
        debug.height, debug.width, debug.encoding, debug.step = msg.height, msg.width, 'bgr8', msg.step
        debug.data = draw_blocks(image, blocks).tobytes()
        self.debug_pub.publish(debug)

    def to_markers(self, blocks, stamp):
        markers = MarkerArray()
        clear = Marker(action=Marker.DELETEALL)
        clear.header.frame_id = 'base_link'
        clear.header.stamp = stamp
        markers.markers.append(clear)
        for i, b in enumerate(blocks):
            m = Marker(type=Marker.CUBE, action=Marker.ADD, id=i, ns=b['color'])
            m.header.frame_id = 'base_link'
            m.header.stamp = stamp
            m.pose.position.x, m.pose.position.y, m.pose.position.z = b['x'], b['y'], BLOCK_SIZE / 2
            m.pose.orientation.w = 1.0
            m.scale.x = m.scale.y = m.scale.z = BLOCK_SIZE * 1.2
            m.color.r, m.color.g, m.color.b = COLORS[b['color']]
            m.color.a = 0.4
            markers.markers.append(m)
        return markers


def main():
    rclpy.init()
    rclpy.spin(BlockDetector())


if __name__ == '__main__':
    main()
