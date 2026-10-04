# Lesson 16: Pixels to the real world → 🥇 Gold

**Goal:** turn "the red block is at pixel (412, 230)" into "the red block is at x = 0.27 m,
y = −0.05 m", then let the robot sort blocks it finds by itself. This is the **Gold** tier.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=3`

## Exercises (together)

1. **The pinhole camera model: similar triangles.** A camera is like a box with a tiny hole:
   light from a block goes through the hole and lands on the sensor behind it. The block,
   the hole and the picture make two similar triangles (geometry!), so
   `distance on the table / camera height = distance in the picture / focal length`.
   That's all `pixel_to_table()` does. Draw it, then work through one block by hand.
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

**Later, with a real webcam:** calibrate with 4 marked corners on a sheet of paper instead of
the pinhole math. (The math behind that, a "homography", is college level; OpenCV does it in
one function call, so you can use it without deriving it.)

> Starter files and solutions for this lesson are still being written.

**Then:** the [Beyond](../README.md#beyond-your-call) section: real hardware, physics, AI.
