"""Solution: Challenge."""

import math

from workshop_arm import Arm

HEIGHT = 0.15

arm = Arm()
arm.go_to('rest')

# TODO 1
corners = [(0.20, -0.05), (0.30, -0.05), (0.30, 0.05), (0.20, 0.05)]
for x, y in corners:
    arm.move_to(x, y, HEIGHT)
first_x, first_y = corners[0]
arm.move_to(first_x, first_y, HEIGHT)

# TODO 2
for degrees in range(0, 361, 30):       # 0, 30, ... 360: the last one is back at the start
    angle = math.radians(degrees)
    x = 0.25 + 0.05 * math.cos(angle)
    y = 0.0 + 0.05 * math.sin(angle)
    arm.move_to(x, y, HEIGHT)

# TODO 3: 24 points (every 15 degrees), then a bigger circle (radius 0.08).
for degrees in range(0, 361, 15):
    angle = math.radians(degrees)
    arm.move_to(0.25 + 0.05 * math.cos(angle), 0.05 * math.sin(angle), HEIGHT)
for degrees in range(0, 361, 15):
    angle = math.radians(degrees)
    arm.move_to(0.25 + 0.08 * math.cos(angle), 0.08 * math.sin(angle), HEIGHT)

arm.go_to('rest')
arm.shutdown()
