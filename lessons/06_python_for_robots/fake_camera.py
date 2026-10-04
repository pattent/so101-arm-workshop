"""A simulated overhead camera, for practicing without a robot. (You don't need to change this.)

Every "picture" it takes, it calls your callback with a list of the blocks it found:

    [{'color': 'red', 'x': 0.25, 'y': -0.05}, {'color': 'blue', 'x': 0.30, 'y': 0.02}, ...]

Like a real camera, it isn't perfect: now and then it reports a color that doesn't exist,
or a position that isn't a number.
"""

import random
import time

GOOD_COLORS = ['red', 'green', 'blue']
GLITCHES = [
    {'color': 'purple', 'x': 0.22, 'y': 0.01},     # a shadow mistaken for a block
    {'color': 'red', 'x': 'glare', 'y': -0.08},    # a reflection hid the position
    {'color': 'blue', 'x': 0.27, 'y': None},       # lost track halfway through
]


class FakeCamera:

    def __init__(self, seed=None):
        self.callbacks = []
        self.random = random.Random(seed)

    def on_new_picture(self, callback):
        """Call `callback(blocks)` every time a new picture is taken."""
        self.callbacks.append(callback)

    def run(self, pictures=3):
        """Take some pictures, and hand each one's blocks to every callback."""
        for number in range(1, pictures + 1):
            print(f'\n--- picture {number} ---')
            blocks = [{'color': self.random.choice(GOOD_COLORS),
                       'x': round(self.random.uniform(0.18, 0.32), 3),
                       'y': round(self.random.uniform(-0.16, 0.04), 3)}
                      for _ in range(self.random.randint(2, 5))]
            blocks.insert(self.random.randint(0, len(blocks)), self.random.choice(GLITCHES))
            for callback in self.callbacks:
                callback(blocks)
            time.sleep(0.5)
