# Lesson 2: Loops and functions

**Goal:** stop repeating yourself. Use **lists** to hold many things, **`for` loops** to do
something to each one, and **functions** to give a set of steps a name.

## Setup

Every exercise in this lesson moves the robot, so start the simulation first:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
Then, in a second terminal (with `pixi shell` and `source install/setup.bash`):
```bash
cd lessons/02_loops_and_functions
python ex1_waypoints.py
```

## Exercises (together)

1. **[`ex1_waypoints.py`](ex1_waypoints.py): lists and `for` loops.**
   Keep a list of points and send the gripper to each one in turn.
2. **[`ex2_wave.py`](ex2_wave.py): functions.**
   Write `wave(arm, times)`, then make the robot wave hello.

## Challenge (on your own)

**[`challenge_square_and_circle.py`](challenge_square_and_circle.py): draw shapes in the air.**
Make the gripper trace a square, then a circle (using `math.cos` and `math.sin`).

## Things to remember

| Idea | Example |
|---|---|
| A list holds many values, in order | `points = [(0.2, 0.0, 0.1), (0.3, 0.0, 0.1)]` |
| A tuple is a small fixed group of values | `(x, y, z)` |
| `for` repeats for each item in a list | `for point in points:` |
| `range(n)` counts 0, 1, ..., n-1 | `for i in range(3):` |
| Indented lines belong to the loop or function | (4 spaces) |
| `def` makes a function | `def wave(arm, times):` |
| Unpacking pulls a tuple apart | `x, y, z = point` |

**Next:** [Lesson 3: Decisions and classes](../03_decisions_and_classes/)
