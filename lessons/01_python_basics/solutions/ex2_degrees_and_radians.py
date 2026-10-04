"""Solution: Exercise 2."""

import math

print('pi is', math.pi)

quarter_turn_degrees = 90
quarter_turn_radians = quarter_turn_degrees * math.pi / 180
print(f'{quarter_turn_degrees} degrees is {quarter_turn_radians} radians')

# TODO 1
eighth_turn_radians = 45 * math.pi / 180
print('45 degrees is', eighth_turn_radians, 'radians')

print('90 degrees is', math.radians(90), 'radians')

# TODO 2
print('math.radians(45) gives', math.radians(45))

# TODO 3: the second input is how many decimals to keep.
print(round(math.pi, 2))     # 3.14
print(round(math.pi, 4))     # 3.1416


def to_radians(degrees):
    return degrees * math.pi / 180


print('Mine says 90 degrees is', to_radians(90), 'radians')
answer = to_radians(180)
print('180 degrees is', answer, 'radians')


# TODO 4
def to_degrees(radians):
    return radians * 180 / math.pi


elbow_degrees = to_degrees(1.2)
print('The elbow is at', round(elbow_degrees, 1), 'degrees')    # 68.8
