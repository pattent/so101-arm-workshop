"""Solution: Bronze challenge (one possible dance)."""

import time

from workshop_arm import Arm

moves = {
    'up': [0, -90, 0, 0, 0],
    'lean_left': [-45, -60, 30, 20, 0],
    'lean_right': [45, -60, 30, 20, 0],
    'bow': [0, -20, 20, 70, 0],
    'twist': [0, -90, 0, 0, 90],
}


def wave(arm, times):
    arm.move_joints(*moves['up'])
    for i in range(times):
        arm.move_joints(0, -90, 0, 40, 0)
        arm.move_joints(0, -90, 0, -40, 0)


def clap(arm, times):
    for i in range(times):
        arm.close_gripper()
        arm.open_gripper()


choreography = ['up', 'lean_left', 'lean_right', 'lean_left', 'lean_right', 'twist', 'up']

arm = Arm()
arm.go_to('rest')
start = time.time()

arm.speed = 0.3                 # slow start
wave(arm, 2)

arm.speed = 0.8                 # the fast part
for name in choreography:
    if not arm.move_joints(*moves[name]):
        print(f'Skipping {name}')
clap(arm, 3)

arm.speed = 0.3                 # slow finish
arm.move_joints(*moves['bow'])

print(f'The dance took {time.time() - start:.1f} seconds.')
arm.go_to('rest')
arm.shutdown()
