"""Solution: Challenge (one possible answer)."""

from workshop_arm import Arm

arm = Arm()

print('Going to the rest pose...')
arm.go_to('rest')

arm.move_joints(0, -45, 45, 45, 0)
print('The gripper is now at', arm.where_am_i())

# TODO 1: negative shoulder_pan turns the arm to its left.
arm.move_joints(-60, -45, 45, 45, 0)
print('Turned left, gripper at', arm.where_am_i())

# TODO 2: straight up.
arm.move_joints(0, -90, 0, 0, 0)
print('Pointing up, gripper at', arm.where_am_i())

# TODO 3: my own pose: reaching out to the right, wrist twisted.
arm.move_joints(45, 0, 0, 30, 90)
print('My pose, gripper at', arm.where_am_i())

arm.go_to('rest')
arm.shutdown()
