"""Solution: Exercise 2, part 2."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):

    def __init__(self):
        super().__init__('listener')
        # TODO 3
        self.create_subscription(String, '/chatter', self.on_chatter, 10)

    def on_chatter(self, msg):
        print('I heard:', msg.data)


def main():
    rclpy.init()
    try:
        rclpy.spin(Listener())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()

# TODO 4: every listener hears every message (a topic is like a radio station: any number
# of talkers and listeners). With two talkers, a listener hears both, mixed together.
