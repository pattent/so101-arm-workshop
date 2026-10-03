# SO-101 Robot Arm Workshop

Learn Python, ROS 2 and robot arm programming with a simulated SO-101 arm.
Runs natively on **Windows, macOS or Linux**: no virtual machine needed.

We use [pixi](https://pixi.sh) only to **install** ROS 2 Jazzy (it's the official way to install
ROS 2 on Windows). After that, everything is the standard ROS 2 workflow: `source`,
`colcon build`, `ros2 launch`, `ros2 run`.

## 1. Install pixi (one time)

**macOS / Linux** (Terminal):
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows** (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Then close and reopen your terminal.

> **Windows:** put this folder somewhere with a short path, like `C:\so101`. Windows has
> trouble with very long file paths.

## 2. Download this workshop

```bash
pixi global install git    # only if you don't already have git
git clone https://github.com/pattent/so101-arm-workshop.git
cd so101-arm-workshop
```

## 3. Install ROS 2 and set up the workspace (one time, ~5 minutes, ~6 GB)

From inside this folder:
```bash
pixi install                        # downloads ROS 2 Jazzy, MoveIt 2, RViz, OpenCV...
pixi shell                          # turns on ROS 2 in this terminal
python scripts/setup_workspace.py   # downloads the SO-101 robot packages
colcon build                        # builds the workspace
```

## 4. Every new terminal

```bash
cd so101-arm-workshop
pixi shell                     # ROS 2 Jazzy (like `source /opt/ros/jazzy/setup.bash`)
source install/setup.bash      # our workspace   (Windows: call install\setup.bat)
```

Re-run the `source` line after every `colcon build`.

## 5. See the robot move

Terminal 1: start the simulated arm, controllers, MoveIt and RViz:
```bash
ros2 launch so101_bringup follower_moveit_demo.launch.py hardware_type:=mock
```

Terminal 2: sort a red and a blue block into matching bins:
```bash
ros2 run workshop_arm demo
```

Then try dragging the arm's marker in RViz and clicking **Plan & Execute**.

## 6. Let the robot find the blocks itself (perception)

In `demo`, we typed in where the blocks are. Here a (simulated) overhead camera
looks at the table, OpenCV finds the blocks, and the arm sorts whatever it sees.

Terminal 1: arm + MoveIt + RViz + camera + block detector + a camera viewer window:
```bash
ros2 launch workshop_arm perception_sim.launch.py
```

Terminal 2: scatter blocks at random spots, then sort them using only the camera:
```bash
ros2 run workshop_arm spawn_blocks        # 5 random blocks (try: spawn_blocks 8)
ros2 run workshop_arm vision_demo
```

How it fits together:
```
sim_camera  --/camera/image_raw-->  block_detector  --/detected_blocks-->  vision_demo  -->  MoveIt  -->  arm
(draws the table                    (OpenCV: color mask,                    (look, pick,
 from above)                         contours, pixel -> meters)              place, repeat)
```

The camera viewer shows `/vision/debug_image`: what the detector found, with each
block's position on the table. The detector code is in `workshop_arm/vision.py`.
It's plain OpenCV, so the same functions work on a real webcam picture.

## Writing your own code

```python
from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')                     # saved poses: 'rest', 'zero', 'extended'
arm.move_joints(0, -45, 90, 45, 0)    # 5 joint angles, in degrees
arm.move_to(0.25, 0.0, 0.10)          # gripper position in meters (x forward, y left, z up)
arm.open_gripper()
arm.close_gripper()
print(arm.where_am_i())               # current gripper (x, y, z)

arm.add_bin('red_bin', 0.12, 0.22, color='red')       # objects show up in RViz
arm.add_block('my_block', 0.25, -0.05, color='red')
arm.grab()        # True if a block is between the fingers (it then moves with the arm)
arm.release()     # drops it below the gripper
arm.shutdown()
```

Save it as `my_first_robot.py` and run `python my_first_robot.py` (in a terminal set up
as in step 3) while the launch file is running.

## What's in here

| Path | What it is |
|---|---|
| `pixi.toml` | Everything we install (ROS 2, MoveIt, OpenCV...) |
| `colcon_defaults.yaml` | Default `colcon build` options (used automatically inside `pixi shell`) |
| `scripts/setup_workspace.py` | Downloads the SO-101 packages and adapts them for the workshop |
| `src/workshop_arm/workshop_arm/arm.py` | The beginner-friendly `Arm` helper |
| `src/workshop_arm/workshop_arm/table.py` | Workcell layout: bin positions, block area, camera position |
| `src/workshop_arm/workshop_arm/vision.py` | Block detection with OpenCV (no ROS) |
| `src/workshop_arm/workshop_arm/*.py` | Nodes: `sim_camera`, `block_detector`, `spawn_blocks`, `demo`, `vision_demo` |
| `src/so101-ros-physical-ai/` | SO-101 robot model, controllers and MoveIt config ([upstream](https://github.com/esol-community/so101-ros-physical-ai)) |

## Notes for instructors

- Simulated vs. real arm is one launch argument: `hardware_type:=mock` today, `hardware_type:=real`
  with a real SO-101. Student code does not change.
- Upstream uses the `pick_ik` IK solver, which is Linux-only on RoboStack, so setup switches to KDL
  with position-only IK.
- `moveit_py` is not available on Windows, so `workshop_arm` talks to MoveIt using plain ROS 2 actions.
- The robot packages are patched to `LANGUAGES NONE` and built with Ninja, so no C++ compiler
  (or Visual Studio) is needed.
- Simulated perception: `sim_camera` renders MoveIt's planning scene from above (pinhole model, with
  noise and blur) instead of using Gazebo, so it works on every OS. It does not draw the arm itself,
  so a held block simply disappears from view. On real hardware this node is swapped for a webcam driver.
- Blocks are allowed to collide with everything in MoveIt (the gripper must touch them); `grab()`
  only succeeds if a block is within 2 cm of the gripper, so bad perception shows up as a miss.
- If your own `~/.bashrc` sources another ROS install (e.g. Humble), start from a clean shell first:
  `env -i HOME=$HOME PATH=/usr/bin:/bin:$HOME/.pixi/bin DISPLAY=$DISPLAY TERM=$TERM bash --noprofile --norc`
