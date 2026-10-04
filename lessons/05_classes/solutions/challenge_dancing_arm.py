"""Solution: Challenge (including the bonus)."""

from workshop_arm import Arm


class DancingArm(Arm):

    def __init__(self):
        super().__init__()
        # TODO 1
        self.moves = {
            'up': [0, -90, 0, 0, 0],
            'lean_left': [-45, -60, 30, 20, 0],
            'lean_right': [45, -60, 30, 20, 0],
            'bow': [0, -20, 20, 70, 0],
            'twist': [0, -90, 0, 0, 90],
        }

    # TODO 2
    def wave(self, times):
        self.move_joints(*self.moves['up'])
        for i in range(times):
            self.move_joints(0, -90, 0, 40, 0)
            self.move_joints(0, -90, 0, -40, 0)

    def clap(self, times):
        for i in range(times):
            self.close_gripper()
            self.open_gripper()

    # Bonus
    def learn(self, name, angles):
        self.moves[name] = angles

    # TODO 3
    def perform(self, choreography):
        for name in choreography:
            if name in self.moves:
                if not self.move_joints(*self.moves[name]):
                    print(f'Could not do {name}, skipping it')
            elif name == 'wave':
                self.wave(2)
            elif name == 'clap':
                self.clap(3)
            else:
                print(f"I don't know the move {name!r}")


# TODO 4
dancer = DancingArm()
dancer.go_to('rest')
dancer.learn('reach', [0, -45, 45, 45, 0])
dancer.perform(['up', 'lean_left', 'wave', 'lean_right', 'twist', 'reach', 'moonwalk',
                'clap', 'bow'])

dancer.go_to('rest')
dancer.shutdown()
