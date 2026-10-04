# Lessons

**Final project: the color-sorting robot.** A camera spots colored blocks on the table, and the
SO-101 arm picks each one up and drops it in the bin of the same color. First in simulation,
and later, if you want, on a real arm with the same code.

**How it works:** one folder per lesson. Each has a `README.md` (what you'll learn and what to
do), starter files with `TODO`s to fill in, and a `solutions/` folder to check your work
*after* you've tried. Every lesson has exercises we do **together** and a **challenge** you try
on your own. We move on when you're ready, not when the calendar says.

**Approach:** you drive the (simulated) robot from the very first lesson. Python is learned
*through* the arm instead of before it. Each lesson peels back one layer of "magic" until you
understand the whole thing, from camera pixels to motor commands.

## The lessons

| # | Lesson | You'll learn | Simulation | Status |
|---|---|---|---|---|
| 0 | [Kickoff](00_kickoff/) | Where we're going; install everything | stage 3 | ✅ ready |
| 1 | [Python basics](01_python_basics/) | Variables, `print`, math; first robot moves | stage 1 | ✅ ready |
| 2 | [Loops and functions](02_loops_and_functions/) | Lists, `for`, `def`; draw shapes in the air | stage 1 | ✅ ready |
| 3 | [Decisions and classes](03_decisions_and_classes/) | `if`, dictionaries, classes. 🥉 **Bronze** | stage 1 | ✅ ready |
| 4 | [Forward kinematics](04_forward_kinematics/) | Coordinates; joint angles → gripper position | stage 1 | outline |
| 5 | [Inverse kinematics](05_inverse_kinematics/) | Gripper position → joint angles | stage 1 | outline |
| 6 | [Nodes and topics](06_nodes_and_topics/) | How ROS 2 programs talk | stage 1 | outline |
| 7 | [Writing nodes](07_writing_nodes/) | Your own publishers and subscribers | stage 1 | outline |
| 8 | [Robot models and TF](08_robot_models_and_tf/) | URDF, coordinate frames | stage 1 | outline |
| 9 | [MoveIt and obstacles](09_moveit_and_obstacles/) | Motion planning around things | stage 1 | outline |
| 10 | [Pick and place](10_pick_and_place/) | Grabbing and sorting. 🥈 **Silver** | stage 2 | outline |
| 11 | [Computer vision](11_computer_vision/) | Finding blocks with OpenCV | stage 3 | outline |
| 12 | [Pixels to the real world](12_pixels_to_world/) | Camera math; the robot sorts by itself. 🥇 **Gold** | stage 3 | outline |

"Outline" means the lesson plan is written, but the starter files and solutions are still to come.

## Final project tiers

| Tier | Goal | Unlocked after |
|---|---|---|
| 🥉 Bronze | Program a 30-second "robot dance" | Lesson 3 |
| 🥈 Silver | Sort 3 blocks from known positions into matching bins | Lesson 10 |
| 🥇 Gold | The camera finds the blocks, and the arm sorts them by itself | Lesson 12 |

## Simulation stages

The simulation grows with you: `ros2 launch workshop_arm workshop.launch.py stage:=N`

| Stage | What's in the simulation | Lessons |
|---|---|---|
| 1 | The arm on an empty table | 1–9 |
| 2 | + bins, and blocks at known spots | 10 |
| 3 | + blocks at random spots, a live overhead camera, a block detector | 0, 11–12 |

## Working backwards: the skills Gold needs

```
Gold: camera → block positions → arm sorts them
 ├─ Vision: OpenCV color detection, pixels → table coordinates     (Lessons 11–12)
 ├─ Manipulation: pick/place, obstacles, MoveIt                    (Lessons 9–10)
 ├─ ROS 2: nodes, topics, actions, TF, robot models                (Lessons 6–8)
 ├─ Arm geometry: coordinates, forward & inverse kinematics        (Lessons 4–5)
 └─ Python: variables → loops → functions → classes                (Lessons 1–3)
```

## Beyond (her call)

- **Real hardware:** build or buy an SO-101 arm; the same code runs with `hardware_type:=real`.
- **Real physics:** turn on MuJoCo's physics so grasps can slip and blocks can tumble.
- **Gripper camera:** a camera on the wrist instead of above the table.
- **AI:** record demonstrations with a second "leader" arm and train a LeRobot policy.

## Notes for instructors

See the [instructor guide](../docs/instructor_guide.md) for session prep and timing.

- [ ] Dry-run the install on a real Windows laptop and a real Mac (only tested on Linux so far).
- [ ] Starter files and solutions for Lessons 4–12.
- Run a lesson's exercises from inside its folder, in a terminal with `pixi shell` and
  `source install/setup.bash`. Exercises that move the robot need the simulation running in
  another terminal.
