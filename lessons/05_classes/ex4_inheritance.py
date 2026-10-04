"""Exercise 4: build on someone else's class (inheritance).

`class ChattyArm(Arm):` means "a ChattyArm is an Arm, plus some extras". It gets every
method Arm has for free (move_to, go_to, grab...), and you can add new ones or change old
ones. You'll see this again in Lesson 10: every ROS 2 program starts with
`class SomethingNode(Node):`.

Run (with the stage 1 simulation running):  python ex4_inheritance.py
"""

from workshop_arm import Arm


class ChattyArm(Arm):
    """An Arm that says what it's doing, and counts its moves."""

    def __init__(self, name):
        # super() means "the class I'm built on" (Arm). Let Arm set itself up first
        # (connect to MoveIt and so on), then add our own extras.
        super().__init__()
        self.name = name
        self.moves = 0

    # A new method that only ChattyArm has.
    def say(self, message):
        print(f'{self.name}: {message}')

    # This REPLACES Arm's go_to with our own version...
    def go_to(self, pose_name):
        self.say(f'Going to {pose_name}!')
        self.moves += 1
        # ...which still asks the original go_to to do the actual moving,
        # and passes its answer (True or False) back.
        return super().go_to(pose_name)


arm = ChattyArm('Atlas')
arm.go_to('rest')
arm.go_to('zero')
arm.say(f'I have moved {arm.moves} times.')

# TODO 1: Give your arm a different name. Add arm.go_to('extended') and check the count.

# TODO 2: Add a method nod(self, times) to ChattyArm that says "Yes!" and tips the wrist
#         down and up `times` times. Count each nod as a move.
#         (Hint: self.move_joints(0, -45, 45, 20, 0), then self.move_joints(0, -45, 45, 70, 0).
#         Inside the class, the arm is `self`, not `arm`.)

# TODO 3: Replace move_to too, so it says where it's going before it moves:
#             def move_to(self, x, y, z):
#         Test it with arm.move_to(0.25, 0.0, 0.10).
#         Then delete the word `return` in front of super().move_to(...) and run
#         print(arm.move_to(0.25, 0.0, 0.10)). What gets printed, and why?

arm.go_to('rest')
arm.shutdown()
