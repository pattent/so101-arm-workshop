"""Challenge: a safety monitor node.

Watch where the gripper is, and warn whenever it goes lower than 3 cm above the table.

Where is the gripper? ROS keeps track of where every part of the robot is with **TF**
(Lesson 12 explains it). The lines marked "TF" below set that up for you; this one line
asks "where is the gripper, measured from the robot's base?":

    t = self.tf_buffer.lookup_transform('base_link', 'gripper_frame_link', Time())
    height = t.transform.translation.z      # meters above the table

Run (with the stage 1 simulation running):  python challenge_safety_monitor.py
Test it: make the arm go low, e.g. arm.move_to(0.25, 0.0, 0.02) in a little program
(or run the stage 2 demo, which grabs blocks at 1.5 cm).

Steps:
  1. Make a timer that calls self.check every 0.2 seconds.
  2. In check: look up the gripper's height (above), and if it's below MIN_HEIGHT,
     print a warning with the height in centimeters.
  3. The lookup fails with an error for the first moment after starting, before TF has
     heard where everything is. Catch it with try / except tf2_ros.TransformException,
     and just return (skip this check).
  4. Also publish the warnings, as String messages on a topic /safety_warnings, so other
     nodes could react. Check with: ros2 topic echo /safety_warnings

Bonus: warn only once each time the gripper goes too low, not 5 times a second.
"""

import rclpy
import tf2_ros
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.time import Time
from std_msgs.msg import String

MIN_HEIGHT = 0.03   # meters


class SafetyMonitor(Node):

    def __init__(self):
        super().__init__('safety_monitor')
        # TF: a buffer that remembers where every robot part is, and a listener that
        # fills it from the /tf topics.
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        # TODO 1 and 4


    # TODO 2 and 3: def check(self):


def main():
    rclpy.init()
    try:
        rclpy.spin(SafetyMonitor())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
