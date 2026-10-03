# Lesson 8: Robot models and TF

**Goal:** understand how ROS knows the robot's shape. A **URDF** file describes every link
(rigid part) and joint. **TF** keeps track of where every link is, all the time.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **Read the SO-101's URDF.** Run
   `ros2 topic echo --once /follower/robot_description` (or open the `.xacro` files in
   `src/so101-ros-physical-ai/so101_description/urdf/`). Match each `<joint>` to the real arm.
2. **Watch TF live.** `ros2 run tf2_ros tf2_echo base_link gripper_frame_link` while you move
   the arm around in RViz. Turn on the TF display in RViz to see every frame.
3. **Same arm everywhere.** The simulation window builds its 3D arm from this same URDF.
   Why is having one model important?

## Challenge (on your own)

Write a tiny 2-link arm URDF from scratch and view it in RViz with joint sliders
(`joint_state_publisher_gui`).

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 9: MoveIt and obstacles](../09_moveit_and_obstacles/)
