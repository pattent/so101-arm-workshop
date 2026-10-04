"""Solution: Exercise 3."""

import math

points = [(0.25, 0.10), (0.30, -0.10), (0.40, 0.30), (0.15, 0.05), (0.50, -0.20)]


def average_x(points):
    total = 0
    for x, y in points:
        total = total + x
    return total / len(points)


print('The average x is', average_x(points))


# TODO 1
def distance_from_base(x, y):
    return math.sqrt(x ** 2 + y ** 2)


# TODO 2
def closest_point(points):
    closest = points[0]
    for x, y in points:
        closest_x, closest_y = closest
        if distance_from_base(x, y) < distance_from_base(closest_x, closest_y):
            closest = (x, y)
    return closest


print('The closest point is', closest_point(points))    # (0.15, 0.05)


# TODO 3
def reachable(points, max_reach):
    good = []
    for x, y in points:
        if distance_from_base(x, y) < max_reach:
            good.append((x, y))
    return good


print('Reachable:', reachable(points, 0.44))             # 3 points
