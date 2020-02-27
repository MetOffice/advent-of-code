from part1 import intcode, read_input
from copy import copy


def brute_force(filepath):

    original_list = read_input(filepath)

    for noun in range(0, 100):
        for verb in range(0, 100):
            new_list = copy(original_list)
            new_list[1] = noun
            new_list[2] = verb

            if intcode(new_list)[0] == 19690720:
                return noun, verb


if __name__ == '__main__':
    filepath = "../../input.txt"

    noun, verb = brute_force(filepath)
    print(noun, verb)
    print(100 * noun + verb)
