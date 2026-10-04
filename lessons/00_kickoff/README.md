# Lesson 0: Kickoff, "Here's where we're going"

**Goal:** see what the robot will be able to do by the end, get everything installed on your
laptop, and decide what *you* want to build.

## 1. See the finish line

In one terminal (set up as in the [main README](../../README.md#every-new-terminal)):
```bash
ros2 launch workshop_arm workshop.launch.py stage:=3
```
In a second terminal:
```bash
ros2 run workshop_arm vision_demo
```

Watch the **SO-101 simulation** window. Blocks are scattered at random. The camera finds them,
and the arm sorts each one into the bin of the same color. Nobody told it where the blocks are.

By the end of this workshop, you'll have written your own version of this.

## 2. Play

- In **RViz**, drag the colored ball and arrows on the gripper, then click **Plan & Execute**.
  Watch the arm move in the simulation window too.
- Run `vision_demo` again with a different number of blocks:
  stop the simulation (`Ctrl+C`), restart it with `blocks:=8`, and run the demo again.

## 3. Install it on your laptop

Follow the [setup steps](../../README.md#setup-one-time-about-10-minutes). You're done when
you can run step 1 above on your own machine.

## 4. The three commands you'll use every session

```bash
pixi shell                     # 1. turn on ROS 2
source install/setup.bash      # 2. load our workspace
ros2 launch workshop_arm workshop.launch.py stage:=1    # 3. start the simulation
```
(On Windows, step 2 is `install\local_setup.ps1` in PowerShell, or `call install\local_setup.bat` in
Command Prompt.)

## 5. Talk about it

- What surprised you about how the robot works?
- What would *you* want a robot arm to do? Sorting blocks is our plan, but if you have a better
  idea, now's the time to say so.
- Where do you think robot arms like this are used in the real world?

**Next:** [Lesson 1: Python basics](../01_python_basics/)
