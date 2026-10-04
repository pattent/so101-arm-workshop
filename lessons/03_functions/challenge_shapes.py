"""Challenge: a shape-drawing robot.

In Lesson 2 you drew a square and a circle with loops, and to draw a second circle you had to
copy the whole loop. Now turn each shape into a function, so drawing another is one line.

Run (with the stage 1 simulation running):  python challenge_shapes.py

Steps:
  1. Write square(arm, center_x, center_y, size): trace a square of that size (in meters)
     around the center, and come back to the first corner.
  2. Write circle(arm, center_x, center_y, radius, points): trace a circle with that many
     points. (Copy your loop from Lesson 2 and swap the numbers for the inputs, or use your
     point_on_circle from exercise 1.)
  3. Use them to draw a picture: e.g. three circles in a row, or a square with a circle
     inside it. Keep every shape within reach: centers around x = 0.20 to 0.30, y = -0.10
     to 0.10, and sizes up to about 0.10 m.

Bonus: write polygon(arm, center_x, center_y, radius, sides). A triangle is 3 sides, a square
is 4... and with 24 sides it looks like a circle! Can circle just call polygon?
"""

import math

from workshop_arm import Arm

HEIGHT = 0.15


# TODO 1: def square(arm, center_x, center_y, size):


# TODO 2: def circle(arm, center_x, center_y, radius, points):


arm = Arm()
arm.go_to('rest')

# TODO 3: draw your picture here.

arm.go_to('rest')
arm.shutdown()
