import numpy as np
import tqdm


def load_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([list(line.strip()) for line in lines])
    return np.array(lines)


def iterate_once(row: int, array):
    beams = np.where(array[row] == "|")
    split_count = 0
    for beam in list(*beams):
        if array[row+1][beam] == "^":
            split_count += 1
            array[row+1, beam-1] = "|"
            array[row+1, beam+1] = "|"
        else:
            array[row+1, beam] = "|"
    return split_count



def main():
    t = load_input("../input.txt")
    start = np.where(t == "S")
    t[(start[0] + 1, start[1])] = "|"

    total = 0
    for i in tqdm.trange(1, len(t)-1):
        total += iterate_once(i, t)

    print(total)


if __name__ == "__main__":
    main()
