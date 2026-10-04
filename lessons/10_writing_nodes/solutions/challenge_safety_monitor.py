"""Solution: Challenge (including the bonus: warn once each time it goes too low)."""

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
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        # TODO 1 and 4
        self.warning_pub = self.create_publisher(String, '/safety_warnings', 10)
        self.create_timer(0.2, self.check)
        self.too_low = False   # bonus: are we already in the "too low" state?

    def check(self):
        # TODO 3
        try:
            t = self.tf_buffer.lookup_transform('base_link', 'gripper_frame_link', Time())
        except tf2_ros.TransformException:
            return
        # TODO 2
        height = t.transform.translation.z
        if height < MIN_HEIGHT and not self.too_low:
            warning = f'Careful! The gripper is only {height * 100:.1f} cm above the table.'
            print(warning)
            self.warning_pub.publish(String(data=warning))
        self.too_low = height < MIN_HEIGHT


def main():
    rclpy.init()
    try:
        rclpy.spin(SafetyMonitor())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
