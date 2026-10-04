# Lesson 9: Nodes and topics

**Goal:** see how ROS 2 works inside. A robot isn't one big program: it's many small programs
called **nodes**, each with one job, that talk by sending **messages** on named channels
called **topics**. Today you explore them from the command line; in Lesson 10 you write your own.

| Word | Means | Example |
|---|---|---|
| **node** | one small program with one job | `turtlesim`, `move_group` (MoveIt) |
| **topic** | a named channel for messages; anyone can send (**publish**) or listen (**subscribe**) | `/turtle1/cmd_vel` |
| **message** | one piece of data sent on a topic, with a fixed shape (its **type**) | a `Twist`: "go forward 2, turn 1.8" |
| **service** | ask a question, get one answer back | "reset the turtle" |
| **action** | a long job that reports progress and a result | "move the arm there" |

Every terminal in this lesson needs `pixi shell` and `source install/setup.bash`, as always.
Answers are in [`solutions/answers.md`](solutions/answers.md), for after you've tried.

## Exercises (together)

### 1. Meet the turtle

You'll need three terminals. In the first:
```bash
ros2 run turtlesim turtlesim_node
```
In the second (then click on this terminal, and drive with the arrow keys):
```bash
ros2 run turtlesim turtle_teleop_key
```
In the third, look around while you drive:
```bash
ros2 node list                      # which programs are running?
ros2 topic list                     # which channels exist?
ros2 topic echo /turtle1/pose       # listen in (Ctrl+C to stop)
ros2 topic info /turtle1/cmd_vel    # who talks and who listens on this channel?
rqt_graph                           # a picture of nodes (ovals) and topics (boxes)
```

- Which node *publishes* on `/turtle1/cmd_vel`, and which node *subscribes* to it?
- What happens to `/turtle1/pose` while you drive? While you don't?

### 2. Talk to the turtle yourself

Close the teleop terminal. Now *you* are the publisher. What does a `cmd_vel` message look like?
```bash
ros2 topic info /turtle1/cmd_vel            # its type is geometry_msgs/msg/Twist
ros2 interface show geometry_msgs/msg/Twist # what's inside a Twist
```
Send one message, then send one every second:
```bash
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}}"
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
```
- What does `linear.x` do? And `angular.z`? Try a negative number.
- Make the circle bigger, then smaller.

A first look at **services** (a question with one answer):
```bash
ros2 service list
ros2 service call /reset std_srvs/srv/Empty
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 2.0, name: 'turtle2'}"
```
- After spawning `turtle2`, run `ros2 topic list` again. What's new?

### 3. The arm's nervous system

Close everything, and start the arm:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
That one command started many nodes. In a second terminal:
```bash
ros2 node list
ros2 topic list
ros2 topic echo --once /follower/joint_states   # one message: every joint's angle (radians)
ros2 topic hz /follower/joint_states            # how many messages per second?
ros2 topic info --verbose /follower/joint_states
rqt_graph
```
- Which node publishes the joint angles? Which nodes listen to them? Why does each one care?
- Move the arm with RViz (drag the gripper marker, **Plan & Execute**) while
  `ros2 topic echo /follower/joint_states` runs. What changes?
- The **actions**: run `ros2 action list`. Two of those are what `arm.move_to` and
  `arm.open_gripper` use. Which two? (Peek at `__init__` in
  [`arm.py`](../../src/workshop_arm/workshop_arm/arm.py).)

## Challenge (on your own)

Stop the simulation and start stage 2 (`stage:=2`). Using **only the command line**, find out
which joint moves the most while `ros2 run workshop_arm demo` sorts the blocks.

Hint: `ros2 topic echo /follower/joint_states --field position` prints just the angles, and the
joints are in the order listed in `name`.

## Things to remember

| Command | What it does |
|---|---|
| `ros2 run <package> <program>` | start one node |
| `ros2 launch <package> <file>` | start many nodes at once (Lesson 11 shows how) |
| `ros2 node list` | which nodes are running |
| `ros2 topic list` | which topics exist |
| `ros2 topic echo <topic>` | print the messages on a topic |
| `ros2 topic info -v <topic>` | its type, publishers and subscribers |
| `ros2 topic hz <topic>` | how many messages per second |
| `ros2 topic pub <topic> <type> "<data>"` | send messages yourself |
| `ros2 interface show <type>` | what's inside a message type |
| `ros2 service list` / `ros2 service call` | list / call services |
| `ros2 action list` | list actions |
| `rqt_graph` | a picture of who talks to whom |

**Next:** [Lesson 10: Writing ROS 2 nodes](../10_writing_nodes/)
