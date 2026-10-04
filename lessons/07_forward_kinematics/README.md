# Lesson 7: Coordinates and forward kinematics

**Goal:** understand *where* things are. Robots measure everything in coordinates (x, y, z) from
a starting point (a "frame"). **Forward kinematics** answers: *if I know the joint angles,
where is the gripper?*

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **Coordinates on paper.** Draw the robot from above and from the side. Mark x (forward),
   y (left), z (up). Where are the bins and blocks from `table.py`?
2. **A 2-link arm in Python.** Two straight links, like an upper arm and a forearm. Each link
   is the hypotenuse of a right triangle, exactly like the circle in Lesson 2: a link of
   length `L1` tipped up by angle `a1` reaches `L1 * cos(a1)` forward and `L1 * sin(a1)` up.
   That's the elbow. The forearm does the same from the elbow, but its angle adds onto the
   first one (`a1 + a2`), because it rides on the upper arm. Add the two triangles up and you
   have the tip. Work one example on paper (a1 = 30°, a2 = 45°) before coding it, then draw
   the arm with `matplotlib`.
3. **Check against the real thing.** Move the SO-101 with `move_joints` (only `shoulder_lift`
   and `elbow_flex`), predict where the gripper should be, and compare with `arm.where_am_i()`.

## Challenge (on your own)

Plot every point the 2-link arm can reach (try every angle in steps of 5°). That shape is the
arm's **workspace**.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 8: Inverse kinematics](../08_inverse_kinematics/)
