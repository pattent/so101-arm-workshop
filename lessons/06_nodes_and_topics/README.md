# Lesson 6: Nodes and topics

**Goal:** see how ROS 2 works inside. A robot is many small programs (**nodes**) that talk by
sending **messages** on named channels (**topics**).

## Exercises (together)

1. **Turtlesim.** In three terminals: `ros2 run turtlesim turtlesim_node`,
   `ros2 run turtlesim turtle_teleop_key`, and then explore with `ros2 node list`,
   `ros2 topic list`, `ros2 topic echo /turtle1/pose` and `rqt_graph`.
2. **Talk to the turtle yourself.** Send a message from the command line with
   `ros2 topic pub` to make it drive in a circle.
3. **The arm's nervous system.** Start `ros2 launch workshop_arm workshop.launch.py stage:=1`
   and look around: `ros2 node list`, `ros2 topic echo /follower/joint_states`, `rqt_graph`.
   Which node publishes the joint angles? Which nodes listen?

## Challenge (on your own)

Using only the command line, find out which joint moves the most while
`ros2 run workshop_arm demo` runs (stage 2).

> Starter files and solutions for this lesson are still being written.

**Next:** [Lesson 7: Writing ROS 2 nodes](../07_writing_nodes/)
