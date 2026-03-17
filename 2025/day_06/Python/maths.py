from functools import reduce
from operator import mul, add


def load_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([line.strip().split() for line in lines])
    return lines


ops = {
    "+": add,
    "*": mul
}


def main():
    input_data = load_input('../input.txt')
    sums = list(zip(*input_data))
    total = 0
    for sum in sums:
        total += reduce(ops[sum[-1]], map(int, sum[:-1]))

    print(total)


if __name__ == "__main__":
    main()
