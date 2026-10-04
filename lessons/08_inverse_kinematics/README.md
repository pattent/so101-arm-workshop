# Lesson 8: Inverse kinematics

**Goal:** solve the reverse problem. **Inverse kinematics (IK)** answers: *I want the gripper
HERE; what joint angles get it there?* This is what `arm.move_to(x, y, z)` does for you.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **Guess and check.** Before any new math: loop over every pair of angles (in steps of 1°),
   run your forward kinematics from Lesson 7 on each, and keep the pair whose tip lands
   closest to the target. It works, but it's slow. Why?
2. **The exact answer, with the law of cosines.** New math, introduced here: it's the
   Pythagorean theorem for triangles *without* a right angle, `c² = a² + b² − 2ab·cos(C)`.
   Check it on a right triangle first (cos 90° = 0, so it turns back into Pythagoras). The
   upper arm, the forearm and the line from shoulder to target make a triangle with three
   known sides, so it gives the elbow angle. Check your answer against the guess-and-check
   one.
3. **Two answers.** Why can the arm reach most points two ways ("elbow up" and "elbow down")?
   Draw both with `matplotlib`.
4. **Follow the mouse.** Animate the 2-link arm so its tip follows your mouse pointer.

## Challenge (on your own)

Use your own IK to compute joint angles, move the SO-101 there with `move_joints`, and compare
where it ends up with `arm.move_to` (which uses MoveIt's IK) for the same point.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 9: Nodes and topics](../09_nodes_and_topics/)
