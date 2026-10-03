# SO-101 Robot Arm Workshop

Learn Python, ROS 2 and robot arm programming with a simulated
[SO-101](https://github.com/TheRobotStudio/SO-ARM100) arm. By the end, the robot uses a camera
to find colored blocks on a table and sorts them into matching bins.

Runs natively on **Windows, macOS and Linux**: no virtual machine needed. We use
[pixi](https://pixi.sh) only to **install** ROS 2 Jazzy (it's the official way to install ROS 2
on Windows). After that, everything is the standard ROS 2 workflow: `source`, `colcon build`,
`ros2 launch`, `ros2 run`.

> **Status:** fully tested on Ubuntu Linux. Every package is available for Windows and macOS
> (Intel and Apple Silicon), but those haven't been tried on a real machine yet. If something
> breaks there, see [Troubleshooting](#troubleshooting).

## Setup (one time, about 10 minutes)

### 1. Install pixi

**macOS / Linux** (Terminal):
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows** (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Close and reopen your terminal afterwards.

### 2. Download the workshop

```bash
pixi global install git    # only if you don't already have git
git clone https://github.com/pattent/so101-arm-workshop.git
cd so101-arm-workshop
```

> **Windows:** clone it somewhere with a short path, like `C:\so101`. Windows has trouble with
> very long file paths.

### 3. Install ROS 2 and build the workspace

From inside the `so101-arm-workshop` folder:
```bash
pixi install                        # downloads ROS 2 Jazzy, MoveIt 2, RViz, MuJoCo, OpenCV (~6 GB)
pixi shell                          # turns on ROS 2 in this terminal
python scripts/setup_workspace.py   # downloads the SO-101 robot packages
colcon build                        # builds the workspace
```

## Every new terminal

```bash
cd so101-arm-workshop
pixi shell                     # ROS 2 Jazzy (like `source /opt/ros/jazzy/setup.bash`)
source install/setup.bash      # our workspace
```

On Windows, the last line is `install\setup.ps1` in PowerShell, or `call install\setup.bat` in
Command Prompt. Run it again after every `colcon build`.

## Running the simulation

The simulation grows with you. Start the stage you're at:

| Stage | Command | What's on the table | Lessons |
|---|---|---|---|
| 1 | `ros2 launch workshop_arm workshop.launch.py stage:=1` | Nothing: just the arm | Modules 0–9 |
| 2 | `ros2 launch workshop_arm workshop.launch.py stage:=2` | Bins, and blocks at **known** spots (`KNOWN_BLOCKS` in `table.py`) | Module 10 (Silver) |
| 3 | `ros2 launch workshop_arm workshop.launch.py stage:=3` | Bins, blocks at **random** spots, an overhead camera and a block detector | Modules 11–12 (Gold) |

Then, in a second terminal:

```bash
ros2 run workshop_arm demo          # stage 2: sorts the blocks using their known positions
ros2 run workshop_arm vision_demo   # stage 3: finds the blocks with the camera, then sorts them
```

Two windows open:

- **SO-101 simulation**: the place to *watch*. A live 3D view of the arm and table and, in
  stage 3, what the overhead camera sees (with the blocks the detector found).
- **RViz**: the place to *plan* and peek inside ROS. Drag the marker on the gripper and click
  **Plan & Execute**, or look at coordinate frames (TF). RViz shows what MoveIt *thinks*;
  it updates a little less smoothly than the simulation window.

Launch options:

| Option | What it does |
|---|---|
| `blocks:=8` | How many random blocks in stage 3 |
| `seed:=42` | The same random layout every time (handy for debugging) |
| `camera:=true` | Turn the overhead camera on in stage 1 or 2 (it's on by default in stage 3) |
| `detector:=false` | Stage 3 without our block detector, so you can run your own |
| `rviz:=false` | Don't open RViz (lighter on slow laptops; you lose drag-to-plan) |
| `view:=false` | Don't open the simulation window |

## Writing your own code

```python
from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')                     # saved poses: 'rest', 'zero', 'extended', 'look'
arm.move_joints(0, -45, 90, 45, 0)    # 5 joint angles, in degrees
arm.move_to(0.25, 0.0, 0.10)          # gripper position in meters (x forward, y left, z up)
arm.open_gripper()
arm.close_gripper()
print(arm.where_am_i())               # current gripper position (x, y, z)

arm.add_bin('red_bin', 0.12, 0.22, color='red')       # put things on the table
arm.add_block('my_block', 0.25, -0.05, color='red')
arm.grab()        # True if a block is between the fingers (it then moves with the arm)
arm.release()     # drops it below the gripper
arm.shutdown()
```

Save it as `my_first_robot.py` and, in a terminal set up as in
[Every new terminal](#every-new-terminal), run `python my_first_robot.py` while a simulation
is running.

## How it works

```
                      MoveIt (plans)  -->  ros2_control (moves the simulated motors)
                           ^                         |
                           |                  /follower/joint_states
                    workshop_arm.Arm                 |
                           ^                         v
 vision_demo  <--/detected_blocks--  block_detector  <--/camera/image_raw--  sim_view
 (look, pick,                        (OpenCV: color mask,                    (draws the arm and
  place, repeat)                      shapes, pixels -> meters)               table with MuJoCo)
```

- **MoveIt** plans collision-free motions; **ros2_control** runs the (simulated) motors.
  Switching to a real SO-101 later is one setting (`hardware_type:=real`); your code stays the same.
- **`sim_view`** draws the world with [MuJoCo](https://mujoco.org) about 15 times per second.
  It builds the arm from the same robot description MoveIt and RViz use, copies the joint angles
  onto it every frame, and shows the blocks and bins where MoveIt says they are. In stage 3 it
  also takes the overhead camera's pictures. The arm, and anything it holds, are in those
  pictures, just like with a real camera.
- **`block_detector`** finds blocks in the camera picture. The vision code is in
  `workshop_arm/vision.py`. It's plain OpenCV, so the same functions work on a real webcam.

## What's in here

| Path | What it is |
|---|---|
| `pixi.toml` | Everything we install (ROS 2, MoveIt, MuJoCo, OpenCV...) |
| `colcon_defaults.yaml` | Default `colcon build` options (used automatically inside `pixi shell`) |
| `scripts/setup_workspace.py` | Downloads the SO-101 packages and adapts them for the workshop |
| `CURRICULUM.md` | The lesson plan |
| `src/workshop_arm/workshop_arm/arm.py` | The beginner-friendly `Arm` helper |
| `src/workshop_arm/workshop_arm/table.py` | Table layout: bins, known blocks (stage 2), random block area (stage 3), camera |
| `src/workshop_arm/workshop_arm/vision.py` | Block detection with OpenCV (no ROS) |
| `src/workshop_arm/workshop_arm/demo.py` | Stage 2 example: sort blocks at known positions |
| `src/workshop_arm/workshop_arm/vision_demo.py` | Stage 3 example: find blocks with the camera and sort them |
| `src/workshop_arm/workshop_arm/sim_view.py` | The simulation window and overhead camera (MuJoCo) |
| `src/workshop_arm/workshop_arm/block_detector.py` | ROS node that runs `vision.py` on the camera pictures |
| `src/workshop_arm/workshop_arm/spawn_blocks.py` | Puts bins and blocks on the table |
| `src/workshop_arm/launch/workshop.launch.py` | Starts the simulation for a given stage |
| `src/so101-ros-physical-ai/` | SO-101 robot model, controllers and MoveIt config, downloaded by setup ([upstream](https://github.com/esol-community/so101-ros-physical-ai)) |

## Troubleshooting

| Problem | Try this |
|---|---|
| `ros2: command not found` | Run `pixi shell` first (in the `so101-arm-workshop` folder). |
| `Package 'workshop_arm' not found` | Run `source install/setup.bash` (after every `colcon build`, too). |
| `MoveIt is not running. Did you start the launch file?` | Start a simulation in another terminal first and wait for RViz / the simulation window to appear. |
| `No block there` / `Missed!` | Is the right stage running? `demo` needs `stage:=2`, `vision_demo` needs `stage:=3`. |
| Everything is slow | Close other apps, or add `rviz:=false`. |
| Leftover windows or nodes from an earlier run | Close all terminals, then run `ros2 daemon stop` in a fresh one. |
| Windows: errors about long paths | Move the folder to a short path like `C:\so101`. |

## Notes for instructors

- Upstream uses the `pick_ik` IK solver, which is Linux-only on RoboStack, so setup switches to
  KDL with position-only IK (the SO-101 has only 5 joints).
- `moveit_py` is not available on Windows, so `workshop_arm` talks to MoveIt with plain ROS 2 actions.
- The robot packages are patched to `LANGUAGES NONE` and built with Ninja, so no C++ compiler
  (or Visual Studio) is needed.
- MuJoCo is used only to draw (no physics); it installs from conda-forge on every OS, unlike
  Gazebo. Blocks attach to the gripper by rule: `grab()` only succeeds if a block is within 2 cm,
  so bad perception shows up as a miss. On real hardware, `sim_view`'s camera is replaced by a
  webcam driver.
- Blocks are allowed to collide with everything in MoveIt (the gripper must touch them); bins
  are real obstacles.
- If your own `~/.bashrc` sources another ROS install (e.g. Humble), start from a clean shell first:
  `env -i HOME=$HOME PATH=/usr/bin:/bin:$HOME/.pixi/bin DISPLAY=$DISPLAY TERM=$TERM bash --noprofile --norc`
