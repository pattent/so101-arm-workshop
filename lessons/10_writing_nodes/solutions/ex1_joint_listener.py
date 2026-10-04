"""Solution: Exercise 1."""

import math

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState


class JointListener(Node):

    def __init__(self):
        super().__init__('joint_listener')
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)
        self.last_pan = None   # TODO 3: shoulder_pan (degrees) the last time we printed

    def on_joints(self, msg):
        # TODO 3: only print when shoulder_pan moved more than 1 degree
        pan = math.degrees(msg.position[msg.name.index('shoulder_pan')])
        if self.last_pan is not None and abs(pan - self.last_pan) <= 1.0:
            return
        self.last_pan = pan

        # TODO 1 and 2
        for name, angle in zip(msg.name, msg.position):
            print(f'{name}: {math.degrees(angle):.1f}°')
        print()


def main():
    rclpy.init()
    node = JointListener()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
