"""Exercise 1: variables and print.

Run:  python ex1_hello_robot.py
"""

# A variable is a name for a value. Here are some facts about our robot.
robot_name = 'SO-101'  # this is called a string when it is text 
number_of_joints = 5  # this is called an integer, a whole number with no decimal
reach_in_meters = 0.48  # this is called a float, a decimal number

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

# Every value has a TYPE, which decides what you can do with it. The four you'll use most:
#   int     a whole number               5
#   float   a number with a decimal      0.48
#   str     text (a "string")            'SO-101'
#   bool    True or False                True
gripper_is_open = True  # this type of variable is called a bool, bools are either True or False
print(type(number_of_joints), type(reach_in_meters), type(robot_name), type(gripper_is_open))

# TODO 4: Guess the answer AND its type, then print both to check:
#             5 / 2          4 / 2          5 * 2
#         (Hint: print(4 / 2, type(4 / 2)))

# TODO 5: Print '5' + '5', then 5 + 5. Why are the answers different?
#         Then try print('5' + 5). It stops with an error: read its LAST line.
#         int('5') turns the text '5' into the number 5. Use it to fix that line.
