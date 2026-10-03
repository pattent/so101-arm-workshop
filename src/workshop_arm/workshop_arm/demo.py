"""Stage 2 example: sort blocks whose positions we already know.

Start the stage 2 simulation first (it puts the bins and blocks on the table):
    ros2 launch workshop_arm workshop.launch.py stage:=2
Then:
    ros2 run workshop_arm demo
"""

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


def main():
    arm = Arm()
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
