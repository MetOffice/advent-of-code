import itertools
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


def find_robot(warehouse: np.ndarray):
    res = np.where(warehouse == '@')
    return res[0][0], res[1][0]

def step_right(warehouse: np.ndarray, robot):
    """
    Operates in-place!!!!!!!
    """
    # Get the line to the right of the robot
    line = warehouse[robot[0]][robot[1]:]

    # Stop at the first obstacle or empty space
    line_of_interest = np.array(list(itertools.takewhile(lambda c: c not in '.#', line)))

    # Character that stops the movement
    stop_character = line[len(line_of_interest)]

    # Cannot move
    if stop_character == '#':
        return

    # Re-insert the original line back into the warehouse offset by 1
    warehouse[robot[0], robot[1] + 1: robot[1] + len(line_of_interest) + 1] = line_of_interest
    # Remove the original position of the robot
    warehouse[robot[0], robot[1]] = '.'

def main():
    inp = read_input("test_input.txt")
    robot = find_robot(inp.warehouse)
    step_right(inp.warehouse, robot)

    print(inp.warehouse)


if __name__ == "__main__":
    main()
