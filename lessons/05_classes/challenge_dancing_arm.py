"""Challenge: a DancingArm class.

Turn your Bronze dance from Lesson 4 into a class: a DancingArm is an Arm that knows how
to dance. Then dancing is just:

    dancer = DancingArm()
    dancer.perform(['up', 'lean_left', 'wave', 'lean_right', 'clap', 'bow'])

Run (with the stage 1 simulation running):  python challenge_dancing_arm.py

Steps:
  1. In __init__, call super().__init__() first, then store your dictionary of named poses
     in self.moves (copy it from your Bronze dance).
  2. Turn the moves that repeat (wave, clap...) into methods: def wave(self, times).
     Inside the class, the arm is `self`: self.move_joints(...), self.open_gripper().
  3. Write perform(self, choreography): for each name in the list, if it's a pose in
     self.moves, move there; if it's 'wave' or 'clap', call that method; otherwise print
     that you don't know that move, and carry on.
  4. Make a DancingArm, and perform your dance.

Bonus: add a method learn(self, name, angles) that adds a new pose to self.moves, and use it
before performing.
"""

from workshop_arm import Arm


class DancingArm(Arm):

    def __init__(self):
        super().__init__()
        # TODO 1: self.moves = { ... }

    # TODO 2: def wave(self, times):

    # TODO 3: def perform(self, choreography):


# TODO 4
dancer = DancingArm()
dancer.go_to('rest')

dancer.go_to('rest')
dancer.shutdown()
