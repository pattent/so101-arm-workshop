"""Solution: Challenge (including the bonus)."""

import math

from workshop_arm import Arm

HEIGHT = 0.15


# TODO 1
def square(arm, center_x, center_y, size):
    half = size / 2
    corners = [(center_x - half, center_y - half), (center_x + half, center_y - half),
               (center_x + half, center_y + half), (center_x - half, center_y + half)]
    for x, y in corners:
        arm.move_to(x, y, HEIGHT)
    first_x, first_y = corners[0]
    arm.move_to(first_x, first_y, HEIGHT)


# Bonus
def polygon(arm, center_x, center_y, radius, sides):
    for i in range(sides + 1):              # +1 to come back to the start
        angle = math.radians(360 * i / sides)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        arm.move_to(x, y, HEIGHT)


# TODO 2: a circle is a polygon with lots of sides.
def circle(arm, center_x, center_y, radius, points):
    polygon(arm, center_x, center_y, radius, points)


arm = Arm()
arm.go_to('rest')

# TODO 3: a square with a circle inside it, then a triangle.
square(arm, 0.25, 0.0, 0.10)
circle(arm, 0.25, 0.0, 0.04, 16)
polygon(arm, 0.25, 0.0, 0.06, 3)

arm.go_to('rest')
arm.shutdown()
