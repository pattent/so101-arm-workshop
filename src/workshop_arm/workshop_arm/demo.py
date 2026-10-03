"""Preview of the final project: sort colored blocks into matching bins.

Run it (with the robot launch file already running in another terminal):
    ros2 run workshop_arm demo
"""

from workshop_arm import Arm

# Where things are on the table (x forward, y left), in meters.
BLOCKS = {
    'red_block': (0.22, -0.10, 'red'),
    'blue_block': (0.28, 0.02, 'blue'),
}
BINS = {
    'red': (0.12, 0.22),
    'blue': (0.24, 0.20),
}
GRAB_Z = 0.015   # gripper height for grabbing a block
SAFE_Z = 0.12    # height for moving around without hitting anything


def pick(arm, name, x, y):
    arm.move_to(x, y, SAFE_Z)      # above the block
    arm.move_to(x, y, GRAB_Z)      # down
    arm.grab(name)
    arm.move_to(x, y, SAFE_Z)      # back up


def place(arm, x, y):
    arm.move_to(x, y, SAFE_Z)      # above the bin
    arm.release()


def main():
    arm = Arm()

    # Set up the table.
    for color, (x, y) in BINS.items():
        arm.add_bin(f'{color}_bin', x, y, color=color)
    for name, (x, y, color) in BLOCKS.items():
        arm.add_block(name, x, y, color=color)

    arm.go_to('rest')
    arm.open_gripper()

    # Sort each block into the bin of the same color.
    for name, (x, y, color) in BLOCKS.items():
        pick(arm, name, x, y)
        bin_x, bin_y = BINS[color]
        place(arm, bin_x, bin_y)

    arm.go_to('rest')
    print('Done! All blocks sorted.')
    arm.shutdown()


if __name__ == '__main__':
    main()
