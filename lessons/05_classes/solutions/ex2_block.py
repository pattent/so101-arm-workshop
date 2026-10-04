"""Solution: Exercise 2."""

import math


class Block:
    """One colored block on the table."""

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def describe(self):
        return f'a {self.color} block at ({self.x:.2f}, {self.y:.2f})'

    # TODO 1
    def distance_from_base(self):
        return math.hypot(self.x, self.y)

    # TODO 4
    def is_in_bin(self, bin_x, bin_y):
        return abs(self.x - bin_x) < 0.05 and abs(self.y - bin_y) < 0.05


red = Block('red', 0.25, -0.05)
blue = Block('blue', 0.30, 0.02)
print('I see', red.describe())
print('I see', blue.describe())

# TODO 2
print(f'The red block is {red.distance_from_base():.3f} m away')
print(f'The blue block is {blue.distance_from_base():.3f} m away')

# TODO 3
blocks = [
    Block('red', 0.25, -0.05),
    Block('green', 0.20, 0.03),
    Block('blue', 0.30, -0.12),
    Block('red', 0.19, -0.10),
]
for block in blocks:
    print(' -', block.describe())

closest = blocks[0]
for block in blocks:
    if block.distance_from_base() < closest.distance_from_base():
        closest = block
print('The closest is', closest.describe())

# TODO 5
print('In the red bin?', Block('red', 0.13, 0.20).is_in_bin(0.12, 0.22))   # True
print('In the red bin?', Block('red', 0.25, 0.20).is_in_bin(0.12, 0.22))   # False
