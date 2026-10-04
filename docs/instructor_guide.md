# Instructor guide

How to run the sessions. The lessons themselves are in [`lessons/`](../lessons/).

## Before the first session

- [ ] Find out her operating system (Windows, Mac with Intel, or Mac with Apple Silicon).
- [ ] If possible, do the install on her laptop **before** the session, or plan the first hour
      around it: `pixi install` downloads ~6 GB. On a slow connection that alone can take a while.
- [ ] Have your own machine ready as a backup, with `stage:=3` running, so the session can go on
      even if her install hits a snag.
- [ ] Skim the lesson's `README.md` and its `solutions/` folder.

**Windows and macOS have not been tested on a real machine yet.** Expect the first install to be
where problems show up. Write down any error exactly; it's probably a small fix.

## Rough timing

These are guesses. Go at her pace; it's fine to split a lesson or merge two.

| Lesson | Estimate | Notes |
|---|---|---|
| 0 Kickoff | 60–90 min | Mostly the install. The demo and "what do you want to build?" chat take ~20 min. |
| 1 Python basics | 45–60 min | Exercises 1–3 need no robot; the challenge moves the arm. Read the "functions" and "What is `workshop_arm`?" boxes together before the challenge. |
| 2 Loops and functions | 60–75 min | First time writing functions (`def`/`return`, no robot), then the wave. The circle (cos/sin) may need a whiteboard sketch. |
| 3 Decisions and classes | 60–90 min | Reading `arm.py` together is the big one; the Bronze dance can be homework. |
| 4–12 | ~60–90 min each | Starter files still to be written; estimate after we see how 0–3 go. |

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
  write Lessons 4–12.
- If she wants to change direction (a different project than block sorting), the toolkit
  (`Arm`, stages, camera) still applies; only the later lessons change.
