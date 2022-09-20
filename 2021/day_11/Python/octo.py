from itertools import product
import numpy as np
import numpy.ma as ma

def get_neighbour_indices(x, y, x_max, y_max):
    x_list = []
    y_list = []
    for xdiff, ydiff in product([-1, 0, 1], [-1, 0, 1]):
        x2, y2 = x + xdiff, y + ydiff
        if (
            (xdiff == 0 and ydiff == 0)
            or (x2 < 0)
            or (y2 < 0)
            or (x2 > x_max)
            or (y2 > y_max)
        ):
            continue
        else:
            x_list.append(x2)
            y_list.append(y2)
    return np.array(x_list), np.array(y_list)


def step(start):
    masked = ma.masked_array(start)
    shape = masked.shape
    x_max = shape[0] -1
    y_max = shape[1] -1
    # increase everything by 1
    masked += 1
    # Flash
    while True:
        to_flash = (masked > 9)
        if not to_flash.any():
            break
        for x, y in zip(*to_flash.nonzero()):
            neighbours = get_neighbour_indices(x, y, x_max, y_max)
            masked[neighbours] += 1
            masked[x, y] = ma.masked
  
    # Reset flashed to 0
    flashes = ma.count_masked(masked)
    return masked.filled(0), flashes

def simulate(start, n):
    print(start)
    flashes = 0
    for i in range(n):
        start, new_flashes = step(start)
        flashes += new_flashes
    print(start)
    return flashes


def find_sync(start):
    print(start)
    flashes = 0
    i = 0
    while True:
        i += 1
        start, new_flashes = step(start)
        flashes += new_flashes
        if new_flashes == start.shape[0] * start.shape[1]:
            print(f"All flashed together on step {i}")
            break
    print(start)
    return flashes

def load_input(filepath: str) -> np.ndarray:
    arr = np.genfromtxt(filepath, int, delimiter=1)
    return arr


if __name__ == "__main__":
    start = load_input("day_11/input.txt")
    # print(start)
    flashes = simulate(start, 100)
    print(f"Flashed {flashes} times")
    start = load_input("day_11/input.txt")
    find_sync(start)
