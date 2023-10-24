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
        if s != - 1:
            start = Coordinate(s,y)
        e = line.find("E")
        if e != - 1:
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


def find_path(input_data: [str], start:Coordinate, end:Coordinate):
    """
    Finds paths
    """
    # lets make our letters be numbers!
    y_extent = len(input_data)
    x_extent = len(input_data[0])
    heights_array = np.zeros([x_extent, y_extent], dtype=int)
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            heights_array[x, y] = get_elevation(letter)

    distances_array = np.ones_like(heights_array) * heights_array.size
    distances_array[start] = 0

    progress_counter = 0

    while(distances_array[end] == heights_array.size):
        # array of bools of whether we can move this way
        moves_array = np.abs(heights_array[:, 1:] - heights_array[:,:-1]) <= 1
        new_distances_array = np.ones_like(distances_array[:, 1:]) * heights_array.size
        new_distances_array[moves_array] = distances_array[:, 1:][moves_array] + 1
        distances_array[:,:-1] = np.min((distances_array[:,:-1], new_distances_array), axis=0)

        moves_array = np.abs(heights_array[:,:-1] - heights_array[:, 1:]) <= 1
        new_distances_array = np.ones_like(distances_array[:, 1:]) * heights_array.size
        new_distances_array[moves_array] = distances_array[:,:-1][moves_array] + 1
        distances_array[:, 1:] = np.min((distances_array[:, 1:], new_distances_array), axis=0)

        moves_array = np.abs(heights_array[ 1:,:] - heights_array[:-1,:]) <= 1
        new_distances_array = np.ones_like(distances_array[ 1:,:]) * heights_array.size
        new_distances_array[moves_array] = distances_array[ 1:,:][moves_array] + 1
        distances_array[:-1,:] = np.min((distances_array[:-1,:], new_distances_array), axis=0)

        moves_array = np.abs(heights_array[:-1,:] - heights_array[ 1:,:]) <= 1
        new_distances_array = np.ones_like(distances_array[ 1:,:]) * heights_array.size
        new_distances_array[moves_array] = distances_array[:-1,:][moves_array] + 1
        distances_array[ 1:,:] = np.min((distances_array[ 1:,:], new_distances_array), axis=0)

        print(f"{progress_counter}/{heights_array.size}")
        progress_counter += 1


    print(distances_array[end])




if __name__ == "__main__":
    input_lines = load_string("../input.txt")
    start, end = find_start_end(input_lines)
    find_path(input_lines, start, end)
