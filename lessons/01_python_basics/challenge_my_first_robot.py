"""Challenge: move the robot!

First start the simulation in another terminal:
    ros2 launch workshop_arm workshop.launch.py stage:=1
Then run:
    python challenge_my_first_robot.py

arm.move_joints(shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll)
sets all five joints, in degrees:

    shoulder_pan    turns the whole arm. Positive turns it to its RIGHT.
    shoulder_lift   tips the arm forward / back.
    elbow_flex      bends the elbow.
    wrist_flex      tips the wrist up / down.
    wrist_roll      twists the gripper.

If a pose is impossible (out of reach, or the arm would hit itself or the table),
the arm stays put and prints a message. That's fine: try different numbers!
"""

# workshop_arm is our own package (in src/workshop_arm/). Like `import math`, but this
# takes just one thing out of it: the Arm class.
from workshop_arm import Arm

arm = Arm()     # make the robot object (exercise 4), which connects to the simulation

print('Going to the rest pose...')
arm.go_to('rest')                      # a method, with one input: the pose's name

# This pose works. Watch where the arm goes.
arm.move_joints(0, -45, 45, 45, 0)     # a method with five inputs, in order (see above)
# where_am_i gives back three numbers: the gripper's x, y and z, in meters.
print('The gripper is now at', arm.where_am_i())

# TODO 1: Make the arm turn to its LEFT. (Which joint? Positive or negative?)

# TODO 2: Make the arm point straight up. (Hint: try shoulder_lift = -90 with the
#         elbow and wrist straight.)

# TODO 3: Invent your own pose. Print where the gripper ended up.

# Bonus: write a function show_pose(arm, pan) that moves the arm to
#        (pan, -45, 45, 45, 0) and prints where the gripper is. A function's input can be
#        the robot itself! Call it three times: with -60, 0 and 60.

arm.go_to('rest')
arm.shutdown()                         # disconnect from the simulation
