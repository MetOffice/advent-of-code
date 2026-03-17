from typing import Any

import numpy as np
from numpy import dtype, ndarray
from scipy import ndimage


def load_input(file_path) -> ndarray[tuple[Any, ...], dtype[Any]]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([list(line.strip()) for line in lines])
    array = np.array(lines)
    array[array == "@"] = 1
    array[array == "."] = 0
    return array.astype(int)

def one_step(data):
    pass

box = np.array(
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
)

def main():
    input_data = load_input('../input.txt')
    # Then convolve it!
    result = 0
    while True:
        neighbours = ndimage.convolve(input_data.astype(int), box, mode="constant", cval=0)
        # Mask by locations with paper rolls
        masked = np.multiply(neighbours, input_data)
        masked[np.logical_and(1 < masked, masked < 5)] = 1
        masked[masked >= 5] = 0
        removed = sum(sum(masked))

        inverted = np.logical_not(masked).astype(int)
        input_data = np.multiply(inverted, input_data)

        if removed == 0:
            break
        result += removed

    print(result)

if __name__ == "__main__":
    main()

