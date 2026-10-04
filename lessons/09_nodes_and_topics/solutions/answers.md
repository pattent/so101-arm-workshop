# Lesson 9: answers

Your node names may have extra numbers on the end (like `/move_group_private_93859256282096`):
ROS adds those to keep names unique. That's normal.

## 1. Meet the turtle

- `/teleop_turtle` (from `turtle_teleop_key`) **publishes** on `/turtle1/cmd_vel`, and
  `/turtlesim` **subscribes** to it. `ros2 topic info /turtle1/cmd_vel` shows 1 publisher and
  1 subscriber; `rqt_graph` draws an arrow from one to the other through the topic.
- `/turtle1/pose` changes while the turtle moves (x, y, theta and the speeds). When it stops,
  the messages keep coming with the same numbers: turtlesim publishes the pose all the time,
  not only when something changes.

## 2. Talk to the turtle yourself

- `linear.x` is the forward speed and `angular.z` the turning speed. A negative `linear.x`
  drives backwards; a negative `angular.z` turns the other way (clockwise).
- A bigger circle: faster forward, or slower turning (`linear.x: 3.0, angular.z: 1.0`).
  A smaller one: the opposite. The circle's radius is `linear.x / angular.z`.
- After spawning `turtle2`, there's a new set of topics: `/turtle2/cmd_vel`, `/turtle2/pose`
  and `/turtle2/color_sensor`. Each turtle gets its own.

## 3. The arm's nervous system

- `/follower/joint_state_broadcaster` publishes `/follower/joint_states`, about 100 times a
  second (`ros2 topic hz` says ~100). The listeners:
  - `/follower/robot_state_publisher` turns joint angles into the position of every part of
    the arm (TF, Lesson 12).
  - `move_group` (MoveIt) needs to know where the arm is *now* to plan a move from there.
  - `sim_view` (the simulation window) draws the arm in the right pose. (It's missing if you
    started with `view:=false` in stages 1–2.)
- While the arm moves, every number in `position` changes; when it stops, they stay put. The
  `name` list doesn't change: it tells you which angle is which. It's in alphabetical order
  (`elbow_flex, gripper, shoulder_lift, shoulder_pan, wrist_flex, wrist_roll`), not in
  order along the arm!
- `ros2 action list` shows four actions. `arm.py` uses `/move_action` (MoveIt plans and moves
  the arm: `move_to`, `move_joints`, `go_to`) and `/follower/gripper_controller/gripper_cmd`
  (the gripper). The other two are what MoveIt itself uses to drive the arm's controller.

## Challenge: which joint moves the most?

It depends on what "the most" means, which is a good thing to discuss. Measured over one run of
the stage 2 demo (your numbers will be close, not identical):

| Joint | Biggest minus smallest angle | Total distance moved |
|---|---|---|
| `wrist_roll` | **163°** | 328° |
| `shoulder_lift` | 103° | 425° |
| `wrist_flex` | 100° | 428° |
| `shoulder_pan` | 99° | 374° |
| `elbow_flex` | 90° | 311° |
| `gripper` | 95° | **657°** |

- **Widest swing:** `wrist_roll`. A block looks the same from any angle, so MoveIt doesn't
  care how the wrist is rolled, and it sometimes rolls it a long way.
- **Most total movement:** the `gripper`: it opens and closes for every block.
- Of the joints that carry the arm around, `shoulder_lift` and `wrist_flex` travel the most:
  every pick goes down to the block and back up, and the wrist keeps the gripper pointing down.

How to find it from the command line: run `ros2 topic echo /follower/joint_states --field position`
while the demo runs, and watch which number changes the most (remember the alphabetical order
from `--field name`). Doing it properly, with a minimum, a maximum and a running total for each
joint, is a lot easier with a subscriber node. That's Lesson 10.
