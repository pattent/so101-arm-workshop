# Lesson 4: Coordinates and forward kinematics

**Goal:** understand *where* things are. Robots measure everything in coordinates (x, y, z) from
a starting point (a "frame"). **Forward kinematics** answers: *if I know the joint angles,
where is the gripper?*

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **Coordinates on paper.** Draw the robot from above and from the side. Mark x (forward),
   y (left), z (up). Where are the bins and blocks from `table.py`?
2. **A 2-link arm in Python.** An arm with two links of length `L1` and `L2` and joint angles
   `a1`, `a2`: the elbow is at `(L1·cos a1, L1·sin a1)`, and the tip is the elbow plus
   `(L2·cos(a1+a2), L2·sin(a1+a2))`. Compute it, then draw the arm with `matplotlib`.
3. **Check against the real thing.** Move the SO-101 with `move_joints` (only `shoulder_lift`
   and `elbow_flex`), predict where the gripper should be, and compare with `arm.where_am_i()`.

## Challenge (on your own)

Plot every point the 2-link arm can reach (try every angle in steps of 5°). That shape is the
arm's **workspace**.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 5: Inverse kinematics](../05_inverse_kinematics/)
