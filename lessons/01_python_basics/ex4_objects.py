"""Exercise 4: objects and classes.

The challenge starts with these lines:
    arm = Arm()
    arm.move_joints(0, -45, 45, 45, 0)
    print(arm.where_am_i())
This exercise shows what they mean, using a simple simulated Mars rover.

Run:  python ex4_objects.py   (no robot needed)
"""

# Part 1: objects. Some values come with their own functions, called with a dot.
# A value like that is an "object", and its functions are called "methods".
robot_name = 'so-101'
print(robot_name.upper())            # text knows how to make itself UPPERCASE
print(robot_name.replace('-', ' '))  # ...and how to swap one thing for another

# TODO 1: Try robot_name.title(). What does it do?


# Part 2: a class is a blueprint for making objects. Here's one for a rover that
# drives along a straight line. Read it line by line: it's built from things you already
# know, variables and functions.
class Rover:

    # __init__ is a function that runs once, when a new rover is made.
    # `self` means "this rover". Variables stored on self (called "attributes") are what
    # the rover remembers about itself.
    def __init__(self, name):
        self.name = name
        self.position = 0           # meters from where it started

    # Every other function in the class (a "method") is something the rover can do.
    # It always gets `self` first, so it can use and change the rover's own attributes.
    def report(self, message):
        print(f'{self.name}: {message}')

    def drive(self, meters):
        self.position = self.position + meters
        print(f'{self.name} drives {meters} m, to {self.position} m.')

    def where_am_i(self):
        return self.position


# Calling the class like a function makes one new rover: an object.
curiosity = Rover('Curiosity')  # Rover (capital R) is the blueprint; curiosity is one rover
curiosity.report('Systems online.')   # call a method: the object, a dot, the method, its inputs
curiosity.drive(3)
print('Curiosity is at', curiosity.where_am_i())    # a method that gives back an answer
print('Curiosity is at', curiosity.position)        # an attribute: no parentheses

# TODO 2: Make a second rover named 'Perseverance'. Have it report something, and drive it
#         4 m. Print both rovers' positions. Did driving one rover move the other?

# TODO 3: Give Rover a battery. In __init__, add an attribute:  self.battery = 100
#         Then make drive use some battery: add a line that takes away 5 (percent) for
#         every meter driven. Drive curiosity and print curiosity.battery.

# TODO 4: Add a method recharge(self) that sets the battery back to 100 and reports it
#         (copy the pattern of `report`). Call it on curiosity and print the battery again.


# The robot arm works exactly the same way:
#     arm = Arm()                         Arm is the class; arm is your robot (an object)
#     arm.move_joints(0, -45, 45, 45, 0)  a method with five inputs
#     arm.where_am_i()                    a method that gives back an answer
#     arm.speed                           an attribute
