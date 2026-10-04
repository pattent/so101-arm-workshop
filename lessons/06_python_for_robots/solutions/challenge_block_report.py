"""Solution: Challenge. (blocks.py, next to this file, holds the Block class.)"""

import os
import sys

# fake_camera.py lives one folder up, next to the starter files. This line lets Python find
# it when you run the solution from here. (Your own version doesn't need it.)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from blocks import Block
from fake_camera import FakeCamera


def on_picture(readings):
    blocks = []
    for reading in readings:
        try:
            blocks.append(Block(reading['color'], reading['x'], reading['y']))
        except (ValueError, TypeError):
            print('  Skipping a bad reading:', reading)

    print(f'Found {len(blocks)} good blocks.')
    if not blocks:
        return

    closest = blocks[0]
    for block in blocks:
        if block.distance_from_base() < closest.distance_from_base():
            closest = block
    print('Pick up first:', closest.describe())

    # Bonus
    counts = {}
    for block in blocks:
        counts[block.color] = counts.get(block.color, 0) + 1
    print('Colors:', counts)


camera = FakeCamera()
camera.on_new_picture(on_picture)
camera.run(3)
