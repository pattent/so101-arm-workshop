# Lesson 1: Python basics

**Goal:** write and run your first Python programs: variables and the four basic **types** of
data (whole numbers, decimals, text, True/False), math, your first **functions**, and
**objects** made from a class. Then use all of it to move the robot.

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

None of these need the robot.

1. **[`ex1_hello_robot.py`](ex1_hello_robot.py): variables, `print` and types.**
   Store facts about the robot in variables and print them. Then meet the four basic types
   (`int`, `float`, `str`, `bool`) and see why `'5' + '5'` isn't 10.
2. **[`ex2_degrees_and_radians.py`](ex2_degrees_and_radians.py): angles, and your first function.**
   People think in degrees, robots think in radians. Convert by hand, then by *calling* a
   function, then *write* your own `to_degrees` function. (Read "Functions" below first.)
3. **[`ex3_how_far.py`](ex3_how_far.py): how far, and can the arm reach it?**
   The Pythagorean theorem, turned into functions you write: `distance_from_base(x, y)` and
   `can_reach(x, y)`.
4. **[`ex4_objects.py`](ex4_objects.py): objects and classes.**
   What `arm = Arm()` and `arm.move_joints(...)` mean. Make simulated Mars rovers from a
   `Rover` class, then give the class a battery and a new method. (Read "Objects" below first.)

## Functions

A **function** is a named action. You **call** it by writing its name and putting its inputs
in parentheses, in a fixed order. Many functions give back an answer (their **return value**):

```python
print('hello')                # name: print       input: 'hello'   (shows it; no answer)
root = math.sqrt(16)          # name: math.sqrt   input: 16        answer: 4.0, saved in root
ok = arm.move_to(0.25, 0, 0.1)  # name: arm.move_to  inputs: x, y, z  answer: True or False
```

You can **write** your own with `def`:

```python
def to_radians(degrees):              # def, the function's name, and its inputs
    return degrees * math.pi / 180    # indented: the steps. return: the answer it gives back


answer = to_radians(90)               # call it like any other function
```

`print` *shows* a value on the screen; `return` *gives it back*, so you can save it in a
variable or use it in a calculation.

## Objects

Some values come with their own functions, called with a dot: `'so-101'.upper()` gives back
`'SO-101'`. A value like that is an **object**, and its functions are its **methods**.

A **class** is a blueprint for making objects. Inside, `__init__` sets up each new object,
`self` means "this object", and variables stored on `self` (its **attributes**) are what it
remembers:

```python
class Rover:
    def __init__(self, name):         # runs once, when a new rover is made
        self.name = name              # an attribute: the rover remembers its name

    def report(self, message):        # a method: something the rover can do
        print(f'{self.name}: {message}')


curiosity = Rover('Curiosity')        # make a rover (an object) from the blueprint
curiosity.report('Systems online.')   # Curiosity: Systems online.
```

The robot arm works the same way: `arm = Arm()` makes it, and `arm.move_joints(...)` is one of
its methods. In Lesson 5 you'll write whole classes of your own, and open the `Arm` class to
see how it's made.

## What is `workshop_arm`?

The challenge starts with `from workshop_arm import Arm`. `workshop_arm` is **our own Python
package**, written for this workshop. It lives in
[`src/workshop_arm/`](../../src/workshop_arm/workshop_arm/arm.py) (you'll read it in Lesson 5).
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
Then make the arm visit three different poses of your choice. Bonus: write a function that
takes the robot as an input.

## Things to remember

| Idea | Example |
|---|---|
| A variable stores a value | `joints = 5` |
| `int`: a whole number | `5`, `-45` |
| `float`: a number with a decimal | `0.48`, `2.0` (and every `/` answer) |
| `str`: text, in quotes | `name = 'SO-101'` |
| `bool`: `True` or `False` | `gripper_is_open = True` |
| Check a value's type | `type(0.48)` |
| Turn text into a number | `int('5')`, `float('0.25')` |
| `print` shows things | `print('The arm has', joints, 'joints')` |
| f-strings mix text and values | `print(f'{name} has {joints} joints')` |
| `import math` gives you math tools | `math.pi`, `math.sqrt(16)`, `math.radians(90)` |
| Call a function: name + inputs in `()`, in order | `round(3.14159, 2)`, `arm.go_to('rest')` |
| Save a function's answer | `root = math.sqrt(16)` |
| Write a function: `def`, inputs, `return` | `def to_degrees(radians):` |
| A comparison is a `bool` you can return | `return distance < 0.48` |
| A class is a blueprint; calling it makes an object | `curiosity = Rover('Curiosity')`, `arm = Arm()` |
| Methods: the object, a dot, the method | `curiosity.drive(3)`, `arm.move_joints(...)` |
| Attributes: values the object remembers | `self.battery = 100`, `curiosity.position` |
| `#` starts a comment (Python ignores it) | `# this is a note for humans` |

**Next:** [Lesson 2: Lists and loops](../02_lists_and_loops/)
