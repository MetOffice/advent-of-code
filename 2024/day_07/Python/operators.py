import operator as op
import itertools


def load_input(filename: str) -> list:
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def process_input(lines):
    answers = []
    values = []
    for line in lines:
        _answer, _values = line.split(": ")
        answers.append(int(_answer))
        values.append([int(x) for x in _values.split(" ")])

    return answers, values


def check_equation(answer, values, pos_operators=[op.add, op.mul]):
    Noperators = len(values) - 1

    operator_list = itertools.product(pos_operators, repeat=Noperators)

    for op_list in operator_list:
        result = values[0]
        for op, val in zip(op_list, values[1:]):
            result = op(result, val)
        if result == answer:
            return True


def concatenate_operator(a, b):
    return int(str(a) + str(b))


def do_puzzle(answer, values, pos_operators):
    # Find which equations are possible
    possible = []
    for answer, value in zip(answers, values):
        if check_equation(answer, value, pos_operators=pos_operators):
            possible.append(True)
        else:
            possible.append(False)

    # Sum possible answers
    total = 0
    for answer, value, is_possible in zip(answers, values, possible):
        if is_possible:
            total += answer
    print(f"Total possible answers: {total}")


if __name__ == "__main__":
    input_lines = load_input("day07_input.txt")

    answers, values = process_input(input_lines)

    # Part 1:
    print("Answer Part 1:")
    pos_operators = [op.add, op.mul]
    do_puzzle(answers, values, pos_operators)

    # Part 2:
    print("Answer Part 2:")
    pos_operators = [op.add, op.mul, concatenate_operator]
    do_puzzle(answers, values, pos_operators)
