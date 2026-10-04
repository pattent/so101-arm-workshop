"""Solution: Challenge (one possible answer)."""

import math

# workshop_arm is our own package (in src/workshop_arm/). Arm is the robot arm.
from workshop_arm import Arm


# TODO 4: copied from exercise 3.
def distance_from_base(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def can_reach(x, y):
    return distance_from_base(x, y) < 0.48


arm = Arm()     # connect to the robot (the simulation must be running)

print('Going to the rest pose...')
arm.go_to('rest')

arm.move_joints(0, -45, 45, 45, 0)
print('The gripper is now at', arm.where_am_i())

# TODO 1: negative shoulder_pan turns the arm to its left.
pan = -60
arm.move_joints(pan, -45, 45, 45, 0)
print(f'Turned to {pan} degrees, gripper at {arm.where_am_i()}')

# TODO 2: straight up.
arm.move_joints(0, -90, 0, 0, 0)
print('Pointing up, gripper at', arm.where_am_i())

# TODO 3: slow, then fast.
arm.speed = 0.2
arm.go_to('rest')
arm.speed = 1.0
arm.move_joints(0, -90, 0, 0, 0)

# TODO 4
ok = arm.move_to(0.25, 0.0, 0.10)
print('Did it work?', ok, type(ok))           # True <class 'bool'>
ok = arm.move_to(0.60, 0.0, 0.10)
print('And the far point?', ok)               # False: the arm can't reach that far
print('My can_reach says', can_reach(0.60, 0.0))   # False too: they agree

# TODO 5: my own pose: reaching out to the right, wrist twisted.
arm.move_joints(45, 0, 0, 30, 90)
print(f'My pose: gripper at {arm.where_am_i()}')


# Bonus
def show_pose(arm, pan):
    arm.move_joints(pan, -45, 45, 45, 0)
    print(f'With shoulder_pan at {pan}, the gripper is at', arm.where_am_i())


show_pose(arm, -60)
show_pose(arm, 0)
show_pose(arm, 60)

arm.speed = 0.5     # back to the normal speed
arm.go_to('rest')
arm.shutdown()
