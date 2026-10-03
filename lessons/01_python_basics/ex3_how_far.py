"""Exercise 3: how far is the gripper from the robot?

The robot measures positions from its base, in meters:
    x = forward, y = to the robot's left.

        y (left)
        ^
        |      * gripper at (x, y)
        |     /
        |    /  distance = ?
        |   /
        |  /
     [robot]-----------> x (forward)

The Pythagorean theorem: distance = square root of (x squared + y squared).

Run:  python ex3_how_far.py
"""

import math

x = 0.25
y = 0.10

# x ** 2 means "x squared" (x times x).
# TODO 1: Calculate the distance with math.sqrt( ... ) and print it.
distance = 0

print(f'The gripper is {distance:.3f} meters from the base.')

# TODO 2: Python has a shortcut: math.hypot(x, y). Check it gives the same answer.

# The SO-101 can reach about 0.48 m from its base.
max_reach = 0.48

# TODO 3: Is the point (0.40, 0.30) within reach? Calculate its distance and print it.
#         (Next lesson you'll learn how to make Python decide for you, with "if".)
