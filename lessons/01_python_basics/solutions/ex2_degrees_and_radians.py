"""Solution: Exercise 2."""

import math

print('pi is', math.pi)

quarter_turn_degrees = 90
quarter_turn_radians = quarter_turn_degrees * math.pi / 180
print(f'{quarter_turn_degrees} degrees is {quarter_turn_radians} radians')

# TODO 1
eighth_turn_radians = 45 * math.pi / 180
print('45 degrees is', eighth_turn_radians, 'radians')

# TODO 2
print('math.radians(45) gives', math.radians(45))

# TODO 3
elbow_radians = 1.2
elbow_degrees = math.degrees(elbow_radians)
print('The elbow is at', elbow_degrees, 'degrees')

# TODO 4
print(f'The elbow is at {elbow_degrees:.2f} degrees')
