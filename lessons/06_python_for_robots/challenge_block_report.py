"""Challenge: a camera report.

The simulated camera in fake_camera.py takes 3 pictures, and for each one it calls your
callback with a list of blocks, like:
    [{'color': 'red', 'x': 0.25, 'y': -0.05}, {'color': 'blue', 'x': 0.30, 'y': 0.02}, ...]
Some of those readings are garbage. Your job: report which block to pick up first.

Run:  python challenge_block_report.py   (no robot needed)

Steps:
  1. Make a new file blocks.py in this folder, and copy your Block class from Lesson 5
     (exercise 2, with distance_from_base) into it. Import it here:  from blocks import Block
  2. Make Block.__init__ refuse bad data: raise a ValueError if the color isn't red, green
     or blue, or if x or y isn't a number.
     (Hint: float(x) raises a ValueError for 'glare', and a TypeError for None.)
  3. Write a callback on_picture(blocks) that:
       - turns each reading into a Block, skipping bad ones with try / except
         (and printing what was skipped),
       - prints how many good blocks it found,
       - prints the closest block to the robot: that's the one to pick up first.
  4. Hand your callback to the camera, then run it.

Bonus: also report how many blocks of each color there are (a dictionary is handy here).
"""

from fake_camera import FakeCamera

# TODO 1: from blocks import Block


# TODO 3: def on_picture(blocks):


camera = FakeCamera()
# TODO 4: camera.on_new_picture(...)
camera.run(3)
