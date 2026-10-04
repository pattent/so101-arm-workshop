"""Exercise 2, part 2: listen to the talker.

Run:  python ex2_listener.py   (while ex2_talker.py runs in another terminal)
"""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):

    def __init__(self):
        super().__init__('listener')
        # TODO 3: Subscribe to /chatter (type String), with a callback self.on_chatter.

    # TODO 3: Write on_chatter(self, msg) that prints 'I heard: ' and msg.data.


def main():
    rclpy.init()
    try:
        rclpy.spin(Listener())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()

# TODO 4: Start TWO listeners (two terminals) and one talker. Do both hear every message?
#         Now start two talkers. What does a listener hear? Look at it all in rqt_graph.
