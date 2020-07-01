from pathlib import Path
from typing import List


def get_input() -> List[int]:
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_str = file.readline()
    input_list = list(map(int, input_str.split(",")))

    return input_list
