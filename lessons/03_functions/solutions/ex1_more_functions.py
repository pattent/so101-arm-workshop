"""Solution: Exercise 1."""

import math


def distance_from_base(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def can_reach(x, y, max_reach=0.48):
    return distance_from_base(x, y) < max_reach


print(can_reach(0.40, 0.20))
print(can_reach(0.40, 0.20, max_reach=0.40))

# TODO 1: (0.40, 0.15) is about 0.427 m away: reachable either way.
print(can_reach(0.40, 0.15))                    # True
print(can_reach(0.40, 0.15, max_reach=0.44))    # True


def split_angle(degrees):
    """How many whole turns, and how many degrees left over?"""
    turns = degrees // 360
    left_over = degrees % 360
    return turns, left_over


turns, left_over = split_angle(800)
print(f'800 degrees is {turns} full turns and {left_over} degrees')


# TODO 2
def point_on_circle(center_x, center_y, radius, degrees):
    angle = math.radians(degrees)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    return x, y


x, y = point_on_circle(0.25, 0.0, 0.05, 90)
print(f'({x:.3f}, {y:.3f})')                    # (0.250, 0.050)


# TODO 3
def describe(x, y):
    how_far = distance_from_base(x, y)
    return f'({x}, {y}) is {how_far:.3f} m away, and I can reach it: {can_reach(x, y)}'


points = [(0.25, 0.10), (0.30, -0.10), (0.40, 0.30)]
for x, y in points:
    print(describe(x, y))
