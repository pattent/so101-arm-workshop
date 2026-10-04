# Lesson 2: Lists and loops

**Goal:** stop repeating yourself. Use **lists** to keep many values in one variable,
**tuples** for values that belong together (like a point's x, y and z), and **`for` loops**
to do something with each one. Then use a loop to sweep the arm and draw shapes in the air.

## Setup

Exercises 2 and 3 move the robot, so start the simulation first:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
Then, in a second terminal (with `pixi shell` and `source install/setup.bash`):
```bash
cd lessons/02_lists_and_loops
python ex1_lists.py
```
(Exercise 1 doesn't need the simulation.)

## Exercises (together)

1. **[`ex1_lists.py`](ex1_lists.py): lists and tuples (no robot).**
   Make a list of the arm's joints, pick items out by their index (starting at 0!), add
   items, check what's in it, and group x, y and z into a tuple.
2. **[`ex2_waypoints.py`](ex2_waypoints.py): `for` loops.**
   Keep a list of points and send the gripper to each one in turn.
3. **[`ex3_sweep.py`](ex3_sweep.py): counting with `range`.**
   Sweep the arm from left to right in steps, count the moves, and collect a list of where
   the gripper went.

## Lists, tuples and loops

```python
joints = ['shoulder_pan', 'shoulder_lift', 'elbow_flex']   # a list, in [ ]
joints[0]                     # 'shoulder_pan': counting starts at 0
joints[-1]                    # 'elbow_flex': the last one
joints.append('wrist_flex')   # add one to the end

point = (0.25, 0.10, 0.15)    # a tuple, in ( ): like a list, but it can't change
x, y, z = point               # unpack it into three variables

for name in joints:           # do the indented lines once for each item
    print(name)
```

## Challenge (on your own)

**[`challenge_square_and_circle.py`](challenge_square_and_circle.py): draw shapes in the air.**
Make the gripper trace a square (a list of corners), then a circle (a `range` loop, with
`math.cos` and `math.sin`). The challenge file explains how to find points on a circle with
SOH-CAH-TOA, with a picture.

## Things to remember

| Idea | Example |
|---|---|
| A list holds many values, in order | `angles = [0, -45, 45, 45, 0]` |
| Get an item by its index (from 0) | `angles[0]`, `angles[-1]` for the last |
| A slice gets several items | `angles[0:3]` (items 0, 1 and 2) |
| How many items | `len(angles)` |
| Add to the end / change an item | `angles.append(10)`, `angles[0] = 30` |
| Is it in the list? (`True` or `False`) | `'gripper' in joints` |
| Biggest, smallest, total | `max(angles)`, `min(angles)`, `sum(angles)` |
| A tuple: a fixed group of values | `point = (0.25, 0.10, 0.15)` |
| Unpacking pulls a tuple apart | `x, y, z = point` |
| `for` repeats for each item | `for point in points:` |
| Indented lines belong to the loop | (4 spaces) |
| `range` counts | `range(3)` is 0, 1, 2; `range(-60, 61, 30)` is -60, -30, 0, 30, 60 |
| Start an empty list, fill it in a loop | `positions = []`, then `positions.append(...)` |

**Next:** [Lesson 3: Functions](../03_functions/)
