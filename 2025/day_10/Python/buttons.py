import itertools
from functools import reduce
from typing import NamedTuple


def parse_button(b):
    return {int(i) for i in b[1:-1].split(",")}


class Machine(NamedTuple):
    @classmethod
    def from_line(cls, item) -> Machine:
        indicators, *buttons, joltage = item.strip().split(" ")
        ind = {i for i, c in enumerate(indicators[1:-1]) if c == "#"}
        butt = [parse_button(b) for b in buttons]
        jolt = [int(i) for i in joltage[1:-1].split(",")]
        return cls(ind, butt, jolt)

    def solve(self):
        for i in range(len(self.buttons)):
            for c in itertools.combinations(self.buttons, i):
                if self.check_combination(c):
                    return i

    def check_combination(self, combination: tuple[set[int]]) -> bool:
        reduced = reduce(set.symmetric_difference, combination, set())
        if reduced == self.indicators:
            return True
        return False

    indicators: set[int]
    buttons: list[set[int]]
    joltage: list[int]


def read_file():
    with open("../input.txt", "r") as file:
        lines = file.readlines()
        return [Machine.from_line(item) for item in lines]


def main():
    machines: list[Machine] = read_file()
    result = [m.solve() for m in machines]
    print(sum(result))


if __name__ == "__main__":
    main()
