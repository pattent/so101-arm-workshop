"""Solution: the Block class, in its own file (a module) so other programs can import it."""

import math

COLORS = ['red', 'green', 'blue']


class Block:
    """One colored block on the table."""

    def __init__(self, color, x, y):
        if color not in COLORS:
            raise ValueError(f'Unknown color {color!r}')
        # float() raises ValueError for text like 'glare' and TypeError for None.
        self.color = color
        self.x = float(x)
        self.y = float(y)

    def describe(self):
        return f'a {self.color} block at ({self.x:.2f}, {self.y:.2f})'

    def distance_from_base(self):
        return math.hypot(self.x, self.y)

    def is_in_bin(self, bin_x, bin_y):
        return abs(self.x - bin_x) < 0.05 and abs(self.y - bin_y) < 0.05
