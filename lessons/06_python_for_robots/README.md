# Lesson 6: Python for robots

**Goal:** the last Python ideas you need before ROS: **callbacks** (handing a function to
someone else to call later), **handling errors**, and splitting a program into **your own
files**. Robot programs use these everywhere: a camera calls your code for every new picture,
sensors send garbage now and then, and real projects are many files.

Why now? In Lesson 10 you'll write ROS 2 nodes, and a node looks like this:

```python
class JointListener(Node):                 # inheritance (Lesson 5): a JointListener IS a Node
    def __init__(self):
        super().__init__('joint_listener') # let Node set itself up first
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)

    def on_joints(self, msg):              # a callback (this lesson): ROS calls it for every message
        ...
```

Every line of that uses something from Lesson 5 or this lesson. Learn them here, with no ROS
in the way, and Lesson 10 will feel easy.

## Setup

Nothing in this lesson needs the simulation.
```bash
cd lessons/06_python_for_robots
python ex1_callbacks.py
```

## Exercises (together)

1. **[`ex1_callbacks.py`](ex1_callbacks.py): callbacks.**
   Give a simulated distance sensor a function, and it calls your function for every reading.
   This is exactly how ROS delivers messages to your code.
2. **[`ex2_when_things_go_wrong.py`](ex2_when_things_go_wrong.py): errors.**
   Read an error message (a "traceback"), catch errors with `try` / `except`, and raise your own.

## Your own files (modules)

Any `.py` file is a **module** you can import, just like `math` or `workshop_arm`. If
`blocks.py` sits next to your program, then

```python
from blocks import Block
```

gives you the `Block` class from it. That's how real projects stay tidy: `workshop_arm` is the
same idea, split into `arm.py`, `vision.py`, `table.py` and so on.

## Challenge (on your own)

**[`challenge_block_report.py`](challenge_block_report.py): a camera report.**
A simulated camera ([`fake_camera.py`](fake_camera.py)) sends you a list of blocks every time it
takes a picture, and like a real camera, it sometimes sends garbage. Put your `Block` class
from Lesson 5 into its own file `blocks.py`, write a callback that turns each picture into
`Block` objects, skip the bad readings with `try` / `except`, and report which block the robot
should pick up first.

This is the same job `vision_demo` does in Lesson 16, minus the real camera.

## Things to remember

| Idea | Example |
|---|---|
| Functions are values too: pass one *without* `()` | `sensor.subscribe(on_reading)` |
| A **callback** is a function someone else calls later | ROS calls `on_joints(msg)` for every message |
| A method can be a callback, and remember things on `self` | `sensor.subscribe(tracker.on_reading)` |
| `try` / `except` catches an error instead of crashing | `except ValueError:` |
| `raise` reports a problem yourself | `raise ValueError('Unknown color')` |
| Read a traceback from the **bottom** up | last line = what went wrong; above it = where |
| Import from your own file | `from blocks import Block` |

**Next:** [Lesson 7: Forward kinematics](../07_forward_kinematics/)
