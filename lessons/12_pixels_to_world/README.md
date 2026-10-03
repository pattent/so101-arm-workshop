# Lesson 12: Pixels to the real world → 🥇 Gold

**Goal:** turn "the red block is at pixel (412, 230)" into "the red block is at x = 0.27 m,
y = −0.05 m", then let the robot sort blocks it finds by itself. This is the **Gold** tier.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=3`

## Exercises (together)

1. **The pinhole camera model.** Why does `pixel_to_table()` need the camera's height and
   focal length? Work through one block by hand.
2. **How accurate is it?** Compare detected positions with where the blocks really are.
3. **From function to node.** Read
   [`block_detector.py`](../../src/workshop_arm/workshop_arm/block_detector.py): it runs the
   vision code on every picture and publishes `/detected_blocks`.
4. **Your own detector.** Restart with `detector:=false` and run your own detector node instead.

## Challenge (on your own): 🥇 Gold

Write your own version of
[`vision_demo.py`](../../src/workshop_arm/workshop_arm/vision_demo.py): look → pick → place →
look again, until the table is clean. Stretch goals: sort the closest block first; recover from
a missed grab.

**Later, with a real webcam:** calibrate with 4 marked corners on a sheet of paper (a
"homography") instead of the pinhole math.

> Starter files and solutions for this lesson are still being written.

**Then:** the [Beyond](../README.md#beyond-her-call) section: real hardware, physics, AI.
