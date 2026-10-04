"""Solution: Exercise 2."""

from workshop_arm import Arm

arm = Arm()
arm.go_to('rest')

waypoints = [
    (0.25, 0.00, 0.15),
    (0.25, 0.10, 0.15),
    (0.30, 0.10, 0.10),   # TODO 1
    (0.30, -0.10, 0.10),  # TODO 1
]

for point in waypoints:
    x, y, z = point
    print(f'Going to x={x} y={y} z={z}')
    arm.move_to(x, y, z)

# TODO 2
print('Number of points:', len(waypoints))

# TODO 3
for point in reversed(waypoints):
    x, y, z = point
    print(f'Going back to x={x} y={y} z={z}')
    arm.move_to(x, y, z)

arm.go_to('rest')
arm.shutdown()
