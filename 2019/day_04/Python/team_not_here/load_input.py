from collections import namedtuple
from pathlib import Path

Range = namedtuple("Range", ["min", "max"])


def get_input() -> Range:
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_str = file.readline()
        _MIN, _MAX = input_str.split('-')

    return Range(_MIN, _MAX)
