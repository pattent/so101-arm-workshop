"""Find colored blocks in a camera image and work out where they are on the table.

These are plain Python + OpenCV functions (no ROS), so you can test them on any
image, including one from your laptop's webcam.
"""

import cv2
import numpy as np

from workshop_arm.arm import BLOCK_SIZE
from workshop_arm.table import CAMERA_HEIGHT, CAMERA_X, CAMERA_Y

# Color ranges in HSV (Hue 0-179, Saturation 0-255, Value 0-255).
# Red sits at both ends of the hue circle, so it needs two ranges.
COLOR_RANGES = {
    'red': [((0, 120, 70), (10, 255, 255)), ((170, 120, 70), (179, 255, 255))],
    'green': [((40, 120, 70), (85, 255, 255))],
    'blue': [((100, 120, 70), (130, 255, 255))],
}

# A block seen from the camera covers roughly this many pixels. Anything much
# smaller is noise, anything much bigger is something else (like a bin).
MIN_AREA = 150
MAX_AREA = 1200


def find_blocks(image_bgr):
    """Return a list of blocks found in the image: [{'color', 'u', 'v', 'area'}, ...].

    (u, v) is the block's center in pixels: u goes right, v goes down.
    """
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    blocks = []
    for color, ranges in COLOR_RANGES.items():
        # 1. Make a black-and-white "mask": white where the pixel is this color.
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for low, high in ranges:
            mask |= cv2.inRange(hsv, np.array(low), np.array(high))

        # 2. Find the outline of each white blob.
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 3. Keep blobs that are block-sized, and find their centers.
        for contour in contours:
            area = cv2.contourArea(contour)
            if not MIN_AREA < area < MAX_AREA:
                continue
            m = cv2.moments(contour)
            blocks.append({
                'color': color,
                'u': m['m10'] / m['m00'],
                'v': m['m01'] / m['m00'],
                'area': area,
            })
    return blocks


def pixel_to_table(u, v, focal, center_u, center_v, height_above_table=BLOCK_SIZE):
    """Turn a pixel (u, v) into table coordinates (x, y) in meters.

    This is the pinhole camera model run backwards. The camera hangs straight down
    at (CAMERA_X, CAMERA_Y), CAMERA_HEIGHT above the table, and we're looking at the
    top of a block, which is `height_above_table` above the table.
    """
    distance = CAMERA_HEIGHT - height_above_table
    x = CAMERA_X - (v - center_v) * distance / focal
    y = CAMERA_Y - (u - center_u) * distance / focal
    return x, y


def draw_blocks(image_bgr, blocks):
    """Draw a labeled box around each found block (for checking your work)."""
    out = image_bgr.copy()
    for b in blocks:
        u, v = round(b['u']), round(b['v'])
        half = round((b['area'] ** 0.5) / 2) + 4
        cv2.rectangle(out, (u - half, v - half), (u + half, v + half), (255, 255, 255), 1)
        label = b['color']
        if 'x' in b:
            label += f" {b['x']:.2f},{b['y']:.2f}"
        cv2.putText(out, label, (u - half, v - half - 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (40, 40, 40), 1, cv2.LINE_AA)
    return out
