"""Exercise 2: math with angles, and your first function.

People usually measure angles in degrees (a full circle is 360).
Robots (and ROS) measure them in radians instead. What's a radian?

    Take a circle, and a piece of string as long as its radius. Lay the string along the
    edge of the circle. The angle it covers, from the center, is 1 radian (about 57 degrees).

A circle's edge (its circumference) is 2 * pi * radius long, so 2 * pi pieces of string fit
around it: a full circle is 2 * pi radians, about 6.28. Half a circle (180 degrees) is pi.
Robots like radians because the math for wheels and joints comes out simpler with them.
You'll mostly think in degrees and let Python convert.

Run:  python ex2_degrees_and_radians.py
"""

import math

print('pi is', math.pi)

# To turn degrees into radians: multiply by pi, divide by 180.
quarter_turn_degrees = 90
quarter_turn_radians = quarter_turn_degrees * math.pi / 180
print(f'{quarter_turn_degrees} degrees is {quarter_turn_radians} radians')

# TODO 1: Convert 45 degrees to radians the same way, and print it.


# Part 2: CALLING a function. Python has one that does the conversion for you.
# You call it by its name, with the input in parentheses, and it gives back the answer.
print('90 degrees is', math.radians(90), 'radians')

# TODO 2: Use math.radians to convert 45 degrees, and check you get the same answer as TODO 1.

# TODO 3: round(number, decimals) gives back a number with fewer decimals. Its inputs go in
#         a fixed order: the number first, then how many decimals to keep.
#         Print round(math.pi, 2), then round(math.pi, 4). What does the second input do?


# Part 3: WRITING a function. Here's how math.radians could be written.
#   def      means "I'm making a function"
#   degrees  is its input: a variable that holds whatever you call it with
#   return   gives the answer back to whoever called it
# The indented line is the function's body: the steps it does each time it's called.
def to_radians(degrees):
    return degrees * math.pi / 180


print('Mine says 90 degrees is', to_radians(90), 'radians')
answer = to_radians(180)                 # save the answer in a variable
print('180 degrees is', answer, 'radians')

# TODO 4: Write your own function to_degrees(radians) that goes the other way:
#         multiply by 180, divide by pi. Copy the pattern of to_radians above.
#         The robot says its elbow is at 1.2 radians. Use your function to print it in
#         degrees, rounded to 1 decimal. (It should be about 68.8.)
