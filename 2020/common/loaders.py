import os
import __main__

def load_string():
    """
    Returns each line from the input file

    Returns:
    --------
    : list of strings
        Each line from the index file
    """
    filepath = os.path.join(os.path.dirname(__main__.__file__), "../input.txt") 
    with open(filepath) as file_handle:
        contents = file_handle.readlines()
    return [line.strip() for line in contents]

