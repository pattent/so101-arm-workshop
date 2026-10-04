"""Exercise 1: more from your functions (no robot needed).

In Lesson 1 you wrote your first functions: to_degrees, distance_from_base and can_reach.
Now three new tricks: inputs with a default value, giving back two answers at once, and
functions that build on each other.

Run:  python ex1_more_functions.py
"""

import math


# Your functions from Lesson 1, exercise 3.
def distance_from_base(x, y):
    return math.sqrt(x ** 2 + y ** 2)


# Trick 1: a DEFAULT value. If you don't give max_reach, it's 0.48.
def can_reach(x, y, max_reach=0.48):
    return distance_from_base(x, y) < max_reach


print(can_reach(0.40, 0.20))                  # uses the default, 0.48
print(can_reach(0.40, 0.20, max_reach=0.40))  # a smaller robot

# TODO 1: The arm we use really reaches about 0.44 m (from its shoulder). Is (0.40, 0.15)
#         reachable with the default? With max_reach=0.44? Print both.


# Trick 2: give back TWO answers, as a tuple (Lesson 2). Unpack them when you call it.
def split_angle(degrees):
    """How many whole turns, and how many degrees left over?"""
    turns = degrees // 360          # // divides and throws away the remainder
    left_over = degrees % 360       # % gives just the remainder
    return turns, left_over


turns, left_over = split_angle(800)
print(f'800 degrees is {turns} full turns and {left_over} degrees')

# TODO 2: Write point_on_circle(center_x, center_y, radius, degrees) that returns the (x, y)
#         of the point at that angle around the circle. Remember from Lesson 2's circle:
#             x = center_x + radius * math.cos(angle)
#             y = center_y + radius * math.sin(angle)
#         but the angle must be in RADIANS (math.radians). Test it:
#             point_on_circle(0.25, 0.0, 0.05, 90)  should be about (0.25, 0.05)
#         (You may see something like 3.06e-18. That's scientific notation for
#         0.00000000000000000306: computers store decimals with a tiny rounding error, so
#         "zero" can come out as almost-zero. Round it to see the real answer.)


# Trick 3: functions that use other functions, and give back text.
# TODO 3: Write describe(x, y) that RETURNS a sentence like
#             '(0.25, 0.1) is 0.269 m away, and I can reach it: True'
#         using distance_from_base and can_reach. Then print describe(...) for each point:
points = [(0.25, 0.10), (0.30, -0.10), (0.40, 0.30)]
