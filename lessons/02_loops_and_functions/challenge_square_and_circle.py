"""Challenge: draw a square and a circle in the air.

Run (with the stage 1 simulation running):  python challenge_square_and_circle.py

Tips:
- Keep the height (z) the same for every point, e.g. 0.15 m.
- A square needs 4 corners, plus going back to the first one to close it.
- A circle around (center_x, center_y) with radius r:
      x = center_x + r * math.cos(angle)
      y = center_y + r * math.sin(angle)
  where angle goes from 0 to 2 * math.pi (in radians!).
- More points make a smoother circle (try 12, then 24).
"""

import math

from workshop_arm import Arm

HEIGHT = 0.15

arm = Arm()
arm.go_to('rest')

# TODO 1: Make a list of the 4 corners of a 10 cm square centered at x=0.25, y=0.
#         Visit each corner with a for loop, then go back to the first corner.

# TODO 2: Write a function circle(arm, center_x, center_y, radius, points) that moves
#         the gripper around a circle.

# TODO 3: Draw a circle with radius 0.05 m around (0.25, 0).

arm.go_to('rest')
arm.shutdown()
