"""Solution: Exercise 1."""

joints = ['shoulder_pan', 'shoulder_lift', 'elbow_flex', 'wrist_flex', 'wrist_roll']
print(joints)
print('The arm has', len(joints), 'joints')
print('The first joint is', joints[0])
print('The second joint is', joints[1])
print('The last joint is', joints[-1])
print('The first three are', joints[0:3])

# TODO 1: counting from 0, elbow_flex is item 2.
print(joints[2])

# TODO 2: joints[5] fails with  IndexError: list index out of range.
# There are 5 items, numbered 0 to 4, so the last one is joints[4].

angles = [0, -45, 45, 45]
angles.append(0)
print('Angles:', angles)
angles[0] = 30
print('After turning:', angles)
print('Biggest:', max(angles), ' smallest:', min(angles), ' total:', sum(angles))

# TODO 3
joints.append('gripper')
print('Now there are', len(joints), 'items')

# TODO 4
print('elbow_flex' in joints)   # True
print('knee' in joints)         # False

point = (0.25, 0.10, 0.15)
print('x is', point[0])
x, y, z = point
print(f'x={x} y={y} z={z}')

# TODO 5: point[0] = 0.30 fails with
#     TypeError: 'tuple' object does not support item assignment

# TODO 6
points = [(0.25, 0.10, 0.15), (0.30, -0.05, 0.10), (0.20, 0.00, 0.20)]
print('The second point is', points[1])
print('Its z is', points[1][2])
