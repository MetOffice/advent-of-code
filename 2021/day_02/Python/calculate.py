from common import loaders, timers

class Submarine:
    def __init__(self, depth=0, horizontal_position=0):

        self.depth = depth
        self.horizontal_position = horizontal_position

    def move(self, command):
        direction, value = command.split()
        value = int(value)

        if direction == "forward":
            self.horizontal_position += value
        elif direction == "down":
            self.depth += value
        elif direction == "up":
            self.depth -= value
        else:
            raise ValueError("Santa has been on the run again (i.e. no acceptable movement command)")

    def execute_course(self, commands):
        for command in commands:
            self.move(command)





if __name__ == "__main__":
    commands = loaders.load_string()

    sub = Submarine()
    sub.execute_course(commands)

    answer_part1 = sub.depth * sub.horizontal_position

    print(answer_part1)
