import re
from functools import reduce
from operator import mul, add


def load_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([line.strip().split() for line in lines])
    return lines


def load_input_2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list([list(line) for line in lines])
    return lines


ops = {
    "+": add,
    "*": mul
}


def part_1(input_data):
    sums = list(zip(*input_data))
    total = 0
    for sum in sums:
        total += reduce(ops[sum[-1]], map(int, sum[:-1]))

    print("Part1:", total)


def part_2(input_data):
    operators = input_data[-1]
    indexes = [i for i, o in enumerate(operators) if o in ["+", "*"]]
    total = 0
    for start, end in list(zip(indexes, indexes[1:] + [len(input_data[0])])):
        operator = ops[operators[start]]
        numbers = [x[start:end] for x in input_data]
        parsed_numbers = [int("".join(x[col] for x in numbers[:-1])) for col in range(len(numbers[0]) - 1)]
        total += reduce(operator, parsed_numbers)
    print("Part2:", total)
    return total


def main():
    input_data = load_input('../input.txt')
    part_1(input_data)
    part_2(load_input_2('../input.txt'))


if __name__ == "__main__":
    main()
