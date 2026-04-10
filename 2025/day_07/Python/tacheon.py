from time import sleep

import numpy as np


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

frames = []
def write_array_as_frame(array):
    frame = "\n".join("".join(row) for row in array)
    frames.append(frame)
    print("\033[0;0H") # Reset cursor to top left
    print(frame)

def main():
    t = load_input("../input.txt")
    start = np.where(t == "S")
    write_array_as_frame(t)
    t[(start[0] + 1, start[1])] = "|"
    write_array_as_frame(t)

    total = 0
    for i in range(1, len(t)-1):
        total += iterate_once(i, t)
        write_array_as_frame(t)
        sleep(0.05) # For animation


    print(total)



if __name__ == "__main__":
    main()
