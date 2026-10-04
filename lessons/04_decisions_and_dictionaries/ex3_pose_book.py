"""Exercise 3: a pose book, with a while loop.

A dictionary maps names to values, like the contacts on your phone map names to numbers.

Run (with the stage 1 simulation running):  python ex3_pose_book.py
Then type a pose name and press Enter. Type quit to stop.
"""

from workshop_arm import Arm

# Each name maps to five joint angles in degrees:
# [shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll]
poses = {
    'up': [0, -90, 0, 0, 0],
    'reach': [0, -45, 45, 45, 0],
}

# TODO 1: Add at least two more poses of your own, like 'look_left' and 'bow'.

arm = Arm()
arm.go_to('rest')

name = ''
while name != 'quit':
    name = input('Which pose? ')
    # TODO 2: If the name is in the dictionary, move there with
    #             arm.move_joints(*poses[name])
    #         (the * spreads the list out into the five inputs).
    #         If it isn't (and isn't 'quit'), print the names you CAN use:
    #             print('Try one of:', list(poses))

arm.go_to('rest')
arm.shutdown()
