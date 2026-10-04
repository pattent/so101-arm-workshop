"""Stage 2 example: sort blocks whose positions we already know.

Start the stage 2 simulation first (it puts the bins and blocks on the table):
    ros2 launch workshop_arm workshop.launch.py stage:=2
Then:
    ros2 run workshop_arm demo
"""

import math

from workshop_arm import Arm
from workshop_arm.table import BINS

# Where the blocks are (x forward, y left, in meters) and what color they are.
# Here we just type them in, copied from KNOWN_BLOCKS in table.py.
# In stage 3, vision_demo finds them with the camera instead.
BLOCKS = [
    (0.22, -0.10, 'red'),
    (0.28, 0.02, 'blue'),
    (0.30, -0.12, 'green'),
]
GRAB_Z = 0.015   # gripper height for grabbing a block
SAFE_Z = 0.12    # height for moving around without hitting anything


def pick(arm, x, y):
    arm.move_to(x, y, SAFE_Z)      # above the block
    arm.move_to(x, y, GRAB_Z)      # down
    caught = arm.grab()
    arm.move_to(x, y, SAFE_Z)      # back up
    return caught


def place(arm, x, y):
    arm.move_to(x, y, SAFE_Z)      # above the bin
    arm.release()


def table_is_ready(arm):
    """True if there's a block at every spot in BLOCKS, and no others.

    In stage 3 the blocks are at random spots, and after a run they're in the bins:
    either way this program would grab the wrong things (or nothing).
    """
    blocks = [obj for obj in arm.get_objects().values() if obj['kind'] == 'block']
    found = [any(math.dist((obj['x'], obj['y']), (x, y)) < 0.01 for obj in blocks)
             for x, y, color in BLOCKS]
    return len(blocks) == len(BLOCKS) and all(found)


def main():
    arm = Arm()
    if not table_is_ready(arm):
        print('The blocks are not where this demo expects them.\n'
              'Restart the simulation with stage:=2 (blocks at known spots), then try again.\n'
              'In stage 3 the blocks are at random spots: use  ros2 run workshop_arm vision_demo')
        arm.shutdown()
        return
    arm.go_to('rest')
    arm.open_gripper()

    # Sort each block into the bin of the same color.
    for x, y, color in BLOCKS:
        if not pick(arm, x, y):
            print('No block there. Did you start the simulation with stage:=2?')
            continue
        bin_x, bin_y = BINS[color]
        place(arm, bin_x, bin_y)

    arm.go_to('rest')
    print('Done! All blocks sorted.')
    arm.shutdown()


if __name__ == '__main__':
    main()
