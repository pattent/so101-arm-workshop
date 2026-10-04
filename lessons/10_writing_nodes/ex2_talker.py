"""Exercise 2, part 1: a publisher, a node that talks on a topic.

It sends a message on /chatter twice a second. Run ex2_listener.py in another terminal to
hear it, or listen with:  ros2 topic echo /chatter

Run:  python ex2_talker.py   (no simulation needed)
"""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, '/chatter', 10)
        self.count = 0
        # A timer is a callback too: "call self.on_timer every 0.5 seconds".
        self.create_timer(0.5, self.on_timer)

    def on_timer(self):
        self.count += 1
        msg = String()
        msg.data = f'Hello from the talker! (message {self.count})'
        self.publisher.publish(msg)
        print('Sent:', msg.data)

    # TODO 2: Make the talker stop after 10 messages. (Hint: in on_timer, if the count
    #         reaches 10, call rclpy.shutdown(). spin() then stops.)


def main():
    rclpy.init()
    try:
        rclpy.spin(Talker())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()

# TODO 1: While the talker runs, in another terminal try:
#             ros2 topic list
#             ros2 topic echo /chatter
#             ros2 topic hz /chatter
#         Then change the timer to 0.1 seconds. What does `ros2 topic hz` say now?
