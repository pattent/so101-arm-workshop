"""Exercise 1: lists, many values in one variable.

Run:  python ex1_lists.py   (no robot needed)
"""

# A list holds many values, in order, inside [ ] and separated by commas.
joints = ['shoulder_pan', 'shoulder_lift', 'elbow_flex', 'wrist_flex', 'wrist_roll']
print(joints)
print('The arm has', len(joints), 'joints')    # len = how many items

# Every item has a number, its INDEX. Counting starts at 0, not 1!
print('The first joint is', joints[0])
print('The second joint is', joints[1])
print('The last joint is', joints[-1])          # negative numbers count from the end
print('The first three are', joints[0:3])       # a "slice": items 0, 1 and 2

# TODO 1: Print elbow_flex using its index. Which number is it?

# TODO 2: Try print(joints[5]). Read the LAST line of the error. Why is there no joint 5?


# Lists can change.
angles = [0, -45, 45, 45]
angles.append(0)            # append adds an item to the end
print('Angles:', angles)
angles[0] = 30              # change one item, by its index
print('After turning:', angles)
print('Biggest:', max(angles), ' smallest:', min(angles), ' total:', sum(angles))

# TODO 3: The arm also has a gripper. Add 'gripper' to the end of joints, then print how
#         many items joints has now.

# TODO 4: `in` checks whether something is in a list, and gives back a bool (True or False).
#         Print 'elbow_flex' in joints. Then try 'knee' in joints.


# A tuple is like a list, but in ( ) and it can't change. Use one for values that belong
# together, like a point: x, y and z.
point = (0.25, 0.10, 0.15)
print('x is', point[0])
x, y, z = point             # "unpacking": three variables in one line
print(f'x={x} y={y} z={z}')

# TODO 5: Try point[0] = 0.30. What does the error say?

# TODO 6: Lists can hold tuples. Make a list called points with three (x, y, z) points.
#         Print the second point, then just its z. (Hint: points[1] is a tuple, so
#         points[1][2] is the third number inside it.)
