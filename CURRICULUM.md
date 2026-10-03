# SO-101 Workshop Curriculum (draft)

**Final project: the color-sorting robot.** A camera spots colored blocks on the table, and the
SO-101 arm picks each one up and drops it in the bin of the same color, first in simulation and
later, if she wants, on a real arm with the same code.

**Pace:** about 12 modules, roughly one per week, but we move on when she's ready, not when the
calendar says. Every module has exercises we do **together** and one **challenge** she tries on her own.

**Approach:** she drives the (simulated) robot from week 2 on. Python is learned *through* the arm
instead of before it. Each module peels back one layer of "magic" until she understands the whole
stack from webcam pixels to motor commands.

---

## Final project tiers

| Tier | Goal | Unlocked after |
|---|---|---|
| 🥉 Bronze | Program a "robot dance": a routine of poses and gripper moves | Module 3 |
| 🥈 Silver | Sort 3 blocks from known positions into bins, avoiding obstacles | Module 10 |
| 🥇 Gold | The camera finds the blocks (simulated first), arm sorts them automatically | Module 12 |

## Simulation stages

The simulation grows with her (`ros2 launch workshop_arm workshop.launch.py stage:=N`):

| Stage | What's in the simulation | Used in |
|---|---|---|
| 1 | Arm, MoveIt, RViz, empty table | Modules 0–9 |
| 2 | + bins and blocks at known spots | Module 10 (Silver) |
| 3 | + random blocks, live overhead camera, block detector | Modules 11–12 (Gold) |

## Working backwards: the skills Gold needs

```
Gold: webcam → block positions → arm sorts them
 ├─ Vision: OpenCV color detection, pixel → table coordinates      (Modules 11–12)
 ├─ Manipulation: pick/place sequences, obstacles, MoveIt         (Modules 9–10)
 ├─ ROS 2: nodes, topics, actions, TF, robot models                (Modules 6–8)
 ├─ Arm geometry: coordinates, forward & inverse kinematics        (Modules 4–5)
 └─ Python: variables → loops → functions → classes               (Modules 1–3)
```

---

## Module 0: Kickoff, "Here's where we're going"

- Watch where we're going: `workshop.launch.py stage:=3` + `ros2 run workshop_arm vision_demo` (the arm finds and sorts blocks by itself).
- Play: drag the arm around in RViz with the interactive marker.
- Show a video of a real SO-101 sorting blocks, so she sees what's possible.
- Install pixi and the workshop on her laptop (see README). **Goal: she leaves with it running.**
- First taste of the ROS routine she will use every session: `pixi shell` → `source` → `ros2 launch` / `ros2 run`.
- Talk: what would *she* want the arm to do? (Adjust the final project if she has a better idea.)

## Part 1: Python, through the robot

### Module 1: Python basics
Variables, numbers, strings, `print`, `math`, running a `.py` file.
- Together: convert joint angles between degrees and radians. Why do robots use radians?
- Together: the gripper is at `(0.25, 0.10)`. How far is that from the base? (Pythagoras in code.)
- Challenge: write `my_first_robot.py` that moves the arm to 3 different poses with `move_joints`.

### Module 2: Lists, loops, functions
- Together: a list of waypoints, and a `for` loop that visits each one.
- Together: write a function `wave(arm, times)` that waves the wrist.
- Challenge: make the gripper trace a square in the air with `move_to` (then a circle, using `math.cos`/`math.sin`).

### Module 3: Decisions, dictionaries, classes → 🥉 Bronze
- Together: `if` the move fails (`move_to` returns `False`), print a message and try somewhere else.
- Together: a dictionary of named poses (`{'wave_left': [...], ...}`).
- Together: open up `workshop_arm/arm.py`. It's just a class! Read it together; what does `self` mean?
- **Bronze challenge:** choreograph a 30-second robot dance.

## Part 2: How arms work

### Module 4: Coordinates and forward kinematics
Frames, x/y/z, joint angles → gripper position.
- Together: a 2-link arm on paper, then in Python with `matplotlib` (draw the arm).
- Together: compute where the SO-101's gripper should be for some joint angles; compare with `arm.where_am_i()`.
- Challenge: plot every point the 2-link arm can reach (its "workspace").

### Module 5: Inverse kinematics
Gripper position → joint angles (the reverse problem).
- Together: solve 2-link IK with trig; animate it following the mouse.
- Together: why does "elbow up" vs "elbow down" give two answers?
- Challenge: use her own IK + `move_joints` to reach a point, then compare with `move_to` (which uses MoveIt's IK).

## Part 3: ROS 2, the robot's nervous system

### Module 6: Nodes and topics
- Together: turtlesim. Drive the turtle, `ros2 node list`, `ros2 topic echo`, `rqt_graph`.
- Together: look at the real arm system: `ros2 topic echo /follower/joint_states`.
- Challenge: from the command line only, find out which joint moves most during the demo.

### Module 7: Writing ROS 2 nodes
Publishers, subscribers, services, actions.
- Together: a subscriber that prints the arm's joint angles in degrees.
- Together: re-read `arm.py`. Now the `ActionClient` parts make sense.
- Challenge: a "safety monitor" node that warns when the gripper goes below the table (z < 0).

### Module 8: Robot models and TF
URDF, links and joints, TF frames, RViz.
- Together: read the SO-101 URDF and match each `<joint>` to the real arm.
- Together: `ros2 run tf2_ros tf2_echo base_link gripper_frame_link` while the arm moves.
- Challenge: build a tiny 2-link arm URDF from scratch and view it in RViz with sliders.

## Part 4: Manipulation

### Module 9: MoveIt and the planning scene
- Together: plan and execute in RViz's MotionPlanning panel.
- Together: add a table and a wall as obstacles; watch MoveIt plan around them.
- Challenge: add obstacles from Python and reach a target "behind" one.

### Module 10: Pick and place → 🥈 Silver
Simulation: `stage:=2` (bins and blocks at the known spots in `table.py`).
- Together: show blocks and bins in RViz (markers/collision objects); "attach" a block to the gripper when grasped.
- Together: break pick/place into functions: `pick(x, y)`, `place(x, y)`.
- **Silver challenge:** sort 3 blocks at known positions into 2 bins by color.

## Part 5: Seeing the world

### Module 11: Computer vision with OpenCV
Simulation: `stage:=3` (random blocks + a live overhead camera).
- Together: watch the simulation window, then open the raw topic with `ros2 run rqt_image_view rqt_image_view /camera/image_raw`. What does the robot "see"? Move the arm: it blocks the view!
- Together: build a color mask (HSV thresholding) for one color and display it; tune the ranges.
- Together: find contours, filter by size (why do the bins not count as blocks?), mark the centers.
- Challenge: add yellow blocks: a new color range in `vision.py` (and a yellow bin in `table.py`).
- Bonus: run the same `find_blocks()` on a photo from her laptop webcam of colored paper squares.

### Module 12: Pixels to the real world → 🥇 Gold
- Together: the pinhole camera model: why does `pixel_to_table()` need the camera's height and focal length?
- Together: check accuracy: compare detected positions with where the blocks really are.
- Together: read `block_detector.py`: turning a function into a ROS node that publishes `/detected_blocks`.
- Together: run with `detector:=false` and plug in her own detector node.
- **Gold challenge:** write her own version of `vision_demo`: look → pick → place → look again
  until the table is clean. Stretch: sort the closest block first; recover from a missed grab.
- (Real webcam later: calibrate with 4 marked corners on paper → homography, replacing the pinhole math.)

---

## Beyond (her call)

- **Real hardware:** buy/print an SO-101 follower arm; same code with `hardware_type:=real`.
- **Physics simulation:** run the arm in Gazebo and watch it push real (simulated) blocks.
- **AI:** record demonstrations with a leader arm and train a LeRobot policy.

## Open items for instructors

- [ ] Dry-run the install on a real Windows laptop and a real Mac (only tested on Linux so far).
- [x] Build the RViz block/bin visualization helpers for Module 10.
- [x] Simulated overhead camera + block detector for Modules 11–12.
- [ ] Write the exercise starter files and solutions for each module.
