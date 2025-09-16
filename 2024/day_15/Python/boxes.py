from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Input:
    warehouse: np.ndarray
    moves: str


def read_input(filename: str) -> Input:
    with open(filename) as f:
        input_str = f.read()

    warehouse, moves = input_str.split("\n\n")

    return Input(
        np.array(list(map(list, warehouse.split("\n")))), moves.replace("\n", "")
    )


print(read_input("test_input.txt"))
