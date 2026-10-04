# Instructor guide

How to run the sessions. The lessons themselves are in [`lessons/`](../lessons/).

## Before the first session

- [ ] Find out her operating system (Windows, Mac with Intel, or Mac with Apple Silicon).
- [ ] Find out which math she's had. The lessons assume Algebra 1 and Geometry (Pythagoras,
      coordinates). Lesson 2's circle uses right-triangle trig (SOH-CAH-TOA), which some
      tenth graders haven't met yet; if so, plan 10 minutes on it before that challenge.
      Radians, the law of cosines and the camera math are explained in the lessons themselves.
- [ ] If possible, do the install on her laptop **before** the session, or plan the first hour
      around it: `pixi install` downloads ~6 GB. On a slow connection that alone can take a while.
- [ ] Have your own machine ready as a backup, with `stage:=3` running, so the session can go on
      even if her install hits a snag.
- [ ] Skim the lesson's `README.md` and its `solutions/` folder.

**Windows has been installed on one laptop so far, and macOS not at all yet.** Expect the first install to be
where problems show up. Write down any error exactly; it's probably a small fix.

## Rough timing

These are guesses. Go at her pace; it's fine to split a lesson or merge two.

| Lesson | Estimate | Notes |
|---|---|---|
| 0 Kickoff | 60–90 min | Mostly the install. The demo and "what do you want to build?" chat take ~20 min. |
| 1 Python basics | 75–90 min | Four exercises, none need the robot; the challenge moves the arm. Read the "Functions" box before ex2 and the "Objects" box before ex4. She *writes* small functions (`to_degrees`, `distance_from_base`, `can_reach`) and *extends* a class (`Rover`: a battery attribute and a `recharge` method), but writing whole classes waits for Lesson 5. The challenge touches each main idea once on the real arm (a variable and f-string, the `speed` attribute, `move_to` returning a `bool` vs her own `can_reach`), and nothing it uses is new; the bonus (a function that takes `arm`) ties functions and objects together. |
| 2 Lists and loops | 60–75 min | Indexing from 0 is the classic stumble: let her hit the `IndexError` in ex1. The circle challenge explains cos/sin with a right-triangle picture; sketch it on paper together, and work out one point (30°) by hand before running it. |
| 3 Functions | 60–75 min | Builds on her Lesson 1 functions: default values, returning a tuple (`point_on_circle`, reused in the shapes challenge), functions on lists. Ex3 gives a one-line preview of `if`, which Lesson 4 covers properly. |
| 4 Decisions and dictionaries | 60–90 min | Ex2 uses the real `BINS` from `table.py`. The Bronze dance can be homework. |
| 5 Classes | 75–90 min | Reading `arm.py` together (ex3) is the big one: it's long, so stick to the questions. The `DancingArm` challenge reuses her Bronze dance. |
| 6 Python for robots | 60–75 min | No robot, on purpose. Callbacks (ex1) are the big idea: everything in Lesson 10 depends on it, so don't rush it. The challenge works as homework. |
| 9 Nodes and topics | 60 min | All command line, three or four terminals at once: arrange the windows before starting. Answers in `solutions/answers.md`. |
| 10 Writing nodes | 75–90 min | Compare each node with the "shape of every node" box in the README. Nodes run until `Ctrl+C`: say so up front. |
| 11 Packages and launch files | 75–90 min | The student creates `src/my_robot/` in the workspace. Rebuild-and-source after every change is the usual stumble. |
| 7–8, 12–16 | ~60–90 min each | Starter files still to be written; estimate after we see how the finished lessons go. |

## Running a session

1. **Start the simulation first** (the stage is at the top of each lesson's README), in its own
   terminal. Keep it running the whole session.
2. **Second terminal** for her code: `pixi shell`, `source install/setup.bash`, `cd` into the
   lesson folder.
3. **Together exercises:** let her type. Read errors out loud together; most are typos or
   indentation.
4. **Challenge:** she tries alone, you're there if stuck. Solutions are for *after* trying.
5. **End with a show-off:** run whatever she made, and note how long the lesson actually took.

## When things go wrong

| Symptom | Fix |
|---|---|
| `MoveIt is not running` | The simulation isn't running (or is still starting up). |
| `Too far!` / `MoveIt could not do that` | Not a bug: the point is out of reach or would hit something. Great teaching moment. |
| Nothing moves, no error | Is the second terminal set up (`pixi shell`, `source install/setup.bash`)? |
| `IndentationError` | Mixed spaces/tabs, or a line not lined up. Use 4 spaces. |
| Everything is slow | Close other apps; restart with `rviz:=false`. |
| Weird leftover behavior | Close all terminals, then `ros2 daemon stop`, and start again. |

More in the main [README troubleshooting table](../README.md#troubleshooting).

## After each session

- Note what took longer or shorter than expected, and what she enjoyed. That decides how we
  write the remaining lessons.
- If she wants to change direction (a different project than block sorting), the toolkit
  (`Arm`, stages, camera) still applies; only the later lessons change.
