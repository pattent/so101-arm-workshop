"""Exercise 2: write your own functions (no robot needed).

A function is a named set of steps. You write it once with `def`, then call it as many
times as you like. Inputs go in the parentheses; `return` sends an answer back.

Run:  python ex2_my_first_functions.py
"""

import math


# A function with an input, that does something (prints) but gives nothing back.
def say_hello(name):
    print(f'Hello, {name}! I am the SO-101.')


say_hello('Alex')
say_hello('Sam')        # same steps, different input


# A function that gives back an answer with `return`.
def to_radians(degrees):
    return degrees * math.pi / 180


answer = to_radians(90)     # the returned value gets saved in `answer`
print('90 degrees is', answer, 'radians')
print('45 degrees is', to_radians(45), 'radians')

# TODO 1: Write a function to_degrees(radians) that returns the angle in degrees.
#         Test it: to_degrees(1.2) should be about 68.75.

# TODO 2: Write a function distance(x, y) that returns how far the point (x, y) is from
#         the robot's base (remember Lesson 1, exercise 3?).
#         Test it: distance(0.25, 0.10) should be about 0.269.

# TODO 3: Use your distance function in a loop: print how far each of these points is.
points = [(0.25, 0.10), (0.30, -0.10), (0.40, 0.30)]

# TODO 4: What's the difference between print and return? Try this and explain what happens:
#             result = say_hello('Robot')
#             print('say_hello gave back:', result)
