from typing import Any

import numpy as np
from numpy import dtype, ndarray


def load_input(file_path) -> ndarray[tuple[Any, ...], dtype[Any]]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([list(line.strip()) for line in lines])
    return np.array(lines)

def convert_to_int(array: ndarray):
    array[array == "@"] = 1
    array[array == "."] = 0


def main():
    input_data = load_input('../input.txt')
    convert_to_int(input_data)
    input_data.astype(int)
    print(input_data)
    # Then convolve it!

if __name__ == "__main__":
    main()

