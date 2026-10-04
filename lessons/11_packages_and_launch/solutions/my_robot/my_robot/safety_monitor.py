"""Warn whenever the gripper goes too low. (Lesson 10's challenge, now with a parameter.)

Run:  ros2 run my_robot safety_monitor
      ros2 run my_robot safety_monitor --ros-args -p min_height:=0.05
"""

import rclpy
import tf2_ros
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.time import Time
from std_msgs.msg import String


class SafetyMonitor(Node):

    def __init__(self):
        super().__init__('safety_monitor')
        # A parameter: a setting you can change when starting the node, without editing
        # the code. 0.03 is the default if nobody sets it.
        self.declare_parameter('min_height', 0.03)
        self.min_height = self.get_parameter('min_height').value
        # get_logger() instead of print: under `ros2 launch`, print's output can show up late
        # (Python saves it up), but log messages appear right away, with a level and a time.
        self.get_logger().info(f'Watching the gripper. Warning below {self.min_height * 100:.1f} cm.')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.warning_pub = self.create_publisher(String, '/safety_warnings', 10)
        self.create_timer(0.2, self.check)
        self.too_low = False

    def check(self):
        try:
            t = self.tf_buffer.lookup_transform('base_link', 'gripper_frame_link', Time())
        except tf2_ros.TransformException:
            return
        height = t.transform.translation.z
        if height < self.min_height and not self.too_low:
            warning = f'Careful! The gripper is only {height * 100:.1f} cm above the table.'
            self.get_logger().warning(warning)
            self.warning_pub.publish(String(data=warning))
        self.too_low = height < self.min_height


def main():
    rclpy.init()
    try:
        rclpy.spin(SafetyMonitor())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
