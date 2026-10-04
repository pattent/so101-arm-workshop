# Lesson 11: Packages and launch files

**Goal:** understand the commands you've typed since Lesson 0, then use them on your own code.
How does `ros2 run workshop_arm demo` find the demo? What do `colcon build` and
`source install/setup.bash` actually do? How does one `ros2 launch` start a dozen programs?
By the end, your safety monitor from Lesson 10 will be a proper ROS **package** with its own
**launch file**.

| Word | Means |
|---|---|
| **package** | a folder of ROS code with a name (`workshop_arm`, `turtlesim`); the unit you build, share and run |
| **workspace** | a folder of packages: ours is `so101-arm-workshop`, with packages in `src/` |
| **`colcon build`** | builds every package in `src/` and installs it into `install/` |
| **`source install/setup.bash`** | tells this terminal where `install/` is, so `ros2 run` and `import` can find things |
| **launch file** | a Python file that starts many nodes at once, with settings |
| **parameter** | a setting a node reads when it starts, like `min_height` |

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1` (exercises 3 and 4)

Run every command in this lesson from the workspace folder (`so101-arm-workshop`), unless it
says `cd src`.

## Exercises (together)

### 1. Where does `ros2 run workshop_arm demo` come from?

Follow the trail, in [`src/workshop_arm/`](../../src/workshop_arm/):
```bash
ros2 pkg list                      # every package ROS knows about (look for workshop_arm)
ros2 pkg executables workshop_arm  # the programs it has
ros2 pkg prefix workshop_arm       # where it's installed (inside install/)
```
- Open [`package.xml`](../../src/workshop_arm/package.xml): the package's name, and the other
  packages it needs.
- Open [`setup.py`](../../src/workshop_arm/setup.py) and find `console_scripts`. The line
  `'demo = workshop_arm.demo:main'` means: *"the program `demo` runs the function `main` in
  `workshop_arm/demo.py`."* Find that `main`.
- Which line in `setup.py` installs the launch file?

So: `colcon build` copies the package into `install/` and makes a little `demo` program there;
`source install/setup.bash` adds `install/` to this terminal's search paths; and `ros2 run`
looks the program up by package name. That's also why you rebuild after changing `arm.py`:
the copy in `install/` doesn't change by itself.

### Where does everything else come from? Environments

Your package uses Python, ROS, OpenCV and NumPy, but you never installed them one by one.
`pixi install` downloaded them all into a hidden folder, `.pixi/`, in the workspace, and
`pixi shell` switches this terminal over to that copy. That's a **virtual environment**: a
separate box of software for one project, so it can't clash with anything else on the
computer, and it's the same on every laptop. (Other Python projects use tools called `venv` or
`conda` for the same job.)

Two rules follow from that:
- If a terminal says `ros2: command not found` or `No module named 'cv2'`, you probably forgot
  `pixi shell`: that terminal isn't in the box.
- Don't `pip install` things into it on your own. Ask first: the right way is to add the library
  to `pixi.toml`, so everyone's box stays the same.

### 2. Make your own package

```bash
cd src
ros2 pkg create --build-type ament_python --license MIT --node-name hello my_robot
cd ..
colcon build
source install/setup.bash          # on Windows: the same line you use in every new terminal
ros2 run my_robot hello
```
Look at what was made in `src/my_robot/`: a `package.xml`, a `setup.py` with a
`console_scripts` line for `hello`, and `my_robot/hello.py`. Change the message in `hello.py`.
Does `ros2 run my_robot hello` show the change? What do you need to do first?

### 3. Move your safety monitor in, with a parameter

1. Copy your `challenge_safety_monitor.py` from Lesson 10 to
   `src/my_robot/my_robot/safety_monitor.py`.
2. In `src/my_robot/setup.py`, add a `console_scripts` line, next to `hello`:
   `'safety_monitor = my_robot.safety_monitor:main',`
3. Make `MIN_HEIGHT` a **parameter**, so it can be changed without editing code. In `__init__`:
   ```python
   self.declare_parameter('min_height', 0.03)               # name, and the default value
   self.min_height = self.get_parameter('min_height').value
   ```
   and use `self.min_height` instead of `MIN_HEIGHT`.
4. Swap `print(...)` for the node's **logger**: `self.get_logger().info('...')` for normal
   messages and `self.get_logger().warning('...')` for warnings. Log messages get a level and
   a timestamp, and (unlike `print`) they show up right away when the node is started from a
   launch file, which you'll do in exercise 4.
5. Build, source, and run it, first normally, then with a different setting:
   ```bash
   colcon build
   source install/setup.bash
   ros2 run my_robot safety_monitor
   ros2 run my_robot safety_monitor --ros-args -p min_height:=0.05
   ```

### 4. Launch files

First, read ours: [`workshop.launch.py`](../../src/workshop_arm/launch/workshop.launch.py).
Skip the `OpaqueFunction` details and look at what `setup` puts in `actions`.
- Which nodes start in stage 1? In stage 3?
- What does `rviz:=false` change? What about `detector:=false`?
- `stage:=3` is a **launch argument**. Where is it declared, with its default?

Now write your own, [`safety.launch.py`](safety.launch.py):
1. Copy it into a new folder `src/my_robot/launch/`, and follow its `TODO`s.
2. Tell `setup.py` to install launch files. Add `from glob import glob` at the top, and this
   line inside `data_files=[...]`:
   ```python
   ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
   ```
3. Build, source, and try:
   ```bash
   ros2 launch my_robot safety.launch.py min_height:=0.05
   ```

## Challenge (on your own)

**[`everything.launch.py`](everything.launch.py): one command for everything.** A launch file
that starts the whole simulation *and* your safety monitor, by **including** two other launch
files. Then this starts your whole robot:
```bash
ros2 launch my_robot everything.launch.py stage:=2 min_height:=0.05
```
Test it: in another terminal, `ros2 run workshop_arm demo` grabs blocks at 1.5 cm, so your
monitor should complain.

The finished package is in [`solutions/my_robot/`](solutions/my_robot/). (The `COLCON_IGNORE`
file in `solutions/` stops `colcon build` from building it, so it can't clash with yours.)

## Things to remember

| Idea | Example |
|---|---|
| Make a Python package | `cd src`, then `ros2 pkg create --build-type ament_python --node-name hello my_robot` |
| Build everything (from the workspace folder) | `colcon build` |
| Build just one package | `colcon build --packages-select my_robot` |
| Rebuild after **every** change, then source | `colcon build`, then `source install/setup.bash` |
| A program name → a Python function | `'safety_monitor = my_robot.safety_monitor:main'` in `setup.py` |
| What a package needs | `<exec_depend>rclpy</exec_depend>` in `package.xml` |
| Declare and read a parameter | `self.declare_parameter('min_height', 0.03)` |
| Set a parameter with `ros2 run` | `--ros-args -p min_height:=0.05` |
| Log instead of `print` in nodes | `self.get_logger().info('hi')`, `self.get_logger().warning('careful')` |
| Start a node from a launch file | `Node(package='my_robot', executable='safety_monitor')` |
| A launch argument | `DeclareLaunchArgument('stage', default_value='1')` and `stage:=2` |
| Run another launch file | `IncludeLaunchDescription(...)` |

**Next:** [Lesson 12: Robot models and TF](../12_robot_models_and_tf/)
