"""Solution: Challenge."""

import math

from workshop_arm import Arm

HEIGHT = 0.15


def circle(arm, center_x, center_y, radius, points):
    for i in range(points + 1):              # +1 to come back to the start
        angle = 2 * math.pi * i / points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        arm.move_to(x, y, HEIGHT)


arm = Arm()
arm.go_to('rest')

# TODO 1
corners = [(0.20, -0.05), (0.30, -0.05), (0.30, 0.05), (0.20, 0.05)]
for x, y in corners:
    arm.move_to(x, y, HEIGHT)
first_x, first_y = corners[0]
arm.move_to(first_x, first_y, HEIGHT)

# TODO 3
circle(arm, 0.25, 0.0, 0.05, 12)

arm.go_to('rest')
arm.shutdown()
