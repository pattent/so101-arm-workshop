"""Solution: Exercise 4."""

from workshop_arm import Arm


class ChattyArm(Arm):
    """An Arm that says what it's doing, and counts its moves."""

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.moves = 0

    def say(self, message):
        print(f'{self.name}: {message}')

    def go_to(self, pose_name):
        self.say(f'Going to {pose_name}!')
        self.moves += 1
        return super().go_to(pose_name)

    # TODO 2
    def nod(self, times):
        self.say('Yes!')
        for _ in range(times):
            self.move_joints(0, -45, 45, 20, 0)
            self.move_joints(0, -45, 45, 70, 0)
            self.moves += 1

    # TODO 3: without `return`, this would give back None instead of True/False,
    # so code that checks `if arm.move_to(...)` would think every move failed.
    def move_to(self, x, y, z):
        self.say(f'Heading to ({x}, {y}, {z})')
        self.moves += 1
        return super().move_to(x, y, z)


# TODO 1
arm = ChattyArm('Nova')
arm.go_to('rest')
arm.go_to('zero')
arm.go_to('extended')
arm.say(f'I have moved {arm.moves} times.')

arm.nod(3)
print('Did the move work?', arm.move_to(0.25, 0.0, 0.10))
arm.say(f'Now I have moved {arm.moves} times.')

arm.go_to('rest')
arm.shutdown()
