import dataclasses


@dataclasses.dataclass
class Instruction:
    dir: str
    value: int


def read_file(file_path) -> list[Instruction]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [parse_line(line.strip()) for line in lines]


def parse_line(line) -> Instruction:
    dir = line[0]
    value = int(line[1:])
    return Instruction(dir, value)


class Lock:
    def __init__(self):
        self.pos = 50
        self.zero_count = 0

    def apply(self, action: Instruction):
        remaining = action.value
        while remaining:
            self.tick(action.dir)
            self.check_zero()
            remaining -= 1

    def tick(self, direction):
        if direction == "R":
            self.pos += 1
        elif direction == "L":
            self.pos -= 1
        self.pos = self.pos % 100

    def check_zero(self):
        if self.pos == 0:
            self.zero_count += 1


def process(actions: list[Instruction]):
    lock = Lock()
    [lock.apply(i) for i in actions]
    print(lock.zero_count)


def main():
    lines = read_file("../input")
    process(lines)


if __name__ == "__main__":
    main()
