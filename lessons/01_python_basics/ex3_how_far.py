"""Exercise 3: how far is the gripper from the robot? Write functions to find out.

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

# Doing that math by hand for every point would get old fast. That's what functions are for.

# TODO 2: Write a function distance_from_base(x, y) that RETURNS the distance.
#         A function can have more than one input: def distance_from_base(x, y):
#         Test it on the point above, then on (0.30, -0.10). (About 0.269 and 0.316.)

# TODO 3: The SO-101 can reach about 0.48 m from its base. Write a function
#         can_reach(x, y) that returns True if the point is close enough, and False if not.
#         (Hint: a comparison like  distance_from_base(x, y) < 0.48  IS True or False,
#         a bool from exercise 1, so you can return it straight away.)
#         A function can call another function you wrote!
#         Test it: can_reach(0.25, 0.10) should be True; can_reach(0.40, 0.30) False.

# TODO 4: print shows a value; return gives it back. Write a function
#         shout_distance(x, y) that PRINTS the distance instead of returning it. Then try:
#             result = shout_distance(0.25, 0.10)
#             print('It gave back:', result)
#         What did it give back? Why?
