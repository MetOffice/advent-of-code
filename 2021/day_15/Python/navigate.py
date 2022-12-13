import numpy as np


def load_input(filepath: str) -> np.ndarray:
    arr = np.genfromtxt(filepath, int, delimiter=1)
    return arr


# todo:
# 0. load input
# 1. pathfind from top to bottom corner
# 2. what is the lowest risk number of the path? remember to not count the value at the start

def find_safest_route(map_of_cave):
    total_safety = np.ones_like(map_of_cave) * 999999
    old_total_safety = total_safety.copy()

    total_safety[0, 0] = 0
    i = 0

    while (np.array_equal(total_safety, old_total_safety) is False):
        print(i)
        old_total_safety = total_safety.copy()
        # do a sideways
        new_total_safety = total_safety[:, :-1] + map_of_cave[:, 1:]
        total_safety[:, 1:] = np.minimum(new_total_safety, total_safety[:, 1:])

        # do the other sideways
        new_total_safety = total_safety[:, 1:] + map_of_cave[:, :-1]
        total_safety[:, :-1] = np.minimum(new_total_safety, total_safety[:, :-1])

        # do a down
        new_total_safety = total_safety[:-1, :] + map_of_cave[1:, :]
        total_safety[1:, :] = np.minimum(new_total_safety, total_safety[1:, :])

        # do an up
        new_total_safety = total_safety[1:, :] + map_of_cave[:-1, :]
        total_safety[:-1, :] = np.minimum(new_total_safety, total_safety[:-1, :])
        i = i+1

    return total_safety


def do_clock_maths(matrix, add):
    return (matrix + add - 1) % 9 + 1



def make_full_array(in_arr, multiply=5):
    in_shape = np.shape(in_arr)
    new_array = np.zeros((in_shape[0] * multiply, in_shape[1] * multiply), dtype=int)

    for i in range(0, multiply):
        for j in range(0, multiply):
            new_array[i*in_shape[0]:(i+1)*in_shape[0], j*in_shape[1]:(j+1)*in_shape[1]] = do_clock_maths(in_arr, i+j)

    return new_array


if __name__ == "__main__":
    arr = load_input("../input.txt")
    result = find_safest_route(arr)
    result_part_1 = result[-1:-1]

    bigger_array = make_full_array(arr)

    result_part_2 = find_safest_route(bigger_array)
    print(result_part_2[-1, -1])

    print("done")

