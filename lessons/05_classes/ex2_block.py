"""Exercise 2: a class for blocks.

A class for real robot work: a Block, which knows its color and where it is, and can
answer questions about itself. You'll use it again in Lesson 6.

Run:  python ex2_block.py   (no robot needed)
"""

import math


class Block:
    """One colored block on the table."""

    # __init__ runs once, when you make a new Block. It saves the facts on `self`
    # (this particular block), so the block's other functions can use them later.
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    # A function inside a class (a "method"). It always gets `self` first.
    def describe(self):
        return f'a {self.color} block at ({self.x:.2f}, {self.y:.2f})'

    # TODO 1: Add a method distance_from_base(self) that returns how far the block is
    #         from the robot's base at (0, 0). math.hypot(x, y) does Pythagoras for you.

    # TODO 4: Add a method is_in_bin(self, bin_x, bin_y) that returns True if the block
    #         is inside a bin centered at (bin_x, bin_y). Bins are 0.10 m wide, so the
    #         block must be less than 0.05 m from the center in x AND in y.
    #         (Hint: abs(-0.03) is 0.03. It removes the minus sign.)


# Make two blocks. Each one is an "object": its own copy of the class, with its own facts.
red = Block('red', 0.25, -0.05)
blue = Block('blue', 0.30, 0.02)
print('I see', red.describe())
print('I see', blue.describe())

# TODO 2: Print how far each block is from the base, using your new method.
#         (Call it like describe: red.distance_from_base())

# TODO 3: Make a list called blocks with at least four Block objects (any colors, any
#         spots on the table). Loop over it and print each one's description.
#         Then find the CLOSEST block and print it.
#         (Hint: keep a variable `closest`, start it at the first block, and replace it
#         whenever you find a block that's closer.)

# TODO 5: Test is_in_bin. The red bin is at (0.12, 0.22).
#         Block('red', 0.13, 0.20) should be in it. Block('red', 0.25, 0.20) should not.
