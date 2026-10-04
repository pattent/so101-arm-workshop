"""Solution: Exercise 2."""

# TODO 1: the traceback ends with
#     ValueError: could not convert string to float: 'twenty'
# and the line above it points at the line in this file that caused it.


def read_height(text):
    """Turn text like '0.12' into a number. Return None if it isn't a number."""
    try:
        return float(text)
    except ValueError:
        print(f'  "{text}" is not a number, skipping it')
        return None


for text in ['0.12', '0.30', 'oops', '0.05']:
    print(text, '->', read_height(text))

# TODO 2
height = None
while height is None:
    height = read_height(input('How high should the gripper go (meters)? '))
print('OK, going to', height, 'm')


ALLOWED_COLORS = ['red', 'green', 'blue']


def check_color(color):
    if color not in ALLOWED_COLORS:
        raise ValueError(f'Unknown color {color!r}. Try one of: {ALLOWED_COLORS}')
    return color


print(check_color('red'))

# TODO 3
try:
    check_color('purple')
except ValueError as error:
    print('Caught it:', error)

# TODO 4
for color in ['red', 'purple', 'blue', 'pink', 'green']:
    try:
        print('Good color:', check_color(color))
    except ValueError:
        print('Skipping', color)

# Think about it: skip a bad camera reading (another picture comes in a moment), but stop
# if the motors stop responding (carrying on blind could hurt someone or break the robot).
