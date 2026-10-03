"""Exercise 2: math with angles.

People usually measure angles in degrees (a full circle is 360).
Robots (and ROS) use radians: a full circle is 2 * pi, about 6.28.

Run:  python ex2_degrees_and_radians.py
"""

import math

print('pi is', math.pi)

# To turn degrees into radians: multiply by pi, divide by 180.
quarter_turn_degrees = 90
quarter_turn_radians = quarter_turn_degrees * math.pi / 180
print(f'{quarter_turn_degrees} degrees is {quarter_turn_radians} radians')

# TODO 1: Convert 45 degrees to radians the same way, and print it.

# TODO 2: Python can do it for you: math.radians(degrees).
#         Use it to convert 45 degrees, and check you get the same answer.

# TODO 3: Go the other way. The robot reports its elbow is at 1.2 radians.
#         How many degrees is that? Use math.degrees(), then print it.

# TODO 4: Printing lots of decimals is messy. Inside an f-string, {value:.2f}
#         shows just 2 decimal places. Print the elbow angle that way.
