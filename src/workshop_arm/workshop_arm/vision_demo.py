"""Preview of the Gold project: use the camera to find blocks, then sort them.

The robot does NOT know where the blocks are. It looks with the camera
(/detected_blocks from block_detector), picks one up, puts it in the bin of the
same color, and looks again, until there are no blocks left.

Start the stage 3 simulation first (random blocks + camera + block detector):
    ros2 launch workshop_arm workshop.launch.py stage:=3
Then:
    ros2 run workshop_arm vision_demo
"""

import rclpy
from rclpy.duration import Duration
from rclpy.time import Time
from visualization_msgs.msg import MarkerArray

from workshop_arm import Arm
from workshop_arm.arm import BIN_SIZE
from workshop_arm.table import BINS

GRAB_Z = 0.015
SAFE_Z = 0.12
MAX_MISSES = 3


class Eyes:
    """Remembers the latest blocks the camera saw."""

    def __init__(self, arm):
        self.node = arm.node
        self.latest = None
        self.node.create_subscription(MarkerArray, '/detected_blocks', self.on_blocks, 1)

    def on_blocks(self, msg):
        self.latest = msg

    def look(self):
        """Wait for a fresh camera picture and return [(color, x, y), ...]."""
        asked_at = self.node.get_clock().now()
        give_up_at = asked_at + Duration(seconds=10)
        while True:
            rclpy.spin_once(self.node, timeout_sec=0.1)
            if self.latest and Time.from_msg(self.latest.markers[0].header.stamp) > asked_at:
                break
            if self.node.get_clock().now() > give_up_at:
                raise RuntimeError('No pictures from the block detector. Did you start the '
                                   'simulation with stage:=3? (Stages 1 and 2 have no camera.)')
        return [(m.ns, m.pose.position.x, m.pose.position.y)
                for m in self.latest.markers if m.action == m.ADD]


def in_a_bin(x, y):
    return any(abs(x - bx) < BIN_SIZE / 2 and abs(y - by) < BIN_SIZE / 2
               for bx, by in BINS.values())


def main():
    arm = Arm()
    eyes = Eyes(arm)
    misses = 0

    while misses < MAX_MISSES:
        # Get out of the camera's way, then look.
        arm.go_to('look')
        blocks = [b for b in eyes.look() if not in_a_bin(b[1], b[2])]
        print(f'I see {len(blocks)} block(s) to sort: '
              + ', '.join(f'{c} at ({x:.3f}, {y:.3f})' for c, x, y in blocks))
        if not blocks:
            break

        color, x, y = blocks[0]
        arm.open_gripper()
        arm.move_to(x, y, SAFE_Z)
        arm.move_to(x, y, GRAB_Z)
        if not arm.grab():
            misses += 1
            arm.move_to(x, y, SAFE_Z)
            continue
        arm.move_to(x, y, SAFE_Z)

        bin_x, bin_y = BINS[color]
        arm.move_to(bin_x, bin_y, SAFE_Z)
        arm.release()

    arm.go_to('rest')
    print('Done! The table is clean.' if misses < MAX_MISSES else 'Too many misses, giving up.')
    arm.shutdown()


if __name__ == '__main__':
    main()
