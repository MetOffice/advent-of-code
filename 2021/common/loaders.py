import os
import __main__


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


def load_ints():
    strings = load_string()
    return [int(string) for string in strings]
