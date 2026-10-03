# Lesson 3: Decisions, dictionaries and classes → 🥉 Bronze

**Goal:** make your programs decide things (`if`), look things up by name (dictionaries), and
understand the `Arm` class you've been using. Then choreograph a robot dance: the **Bronze** tier!

## Setup

Start the simulation, then run exercises from a second terminal:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
```bash
cd lessons/03_decisions_and_classes
python ex1_try_again.py
```

## Exercises (together)

1. **[`ex1_try_again.py`](ex1_try_again.py): `if` / `else`.**
   `move_to` returns `True` if it worked and `False` if not. Use that to try a backup plan.
2. **[`ex2_pose_book.py`](ex2_pose_book.py): dictionaries and `while` loops.**
   A "phone book" of poses: type a pose's name and the robot goes there.
3. **Inside the `Arm` class.** Open
   [`src/workshop_arm/workshop_arm/arm.py`](../../src/workshop_arm/workshop_arm/arm.py) together
   and find the answers:
   - What does `class Arm:` mean? What's `__init__` for?
   - Why does every function inside the class start with `self`?
   - Find `go_to`. What does it do if you ask for a pose that doesn't exist?
   - Find `SAVED_POSES`. Add your own pose there, rebuild (`colcon build`, then
     `source install/setup.bash`), and use it with `arm.go_to('your_pose')`.

## Challenge (on your own): 🥉 Bronze

**[`challenge_robot_dance.py`](challenge_robot_dance.py): a 30-second robot dance.**
Use everything so far: variables, lists, loops, functions, `if`, dictionaries.
Show it off at the end of the session!

## Things to remember

| Idea | Example |
|---|---|
| `if` / `elif` / `else` choose what to do | `if ok: ... else: ...` |
| Comparisons | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| `and`, `or`, `not` combine conditions | `if not ok and tries < 3:` |
| A dictionary maps names to values | `poses = {'up': [0, -90, 0, 0, 0]}` |
| Look up / check a name | `poses['up']`, `if name in poses:` |
| `while` repeats until a condition is false | `while name != 'quit':` |
| `*` spreads a list into a function's inputs | `arm.move_joints(*poses['up'])` |
| `input()` asks the person at the keyboard | `name = input('Pose? ')` |

**Next:** [Lesson 4: Forward kinematics](../04_forward_kinematics/)
