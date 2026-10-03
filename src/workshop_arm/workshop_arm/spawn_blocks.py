"""Set up the table: bins in their fixed spots and blocks scattered at random.

Run:  ros2 run workshop_arm spawn_blocks            (5 random blocks)
      ros2 run workshop_arm spawn_blocks 8          (8 blocks)
      ros2 run workshop_arm spawn_blocks 5 42       (same layout every time: "seed" 42)
"""

import math
import random
import sys

from workshop_arm import Arm
from workshop_arm.table import BINS, BLOCK_AREA_X, BLOCK_AREA_Y

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
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    count = int(args[0]) if args else 5
    if len(args) > 1:
        random.seed(int(args[1]))

    arm = Arm()
    arm.clear_table()
    for color, (x, y) in BINS.items():
        arm.add_bin(f'{color}_bin', x, y, color=color)
    for i, (x, y) in enumerate(random_spots(count)):
        arm.add_block(f'block_{i}', x, y, color=random.choice(list(BINS)))
    print(f'Put {count} blocks on the table.')
    arm.shutdown()


if __name__ == '__main__':
    main()
