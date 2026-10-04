"""Solution: Exercise 4."""

robot_name = 'so-101'
print(robot_name.upper())
print(robot_name.replace('-', ' '))

# TODO 1: title() makes the first letter of each word a capital: 'So-101'
print(robot_name.title())


class Rover:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.battery = 100                          # TODO 3

    def report(self, message):
        print(f'{self.name}: {message}')

    def drive(self, meters):
        self.position = self.position + meters
        self.battery = self.battery - 5 * meters    # TODO 3
        print(f'{self.name} drives {meters} m, to {self.position} m.')

    def where_am_i(self):
        return self.position

    # TODO 4
    def recharge(self):
        self.battery = 100
        self.report('Battery recharged to 100%.')


curiosity = Rover('Curiosity')
curiosity.report('Systems online.')
curiosity.drive(3)
print('Curiosity is at', curiosity.where_am_i())
print('Curiosity is at', curiosity.position)

# TODO 2: each rover is its own object, with its own position.
perseverance = Rover('Perseverance')
perseverance.report('Ready to explore.')
perseverance.drive(4)
print('Curiosity is at', curiosity.position, 'and Perseverance is at', perseverance.position)

# TODO 3
curiosity.drive(2)
print('Curiosity has', curiosity.battery, '% battery')    # 75: 5 m driven so far, 5% each

# TODO 4
curiosity.recharge()
print('Curiosity has', curiosity.battery, '% battery')    # 100
