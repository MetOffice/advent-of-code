import os
import __main__
from collections import namedtuple


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

    return start,end


start, end = find_start_end(load_string("../test_input.txt"))

print(start.x)
