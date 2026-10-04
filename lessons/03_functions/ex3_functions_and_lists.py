"""Exercise 3: functions that work on lists (no robot needed).

A function can take a whole list as its input, and give back a number, an item from the
list, or even a brand new list.

Run:  python ex3_functions_and_lists.py
"""

import math

points = [(0.25, 0.10), (0.30, -0.10), (0.40, 0.30), (0.15, 0.05), (0.50, -0.20)]


# A function that takes a list and gives back one number.
def average_x(points):
    total = 0
    for x, y in points:
        total = total + x
    return total / len(points)


print('The average x is', average_x(points))

# TODO 1: Copy your distance_from_base(x, y) function from Lesson 1 (exercise 3) here.

# The next two need a sneak peek at `if` (Lesson 4 covers it properly). The indented lines
# under an `if` only run when its comparison is True:
#     if distance_from_base(x, y) < 0.44:
#         print('I can reach that!')

# TODO 2: Write a function closest_point(points) that returns the point closest to the base.
#         Use distance_from_base: start with closest = points[0], loop over the points, and
#         use `if` to replace closest whenever you find a nearer one.
#         (Hint: closest_x, closest_y = closest pulls the closest point apart again.)
#         Test it: it should be (0.15, 0.05).

# TODO 3: Write a function reachable(points, max_reach) that returns a NEW list with only
#         the points the arm can reach. Start with an empty list, and append each point
#         whose distance is less than max_reach.
#         Test it: reachable(points, 0.44) should give back 3 points.
