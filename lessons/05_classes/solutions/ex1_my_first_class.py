"""Solution: Exercise 1 (one possible answer)."""


class Rover:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.battery = 100

    def report(self, message):
        print(f'{self.name}: {message}')

    def drive(self, meters):
        # TODO 2: check the battery before moving.
        cost = 5 * abs(meters)
        if cost > self.battery:
            self.report(f'Not enough battery to drive {meters} m.')
            return
        self.position = self.position + meters
        self.battery = self.battery - cost
        print(f'{self.name} drives {meters} m, to {self.position} m.')

    # TODO 1
    def return_to_base(self):
        self.drive(-self.position)


curiosity = Rover('Curiosity')
curiosity.report('Systems online.')
curiosity.drive(3)
curiosity.drive(2)
print('Curiosity is at', curiosity.position, 'm with', curiosity.battery, '% battery')

# TODO 1
curiosity.return_to_base()
print('Curiosity is at', curiosity.position, 'm with', curiosity.battery, '% battery')

# TODO 2: 50% battery left, and 20 m would need 100%.
curiosity.drive(20)


# TODO 3
class Drone:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.height = 0

    def take_off(self):
        self.height = 10
        self.battery = self.battery - 20
        print(f'{self.name} takes off to {self.height} m. Battery: {self.battery}%')

    def land(self):
        self.height = 0
        print(f'{self.name} lands.')


scout = Drone('Scout', 100)
falcon = Drone('Falcon', 60)
scout.take_off()
falcon.take_off()
scout.land()
print('Scout is at', scout.height, 'm and Falcon is at', falcon.height, 'm')
