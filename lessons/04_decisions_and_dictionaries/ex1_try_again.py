"""Exercise 1: making decisions with if / else.

Run (with the stage 1 simulation running):  python ex1_try_again.py
"""

from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')

# move_to gives back True if it worked, False if it couldn't.
ok = arm.move_to(0.25, 0.0, 0.15)
print('Did the first move work?', ok)

if ok:
    print('Yes! The gripper is at', arm.where_am_i())
else:
    print('No, that point was not reachable.')

# This point is too far away for the arm to reach.
far_away = (0.60, 0.0, 0.10)

# TODO 1: Try to move to far_away. If it doesn't work, print a message and
#         move to a closer backup point instead, e.g. (0.30, 0.0, 0.10).

# TODO 2: Write a function try_points(arm, points) that tries each point in a list
#         and STOPS at the first one that works. Print which one worked.
#         (Hint: `return` leaves a function right away.)

arm.go_to('rest')
arm.shutdown()
