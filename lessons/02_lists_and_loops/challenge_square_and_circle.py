"""Challenge: draw a square and a circle in the air.

Run (with the stage 1 simulation running):  python challenge_square_and_circle.py

Tips:
- Keep the height (z) the same for every point, e.g. 0.15 m.
- A square needs 4 corners, plus going back to the first one to close it.
- More points make a smoother circle (try 12, then 24).

How do you find points on a circle? With the right-triangle trig you know (SOH-CAH-TOA).
Pick a point on the circle at some angle. Draw a line from the center to it (that's the
radius r, the hypotenuse), then straight down to the x axis. That makes a right triangle:

                  * point on the circle
                 /|
              r / |  opposite side = r * sin(angle)     (SOH: sin = opposite / hypotenuse)
               /  |
              /   |
     center  *----+
             adjacent side = r * cos(angle)              (CAH: cos = adjacent / hypotenuse)

So the point is   x = center_x + r * math.cos(angle)
                  y = center_y + r * math.sin(angle)
Walk the angle all the way around (0, 30, 60, ... 360 degrees) and you trace the circle.
(Past 90 degrees, cos and sin turn negative, which is exactly what moves the point left of
or below the center. Python handles that for you.)
One catch: math.cos and math.sin want the angle in RADIANS, so use math.radians() first.
"""

import math

from workshop_arm import Arm

HEIGHT = 0.15

arm = Arm()
arm.go_to('rest')

# TODO 1: Make a list of the 4 corners of a 10 cm square centered at x=0.25, y=0.
#         Visit each corner with a for loop, then go back to the first corner.

# TODO 2: Draw a circle with radius 0.05 m around (0.25, 0), with 12 points: one every
#         30 degrees. Use a for loop: range(0, 361, 30) gives 0, 30, 60, ... 360 (ending
#         at 360 brings you back to the start). For each angle, work out x and y with the
#         formulas above, and move there.

# TODO 3: Make the circle smoother with 24 points. Then draw a second, bigger circle.
#         (In Lesson 3 you'll turn this into a function, so you don't have to copy the loop.)

arm.go_to('rest')
arm.shutdown()
