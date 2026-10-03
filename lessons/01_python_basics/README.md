# Lesson 1: Python basics

**Goal:** write and run your first Python programs: variables, numbers, text, `print`, and
the `math` module. Then use them to move the robot.

## How to run the exercises

Open a terminal in this folder with ROS turned on:
```bash
cd so101-arm-workshop
pixi shell
source install/setup.bash
cd lessons/01_python_basics
python ex1_hello_robot.py
```

Each exercise file has `TODO` comments telling you what to fill in. Run it, read what it
prints, change it, run it again. Stuck? Peek in [`solutions/`](solutions/), but try first!

## Exercises (together)

1. **[`ex1_hello_robot.py`](ex1_hello_robot.py): variables and `print`.**
   Store facts about the robot in variables and print them.
2. **[`ex2_degrees_and_radians.py`](ex2_degrees_and_radians.py): math with angles.**
   People think in degrees, robots think in radians. Convert between them.
3. **[`ex3_how_far.py`](ex3_how_far.py): the Pythagorean theorem.**
   How far is the gripper from the robot's base? Can the arm reach a point?

## Challenge (on your own)

**[`challenge_my_first_robot.py`](challenge_my_first_robot.py): move the real (simulated) arm.**
Start the simulation first, in another terminal:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
Then make the arm visit three different poses of your choice.

## Things to remember

| Idea | Example |
|---|---|
| A variable stores a value | `joints = 5` |
| Text goes in quotes | `name = 'SO-101'` |
| `print` shows things | `print('The arm has', joints, 'joints')` |
| f-strings mix text and values | `print(f'{name} has {joints} joints')` |
| `import math` gives you math tools | `math.pi`, `math.sqrt(16)`, `math.radians(90)` |
| `#` starts a comment (Python ignores it) | `# this is a note for humans` |

**Next:** [Lesson 2: Loops and functions](../02_loops_and_functions/)
