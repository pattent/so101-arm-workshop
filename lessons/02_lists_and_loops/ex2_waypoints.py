"""Exercise 2: for loops, one step for each item in a list.

Run (with the stage 1 simulation running):  python ex2_waypoints.py
"""

from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')

# A list of points for the gripper to visit: (x, y, z) in meters.
# x = forward, y = left, z = up.
waypoints = [
    (0.25, 0.00, 0.15),
    (0.25, 0.10, 0.15),
]

# A for loop runs the indented lines once for each item in the list.
for point in waypoints:
    x, y, z = point                 # "unpack" the tuple into three variables
    print(f'Going to x={x} y={y} z={z}')
    arm.move_to(x, y, z)

# TODO 1: Add two more points to the list, so the gripper visits four places.

# TODO 2: How many points are in the list? Print len(waypoints).

# TODO 3: Visit the points in reverse order. (Hint: reversed(waypoints))

arm.go_to('rest')
arm.shutdown()
