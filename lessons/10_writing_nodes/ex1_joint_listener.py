"""Exercise 1: a subscriber, a node that listens to a topic.

It listens to /follower/joint_states (the arm's joint angles, about 100 times a second)
and prints them. Look for three ideas from Lessons 5 and 6: a class that inherits from Node,
super().__init__(), and a callback.

Run (with the stage 1 simulation running):  python ex1_joint_listener.py
Stop it with Ctrl+C.
"""

import math

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState     # the message type (see: ros2 topic info)


class JointListener(Node):                 # a JointListener IS a Node

    def __init__(self):
        super().__init__('joint_listener')  # Node sets itself up, with this node's name
        # "Whenever a message arrives on this topic, call self.on_joints with it."
        # (10 = how many messages to keep in line if we're slow to handle them.)
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)

    def on_joints(self, msg):
        # A JointState message has lists: msg.name[0] goes with msg.position[0], and so on.
        print(msg.name[0], msg.position[0])

        # TODO 1: Print EVERY joint's name and angle, not just the first one.
        #         (Hint: zip(msg.name, msg.position) pairs them up for a for loop.)

        # TODO 2: The angles are in radians. Print them in degrees, rounded to 1 decimal.
        #         (math.degrees, and an f-string with {angle:.1f})

        # TODO 3: 100 messages a second is a lot to read! Only print when shoulder_pan
        #         changes by more than 1 degree since the last time you printed.
        #         (Hint: remember the last value in self, like ClosestTracker in Lesson 6.
        #         Set it up in __init__.)


def main():
    rclpy.init()                  # start ROS for this program
    node = JointListener()
    try:
        rclpy.spin(node)          # wait for messages and call the callbacks, forever
    except (KeyboardInterrupt, ExternalShutdownException):
        pass                      # Ctrl+C: stop quietly instead of printing an error


if __name__ == '__main__':
    main()
