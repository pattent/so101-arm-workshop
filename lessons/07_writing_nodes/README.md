# Lesson 7: Writing ROS 2 nodes

**Goal:** write your own nodes in Python: **publishers**, **subscribers**, and a first look at
**services** and **actions**. Then open up `arm.py` again: now the ROS parts make sense.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

## Exercises (together)

1. **A subscriber.** Listen to `/follower/joint_states` and print each joint angle in degrees.
2. **A publisher.** Publish a message on your own topic, and watch it with `ros2 topic echo`.
3. **Your own package.** Create a ROS package in `src/` with `ros2 pkg create`, add your node,
   `colcon build`, and run it with `ros2 run`.
4. **Back to `arm.py`.** Find the `ActionClient`s. What are they talking to?

## Challenge (on your own)

A "safety monitor" node: watch where the gripper is (with TF, or `Arm.where_am_i()`) and print a
warning whenever it goes below 3 cm above the table.

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 8: Robot models and TF](../08_robot_models_and_tf/)
