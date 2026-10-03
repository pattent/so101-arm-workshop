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
