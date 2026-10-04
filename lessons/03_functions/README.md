# Lesson 3: Functions

**Goal:** get more out of **functions**. In Lesson 1 you wrote your first ones
(`to_degrees`, `distance_from_base`, `can_reach`). Now: inputs with default values, giving
back two answers at once, functions that move the robot, and functions that work on whole
lists. Then teach the robot to wave and draw.

## Setup

Exercise 2 and the challenge move the robot, so start the simulation first:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
Then, in a second terminal (with `pixi shell` and `source install/setup.bash`):
```bash
cd lessons/03_functions
python ex1_more_functions.py
```

## Exercises (together)

1. **[`ex1_more_functions.py`](ex1_more_functions.py): more from your functions (no robot).**
   Default values, returning two answers as a tuple (`point_on_circle`), and functions that
   build on each other.
2. **[`ex2_wave.py`](ex2_wave.py): functions that move the robot.**
   Write `wave(arm, times)`, then make the robot wave hello.
3. **[`ex3_functions_and_lists.py`](ex3_functions_and_lists.py): functions and lists (no robot).**
   Functions that take a list of points and give back the closest one, or a new list of just
   the reachable ones.

## Functions, one step further

```python
def can_reach(x, y, max_reach=0.48):   # max_reach has a default: you can leave it out
    return distance_from_base(x, y) < max_reach


can_reach(0.25, 0.10)                  # uses 0.48
can_reach(0.25, 0.10, max_reach=0.44)  # uses 0.44


def point_on_circle(center_x, center_y, radius, degrees):
    ...
    return x, y                        # two answers, as a tuple


x, y = point_on_circle(0.25, 0.0, 0.05, 90)   # unpack them
```

## Challenge (on your own)

**[`challenge_shapes.py`](challenge_shapes.py): a shape-drawing robot.**
Turn Lesson 2's square and circle loops into `square(...)` and `circle(...)` functions, then
draw a picture with them. Bonus: one `polygon(...)` function for any number of sides.

## Things to remember

| Idea | Example |
|---|---|
| `def` makes a function; its inputs go in `()` | `def wave(arm, times):` |
| A default value makes an input optional | `def can_reach(x, y, max_reach=0.48):` |
| Return two answers as a tuple, then unpack | `return x, y`, then `x, y = point_on_circle(...)` |
| Indented lines are the function's steps | (4 spaces) |
| `return` sends an answer back (and ends the function) | `return degrees * math.pi / 180` |
| Save the answer when you call it | `d = distance(0.25, 0.10)` |
| No `return` means the answer is `None` | `print` *shows* a value; `return` *gives it back* |
| A function can call other functions | `circle` can call `polygon` |
| Inputs can be lists, and so can answers | `def reachable(points, max_reach):` |
| Write a function once, use it many times | `wave(arm, 3)`, then `wave(arm, 5)` |

**Next:** [Lesson 4: Decisions and dictionaries](../04_decisions_and_dictionaries/)
