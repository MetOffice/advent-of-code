import os
import __main__
from collections import namedtuple
import string

import numpy as np


def load_string(filepath=None):
    """
    Returns each line from the input file

    Returns
    -------
    : list of strings
        Each line from the index file
    """
    if not filepath:
        filepath = os.path.join(os.path.dirname(__main__.__file__), "../input.txt")

    with open(filepath) as file_handle:
        contents = file_handle.readlines()
    return [line.strip() for line in contents]


Coordinate = namedtuple("Coordinate", ["x", "y"])


def find_start_end(input_file: [str]) -> tuple[Coordinate,Coordinate]:
    start: Coordinate = None
    end: Coordinate = None

    for y, line in enumerate(input_file):
        s = line.find("S")
        if s != -1:
            start = Coordinate(s,y)
        e = line.find("E")
        if e != -1:
            end = Coordinate(e,y)

    return start, end

def get_elevation(s: str) -> int:
    """
    Return 1-26 for a-z, 27-52 for A-Z.
    """
    if s in string.ascii_lowercase:
        return ord(s) - 96
    else:
        if s == "E":
            return 26
        if s == "S":
            return 1


def find_path(input_data: [str], start, end):
    # lets make our letters be numbers!
    y_extent = len(input_data)
    x_extent = len(input_data[0])
    number_array = np.zeros([x_extent, y_extent])
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            number_array[x, y] = get_elevation(letter)

    # from current point, check the neighbouring (up, down, left, right) which are between 1 and <this value> + 1
    current_point = start
    possible_path_points = []
    for x_point in [current_point.x -1, current_point.x + 1]:
        if x_point == -1 or x_point == x_extent:
            pass
        else:
            possible_path_points.append(Coordinate(x_point, current_point.y))

    for y_point in [current_point.y + 1, current_point.y -1]:
        if y_point == -1 or y_point == y_extent:
            pass
        else:
            possible_path_points.append(Coordinate(current_point.x,y_point))

    #for coord in possible_path_points:
        # now check if these points are 1 <= current elevation <= current_elevation + 1
        # move current_point accordingly?

    print("done")




if __name__ == "__main__":
    start, end = find_start_end(load_string("../test_input.txt"))
    find_path(load_string("../test_input.txt"), start, end)
