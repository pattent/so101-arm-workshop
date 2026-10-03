"""The workcell layout: where the bins are, where blocks can appear, and where the camera is.

All positions are in meters, measured from the robot's base (x forward, y left, z up).
"""

# Bins are bolted down, so their positions are always known.
BINS = {
    'red': (0.12, 0.22),
    'green': (0.24, 0.20),
    'blue': (0.34, 0.12),
}

# Stage 2: blocks always start at these known spots (name: (x, y, color)).
KNOWN_BLOCKS = {
    'block_0': (0.22, -0.10, 'red'),
    'block_1': (0.28, 0.02, 'blue'),
    'block_2': (0.30, -0.12, 'green'),
}

# Stage 3: blocks get scattered at random somewhere inside this rectangle.
BLOCK_AREA_X = (0.18, 0.32)
BLOCK_AREA_Y = (-0.16, 0.04)

# An overhead camera looking straight down at the table.
CAMERA_X = 0.22
CAMERA_Y = 0.04
CAMERA_HEIGHT = 0.60
CAMERA_WIDTH = 640    # pixels
CAMERA_HEIGHT_PX = 480
CAMERA_FOCAL = 600.0  # focal length, in pixels
