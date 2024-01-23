#!/usr/bin/env python3
import regex as re

from common.loaders import load_string


def find_first_n_last_digit(input_string):
    ''' Uses regexes to find the first and last digits in a string, concattenate
    them and turn the result into an integer.'''
    new_reg = re.findall(r"one|two|three|four|five|six|seven|eight|nine|[1-9]", input_string, overlapped=True)
    number_string = parse_number_string_to_int(new_reg[0])*10 + parse_number_string_to_int(new_reg[-1])
    return number_string


def parse_number_string_to_int(number_string):
    '''Takes a string with a written number and return int for one to nine'''
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
                "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9}
    return num_dict[number_string]


def main():
    '''Main program to bolt all the bits n bobs together as well as handle admin
    such as loading the inputs and printing the result'''
    print("I am Groot")
    inputs = load_string("../input.txt")
    total = 0
    for input_string in inputs:
        total += find_first_n_last_digit(input_string)

    print(f"Part 2: the total is {total}")


if __name__ == "__main__":
    main()
