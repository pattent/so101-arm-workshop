"""Solution: Exercise 1."""

robot_name = 'SO-101'
number_of_joints = 5
reach_in_meters = 0.48

print('Hello! My name is', robot_name)
print('I have', number_of_joints, 'joints, plus a gripper.')
print(f'I can reach {reach_in_meters} meters.')

# TODO 1
reach_in_cm = reach_in_meters * 100
print(f'That is {reach_in_cm} centimeters.')

# TODO 2
my_name = 'Alex'
print(f'Nice to meet you, {my_name}!')

# TODO 3
number_of_joints = number_of_joints + 1
print('After the upgrade I have', number_of_joints, 'joints.')

gripper_is_open = True
print(type(number_of_joints), type(reach_in_meters), type(robot_name), type(gripper_is_open))

# TODO 4: dividing with / always gives a float, even when it comes out even.
print(5 / 2, type(5 / 2))      # 2.5 <class 'float'>
print(4 / 2, type(4 / 2))      # 2.0 <class 'float'>
print(5 * 2, type(5 * 2))      # 10 <class 'int'>

# TODO 5: + joins text together, but adds numbers.
print('5' + '5')               # 55
print(5 + 5)                   # 10
# print('5' + 5) fails with: TypeError: can only concatenate str (not "int") to str
print(int('5') + 5)            # 10
