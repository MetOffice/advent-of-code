import itertools
import os
from dataclasses import dataclass
from typing import Literal

import numpy as np
from PIL import Image


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

def step(warehouse, dir: Literal['^', 'v', '<', '>']):
    match dir:
        case '>':
            step_right(warehouse)
        case '<':
            rotated = np.rot90(warehouse, 2)
            step_right(rotated)
        case '^':
            rotated = np.rot90(warehouse, 3)
            step_right(rotated)
        case 'v':
            rotated = np.rot90(warehouse, 1)
            step_right(rotated)

def step_right(warehouse: np.ndarray):
    """
    Operates in-place!!!!!!!
    """
    robot = find_robot(warehouse)
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

    return

def main():
    images = []

    inp = read_input("test_input.txt")
    while True:
        print(chr(27) + "[2J")
        print(inp.warehouse)
        images.append(convert_image(inp.warehouse).resize((300, 300), Image.NEAREST))
        step(inp.warehouse, '^')
        if input("Continue...") == "q":
            break

    images[0].save('warehouse.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=1000, loop=1)
    os.startfile('warehouse.gif')

def convert_image(arr):
    colour_map = {
        '.': (255, 255, 255),
        '#': (50, 50, 50),
        '@': (255, 0, 0),
    }
    height, width = arr.shape
    img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), colour_map.get(arr[y, x], (128, 128, 128)))

    return img


if __name__ == "__main__":
    main()
