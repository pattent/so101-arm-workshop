"""Exercise 3: counting with range.

range makes a list of numbers for a for loop to count through:
    range(3)              0, 1, 2           (starts at 0, stops BEFORE 3)
    range(-60, 61, 30)    -60, -30, 0, 30, 60   (start, stop before, step)

Run (with the stage 1 simulation running):  python ex3_sweep.py
"""

from workshop_arm import Arm

for i in range(3):
    print('Counting:', i)
print('The sweep angles:', list(range(-60, 61, 30)))

arm = Arm()
arm.go_to('rest')

# Sweep the arm from its left to its right, 30 degrees at a time.
# (Negative shoulder_pan turns the arm to its LEFT.)
for pan in range(-60, 61, 30):
    print('shoulder_pan =', pan)
    arm.move_joints(pan, -45, 45, 45, 0)

# TODO 1: Sweep back the other way, from right to left.
#         (Hint: a negative step counts down: range(60, -61, -30))

# TODO 2: Sweep left to right again in smaller steps of 15 degrees, and count the moves:
#         make a variable moves = 0 before the loop, and add 1 to it inside the loop.
#         Print it at the end.

# TODO 3: Remember where the gripper was after each move of that sweep. Make an empty list
#         positions = [] before the loop, and append arm.where_am_i() inside it.
#         Print the list at the end, then print just the first and the last position.

arm.go_to('rest')
arm.shutdown()
