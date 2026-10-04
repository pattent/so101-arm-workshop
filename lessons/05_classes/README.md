# Lesson 5: Classes

**Goal:** write your own **classes**. In Lesson 1 you used objects (`arm = Arm()`) and added
to a class someone else wrote (`Rover`). Now you'll write whole classes from scratch, open
up the real `Arm` class to see how it's made, and build a new class on top of it
(**inheritance**).

## Setup

Exercises 3 and 4 and the challenge move the robot, so start the simulation first:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
```bash
cd lessons/05_classes
python ex1_my_first_class.py
```

## Exercises (together)

1. **[`ex1_my_first_class.py`](ex1_my_first_class.py): your first class (no robot).**
   A quick reminder with the `Rover` from Lesson 1, then write a class of your own from
   scratch (a drone, a bank account, a playlist: your choice), with its own attributes and
   methods.
2. **[`ex2_block.py`](ex2_block.py): a class for blocks (no robot).**
   A `Block` that knows its color and position, and can say how far it is from the robot and
   whether it's in a bin. (You'll use it again in Lesson 6.)
3. **Inside the `Arm` class.** Open
   [`src/workshop_arm/workshop_arm/arm.py`](../../src/workshop_arm/workshop_arm/arm.py) together.
   It's long, but it's built just like `Rover`. Find the answers:
   - Find `class Arm:` and its `__init__`. What does an `Arm` remember about itself?
   - Why does every method inside the class start with `self`?
   - Find `go_to`. What does it do if you ask for a pose that doesn't exist?
   - Find `SAVED_POSES` (a dictionary!). Add your own pose there, rebuild (`colcon build`, then
     `source install/setup.bash`), and use it with `arm.go_to('your_pose')`.
4. **[`ex4_inheritance.py`](ex4_inheritance.py): build on the `Arm` class.**
   A `ChattyArm` that *is* an `Arm`, plus a name, a move counter and new tricks.

## Writing a class

```python
class Rover:
    def __init__(self, name):       # runs once, when a new rover is made
        self.name = name            # self is "this rover": it remembers its name
        self.position = 0

    def drive(self, meters):        # a method: something the rover can do
        self.position = self.position + meters


curiosity = Rover('Curiosity')      # make one (an object)
curiosity.drive(3)
print(curiosity.position)           # 3
```

**Inheritance:** `class ChattyArm(Arm):` means "a ChattyArm is an Arm, plus some extras". It
gets every method `Arm` has for free. `super()` means "the class I'm built on", so
`super().__init__()` lets `Arm` set itself up first.

## Challenge (on your own)

**[`challenge_dancing_arm.py`](challenge_dancing_arm.py): a `DancingArm` class.**
Turn your Bronze dance into a class built on `Arm`, so a whole dance is one line:
`dancer.perform(['up', 'wave', 'bow'])`.

## Things to remember

| Idea | Example |
|---|---|
| `class` makes your own kind of object | `class Rover:` |
| `__init__` sets up a new object | `def __init__(self, name):` |
| `self` is "this one": store attributes on it | `self.position = 0` |
| A method is a function inside a class | `def drive(self, meters):` |
| Make an object by calling the class | `curiosity = Rover('Curiosity')` |
| Every object has its own attributes | driving `curiosity` doesn't move `perseverance` |
| Inside a class, call your own methods on `self` | `self.drive(-self.position)` |
| Inheritance: get everything another class has | `class ChattyArm(Arm):` |
| `super()` is the class you built on | `super().__init__()`, `super().go_to(pose)` |

**Next:** [Lesson 6: Python for robots](../06_python_for_robots/)
