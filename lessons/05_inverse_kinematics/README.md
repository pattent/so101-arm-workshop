# Lesson 5: Inverse kinematics

**Goal:** solve the reverse problem. **Inverse kinematics (IK)** answers: *I want the gripper
HERE; what joint angles get it there?* This is what `arm.move_to(x, y, z)` does for you.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **2-link IK with trigonometry.** Given a target `(x, y)`, use the law of cosines to find the
   elbow angle, then the shoulder angle. Check it by running your forward kinematics from Lesson 4.
2. **Two answers.** Why can the arm reach most points two ways ("elbow up" and "elbow down")?
   Draw both with `matplotlib`.
3. **Follow the mouse.** Animate the 2-link arm so its tip follows your mouse pointer.

## Challenge (on your own)

Use your own IK to compute joint angles, move the SO-101 there with `move_joints`, and compare
where it ends up with `arm.move_to` (which uses MoveIt's IK) for the same point.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 6: Nodes and topics](../06_nodes_and_topics/)
