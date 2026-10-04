"""Solution: Exercise 2, part 1."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, '/chatter', 10)
        self.count = 0
        self.create_timer(0.5, self.on_timer)

    def on_timer(self):
        self.count += 1
        msg = String()
        msg.data = f'Hello from the talker! (message {self.count})'
        self.publisher.publish(msg)
        print('Sent:', msg.data)
        # TODO 2
        if self.count >= 10:
            rclpy.shutdown()


def main():
    rclpy.init()
    try:
        rclpy.spin(Talker())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()

# TODO 1: with a 0.1 s timer, `ros2 topic hz /chatter` says about 10 (messages per second).
