"""Solution: Exercise 2."""

from workshop_arm import Arm

poses = {
    'up': [0, -90, 0, 0, 0],
    'reach': [0, -45, 45, 45, 0],
    'look_left': [-60, -45, 45, 45, 0],   # TODO 1
    'bow': [0, -20, 20, 70, 0],           # TODO 1
}

arm = Arm()
arm.go_to('rest')

name = ''
while name != 'quit':
    name = input('Which pose? ')
    # TODO 2
    if name in poses:
        arm.move_joints(*poses[name])
    elif name != 'quit':
        print('Try one of:', list(poses))

arm.go_to('rest')
arm.shutdown()
