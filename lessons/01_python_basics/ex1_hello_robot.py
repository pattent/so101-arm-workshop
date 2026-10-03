"""Exercise 1: variables and print.

Run:  python ex1_hello_robot.py
"""

# A variable is a name for a value. Here are some facts about our robot.
robot_name = 'SO-101'
number_of_joints = 5
reach_in_meters = 0.48

print('Hello! My name is', robot_name)
print('I have', number_of_joints, 'joints, plus a gripper.')

# An "f-string" (notice the f before the quote) puts values inside text with {}.
print(f'I can reach {reach_in_meters} meters.')

# TODO 1: Make a variable called reach_in_cm that holds the reach in centimeters.
#         (Hint: there are 100 centimeters in a meter. Use * to multiply.)
reach_in_cm = 0

print(f'That is {reach_in_cm} centimeters.')

# TODO 2: Make a variable called my_name with your name in it, and print
#         a message like "Nice to meet you, Alex!" using an f-string.

# TODO 3: The robot is getting a gripper upgrade and will have 6 joints.
#         Change number_of_joints (without retyping 5 or 6 by hand!) by adding 1,
#         then print it again.
