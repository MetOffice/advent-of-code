import os
import __main__
from collections import namedtuple
import string

import numpy as np
from gif_plotter import GifPlotter


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
    E is at height 26 and S is at height 1.
    """
    if s in string.ascii_lowercase:
        return ord(s) - 96
    else:
        if s == "E":
            return 26
        if s == "S":
            return 1

def get_heights(input_data:[str]):
    """
    Create the heights maps from the input data
    """
    # lets make our letters be numbers!
    y_extent = len(input_data)
    x_extent = len(input_data[0])
    heights = np.zeros([x_extent, y_extent], dtype=int)
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            heights[x, y] = get_elevation(letter)

    return heights


def find_path(heights:np.ndarray, start:Coordinate, can_be_reached:callable, still_going:callable, output:callable, plotter:GifPlotter=None):
    """
    Finds shortest path to each point from the start.

    heights is a 2d array of integer heights of each point.
    start is the coordinate used as the root of pathfinding.
    can_be_reached is a function returning true if a to space can be reached from a from space
    still_going is a function returning true if the pathfinder has not yet completed
    output prints the desired output to console
    plotter is a plotter object for our entertainment
    """
    distances = np.ones_like(heights) * heights.size
    distances[start] = 0

    progress_counter = 0
    last = np.copy(distances)

    while(still_going(distances, heights)):

        # pathfind in each of the four cardinal directions
        update_distances(heights, distances, np.index_exp[:, 1:], np.index_exp[:,:-1], can_be_reached)
        update_distances(heights, distances, np.index_exp[:,:-1], np.index_exp[:, 1:], can_be_reached)
        update_distances(heights, distances, np.index_exp[ 1:,:], np.index_exp[:-1,:], can_be_reached)
        update_distances(heights, distances, np.index_exp[:-1,:], np.index_exp[ 1:,:], can_be_reached)

        print(f"{progress_counter}/{heights.size}")
        if plotter:
            plotter.snapshot(distances, heights)
        progress_counter += 1
        # emergency stop in case of stuck
        if np.all(last == distances):
            break
        last = np.copy(distances)

    output(distances, heights)


def update_distances(heights:np.ndarray, distances:np.ndarray, from_slice, to_slice, can_be_reached:callable):
    """
    Update the distances array with all moves from the from slice to the to slice according
    tot he can_be_reached predicate.
    This mutates the distances array in place.
    """
    moves = can_be_reached(heights[from_slice], heights[to_slice])
    new_distances = np.ones_like(distances[from_slice]) * heights.size
    new_distances[moves] = distances[from_slice][moves] + 1
    distances[to_slice] = np.min((distances[to_slice], new_distances), axis=0)


def can_be_reached_pt1(come_from, go_to):
    """
    Can we get from come_from to go_to?
    """
    return go_to - come_from <= 1


def can_be_reached_pt2(come_from, go_to):
    """
    Can we get from come_from to go_to?
    This is the reverse of the method in part 1
    """
    return go_to - come_from >= -1


def still_going_pt1(distances_array, heights_array):
    """
    Have we not yet reached the end according to the rules of part 1
    """
    return distances_array[end] == heights_array.size


def still_going_pt2(distances_array, heights_array):
    """
    Have we not yet reached the end according to the rules of part 2
    """
    return np.all(distances_array[heights_array == 1] == heights_array.size)


def output_pt1(distances, heights):
    """
    Write out the desired output of part 1
    """
    print(f"The end is {distances[end]} steps from the start.")


def output_pt2(distances, heights):
    """
    Write out the desired output of part 1
    """
    print(f"The closest point to the end at height a is {np.min(distances[heights == 1])} steps away.")


if __name__ == "__main__":
    plotter = GifPlotter()
    input_lines = load_string("../input.txt")
    start, end = find_start_end(input_lines)
    heights = get_heights(input_lines)

    print("Part 1: Shortest distance from start to end.")
    find_path(heights, start, can_be_reached_pt1, still_going_pt1, output_pt1, plotter)
    plotter.save("part1")

    plotter = GifPlotter()
    print("Part 2: Shortest distance from any low point to end.")
    find_path(heights, end, can_be_reached_pt2, still_going_pt2, output_pt2, plotter)
    plotter.save("part2")