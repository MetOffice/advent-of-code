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
        if action.dir == "R":
            dry = self.pos + action.value
        elif action.dir == "L":
            dry = self.pos - action.value
        else:
            raise NotImplemented()

        div, mod = divmod(dry, 100)
        if (self.pos == 0 and action.dir == "L"):
            self.zero_count += abs(div)-1
        elif (self.pos != 0 and div != 0) or mod == 0:
            self.zero_count += max(abs(div), 1)
        self.pos = mod


def process(actions: list[Instruction]):
    lock = Lock()
    [lock.apply(i) for i in actions]
    print(lock.zero_count)


def main():
    lines = read_file("../input")
    process(lines)


if __name__ == "__main__":
    main()
