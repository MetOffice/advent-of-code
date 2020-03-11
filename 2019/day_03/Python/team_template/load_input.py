from copy import deepcopy
from pathlib import Path
input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"

with open(input_file, "r") as file:
    _INPUT = file.read().splitlines()
    _WIRES = [line.split(",") for line in _INPUT]


def get_input():
    return _INPUT.copy()


def get_wires():
    return deepcopy(_WIRES)
