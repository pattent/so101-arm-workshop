# Lesson 4: Decisions and dictionaries → 🥉 Bronze

**Goal:** make your programs decide things (`if`, `elif`, `else`), repeat until something
happens (`while`), and look things up by name (**dictionaries**). Then put everything from
Lessons 1–4 together in a robot dance: the **Bronze** tier!

## Setup

Exercises 1 and 3 and the Bronze challenge move the robot, so start the simulation first:
```bash
ros2 launch workshop_arm workshop.launch.py stage:=1
```
```bash
cd lessons/04_decisions_and_dictionaries
python ex1_try_again.py
```

## Exercises (together)

1. **[`ex1_try_again.py`](ex1_try_again.py): `if` / `else`.**
   `move_to` returns `True` if it worked and `False` if not. Use that to try a backup plan.
2. **[`ex2_dictionaries.py`](ex2_dictionaries.py): dictionaries (no robot).**
   The real table's bins, by color: look them up, add and change them, loop over them, and
   count blocks by color.
3. **[`ex3_pose_book.py`](ex3_pose_book.py): a dictionary and a `while` loop.**
   A pose book: type a pose's name and the robot goes there, until you type `quit`.

## Decisions and dictionaries

```python
if ok:                            # True or False decides which lines run
    print('It worked!')
elif tries < 3:                   # checked only if the first one was False
    print('Trying again...')
else:                             # if nothing above was True
    print('Giving up.')

bins = {'red': (0.12, 0.22), 'blue': (0.34, 0.12)}   # a dictionary: key: value
bins['red']                       # (0.12, 0.22): look up by key
bins['green'] = (0.24, 0.20)      # add (or change) a key
for color, position in bins.items():
    print(color, position)
```

Which one should I use? A **list** when the order matters (waypoints, a choreography).
A **dictionary** when you look things up by name (bins by color, poses by name).

## Challenge (on your own): 🥉 Bronze

**[`challenge_robot_dance.py`](challenge_robot_dance.py): a 30-second robot dance.**
Use everything so far: variables, lists, loops, functions, `if` and dictionaries.
Show it off at the end of the session!

## Things to remember

| Idea | Example |
|---|---|
| `if` / `elif` / `else` choose what to do | `if ok: ... else: ...` |
| Comparisons give `True` or `False` | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| `and`, `or`, `not` combine conditions | `if not ok and tries < 3:` |
| `while` repeats until its condition is `False` | `while name != 'quit':` |
| A dictionary maps keys to values | `poses = {'up': [0, -90, 0, 0, 0]}` |
| Look up / check a key | `poses['up']`, `if name in poses:` |
| Add or change a key | `poses['bow'] = [0, -20, 20, 70, 0]` |
| Loop over keys and values | `for name, angles in poses.items():` |
| A missing key is an error (`KeyError`) | check with `in` first |
| `*` spreads a list into a function's inputs | `arm.move_joints(*poses['up'])` |
| `input()` asks the person at the keyboard | `name = input('Pose? ')` |

**Next:** [Lesson 5: Classes](../05_classes/)
