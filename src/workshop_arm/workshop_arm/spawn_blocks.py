"""Set up the table: bins in their fixed spots, plus blocks.

Run:  ros2 run workshop_arm spawn_blocks known        (stage 2: blocks at the spots in table.py)
      ros2 run workshop_arm spawn_blocks random       (stage 3: 5 blocks at random spots)
      ros2 run workshop_arm spawn_blocks random 8     (8 random blocks)
      ros2 run workshop_arm spawn_blocks random 5 42  (same random layout every time: "seed" 42)
"""

import math
import random
import sys

from rclpy.utilities import remove_ros_args

from workshop_arm import Arm
from workshop_arm.table import BINS, BLOCK_AREA_X, BLOCK_AREA_Y, KNOWN_BLOCKS

MIN_SPACING = 0.05   # meters between block centers, so the gripper fits


def random_spots(count):
    spots = []
    for _ in range(100000):
        if len(spots) == count:
            return spots
        x = random.uniform(*BLOCK_AREA_X)
        y = random.uniform(*BLOCK_AREA_Y)
        if all(math.dist((x, y), s) >= MIN_SPACING for s in spots):
            spots.append((x, y))
    raise ValueError(f'Could not fit {count} blocks on the table. Try fewer.')


def main():
    args = remove_ros_args(sys.argv)[1:]
    layout = args[0] if args else 'known'
    if layout == 'known':
        blocks = list(KNOWN_BLOCKS.values())
    elif layout == 'random':
        count = int(args[1]) if len(args) > 1 else 5
        if len(args) > 2:
            random.seed(int(args[2]))
        blocks = [(x, y, random.choice(list(BINS))) for x, y in random_spots(count)]
    else:
        sys.exit(f"Unknown layout {layout!r}: use 'known' or 'random'")

    arm = Arm()
    arm.clear_table()
    for color, (x, y) in BINS.items():
        arm.add_bin(f'{color}_bin', x, y, color=color)
    for i, (x, y, color) in enumerate(blocks):
        arm.add_block(f'block_{i}', x, y, color=color)
    print(f'Put {len(blocks)} blocks on the table ({layout} layout).')
    arm.shutdown()


if __name__ == '__main__':
    main()
