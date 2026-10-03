# Lesson 11: Computer vision with OpenCV

**Goal:** make the robot see. Find colored blocks in a camera picture with **OpenCV**.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=3`
(random blocks and a live overhead camera). The simulation window shows what the camera sees.

## Exercises (together)

1. **What does the robot see?** Watch the camera view, and open the raw picture with
   `ros2 run rqt_image_view rqt_image_view /camera/image_raw`. Move the arm: it blocks the view!
2. **Color masks.** Convert the picture to HSV and keep only the "red" pixels with `cv2.inRange`.
   Show the black-and-white mask. Tune the color ranges.
3. **Find the blobs.** Use `cv2.findContours` on the mask, keep the block-sized ones (why do the
   bins not count?), and mark their centers.
4. **Compare with ours.** Read
   [`vision.py`](../../src/workshop_arm/workshop_arm/vision.py): it does exactly these steps.

## Challenge (on your own)

Add yellow blocks: a new color range in `vision.py`, and a yellow bin in `table.py`.
Bonus: run `find_blocks()` on a photo of colored paper squares from your own webcam.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 12: Pixels to the real world](../12_pixels_to_world/)
