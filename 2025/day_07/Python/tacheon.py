from time import sleep

import numpy as np


def load_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([list(line.strip()) for line in lines])
    # This should be an int array...
    return np.array(lines, dtype=(str, 15))


def iterate_once(row: int, array):
    beams = np.where(np.char.isdigit(array[row]))
    split_count = 0
    for beam in list(*beams):
        beam_val = int(array[row, beam])
        if array[row+1][beam] == "^":
            split_count += 1
            array[row+1, beam-1] = int(array[row+1, beam-1].replace(".","0")) + beam_val
            array[row+1, beam+1] = int(array[row+1, beam+1].replace(".","0")) + beam_val
        else:
            array[row+1, beam] = int(array[row+1, beam].replace(".","0")) + beam_val
    return split_count

frames = []
def write_array_as_frame(array):
    frame = "\n".join("".join(row) for row in array)
    frames.append(frame)
    print("\033[0;0H") # Reset cursor to top left
    print(frame)


def count_last_row(t):
    last_row = t[-1]
    ints = [ int(a) for a in last_row if a.isdigit() ]
    return sum(ints)


def main():
    t = load_input("../input.txt")
    start = np.where(t == "S")
    write_array_as_frame(t)
    t[(start[0] + 1, start[1])] = "1"
    write_array_as_frame(t)

    total = 0
    for i in range(1, len(t)-1):
        total += iterate_once(i, t)
        write_array_as_frame(t)
        # sleep(1) # For animation

    result2 = count_last_row(t)


    print("Pt1:" + str(total))
    print("Pt2:" + str(result2))



if __name__ == "__main__":
    main()
