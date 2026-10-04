"""Solution: Exercise 3 (including TODO 3: say "still" only after 0.5 s without moving)."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import String

MOVING_THRESHOLD = 0.0005
STILL_TIME = 0.5   # seconds without moving before we say "still"


class MotionDetector(Node):

    def __init__(self):
        super().__init__('motion_detector')
        self.status_pub = self.create_publisher(String, '/arm_status', 10)
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)
        self.last_positions = None
        self.last_status = None
        self.last_moved = self.get_clock().now()   # TODO 3

    def on_joints(self, msg):
        if self.last_positions is None:
            self.last_positions = list(msg.position)
            return

        # TODO 1
        change = 0.0
        for new, old in zip(msg.position, self.last_positions):
            change += abs(new - old)
        self.last_positions = list(msg.position)

        # TODO 3: remember when we last moved, and only call it still after STILL_TIME
        now = self.get_clock().now()
        if change > MOVING_THRESHOLD:
            self.last_moved = now
        still_for = (now - self.last_moved).nanoseconds / 1e9
        status = 'still' if still_for > STILL_TIME else 'moving'

        # TODO 2
        if status != self.last_status:
            self.status_pub.publish(String(data=status))
            print('The arm is', status)
            self.last_status = status


def main():
    rclpy.init()
    try:
        rclpy.spin(MotionDetector())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
