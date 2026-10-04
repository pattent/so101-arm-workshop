"""Exercise 3: a node that listens AND talks.

It listens to the joint angles, works out whether the arm is moving, and publishes
"moving" or "still" on its own topic, /arm_status, but only when that changes.
Lots of robot nodes look like this: take messages in, work something out, send a
simpler message out for other nodes to use.

Run (with the stage 1 simulation running):  python ex3_motion_detector.py
Watch its topic:  ros2 topic echo /arm_status
Then move the arm (RViz, or one of your Lesson 2 programs).
"""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import String

# How much (radians) the joints must change between two messages to count as moving.
MOVING_THRESHOLD = 0.0005


class MotionDetector(Node):

    def __init__(self):
        super().__init__('motion_detector')
        self.status_pub = self.create_publisher(String, '/arm_status', 10)
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)
        self.last_positions = None   # the angles in the previous message
        self.last_status = None      # what we last published

    def on_joints(self, msg):
        if self.last_positions is None:
            self.last_positions = list(msg.position)
            return

        # TODO 1: Add up how much each joint changed since the last message:
        #             change = sum of abs(new - old) for each joint
        #         (zip(msg.position, self.last_positions) pairs them up.)
        #         Then save the new positions in self.last_positions for next time.
        change = 0.0

        status = 'moving' if change > MOVING_THRESHOLD else 'still'

        # TODO 2: If status is different from self.last_status, publish it as a String
        #         on self.status_pub, print it, and remember it in self.last_status.


def main():
    rclpy.init()
    try:
        rclpy.spin(MotionDetector())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()

# TODO 3: The joint_states arrive 100 times a second, so a tiny pause in the middle of a
#         move can flicker "still" for a moment. How could you make it say "still" only
#         after the arm has been still for half a second? (Try it!)
