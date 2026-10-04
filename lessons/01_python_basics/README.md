# Lesson 1: Python basics

**Goal:** write and run your first Python programs: variables, numbers, text, and *using*
functions like `print`, `math.sqrt` and `arm.move_to`. Then use them to move the robot.

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

## Functions: you're already using them

A **function** is a named action. You *call* it by writing its name and putting its inputs in
parentheses. Many functions also give back an answer (their **return value**).

```python
print('hello')                # name: print       input: 'hello'   (shows it; no answer)
root = math.sqrt(16)          # name: math.sqrt   input: 16        answer: 4.0, saved in root
ok = arm.move_to(0.25, 0, 0.1)  # name: arm.move_to  inputs: x, y, z  answer: True or False
```

The dot in `math.sqrt` means "the `sqrt` function that lives in `math`". In Lesson 2 you'll
write your own functions with `def`.

## What is `workshop_arm`?

The challenge starts with `from workshop_arm import Arm`. `workshop_arm` is **our own Python
package**, written for this workshop. It lives in
[`src/workshop_arm/`](../../src/workshop_arm/workshop_arm/arm.py) (you'll read it in Lesson 3).
It hides the complicated ROS 2 and MoveIt parts so you can move the robot with one line, like
`arm.move_to(0.25, 0.0, 0.10)`.

It isn't downloaded from anywhere: `colcon build` installs it into the `install/` folder, and
`source install/setup.bash` tells Python where to find it. That's why you run that line in every
new terminal. If you ever see `ModuleNotFoundError: No module named 'workshop_arm'`, you forgot it.

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
| Call a function: name + inputs in `()` | `math.sqrt(16)`, `arm.go_to('rest')` |
| Save a function's answer | `root = math.sqrt(16)` |
| `#` starts a comment (Python ignores it) | `# this is a note for humans` |

**Next:** [Lesson 2: Loops and functions](../02_loops_and_functions/)
