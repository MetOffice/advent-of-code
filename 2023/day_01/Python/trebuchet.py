#!/usr/bin/env python3
import re
import sys

sys.path.extend(["/net/home/h05/frtz/PythonTraining/advent-of-code/2023"])
from common.loaders import load_string


def find_first_n_last_digit(input_string):
    ''' Uses regexes to find the first and last digits in a string, concattenate
    them and turn the result into an integer.'''
    first_digit = re.search(r"^[a-zA-Z]*(\d).*$", input_string)
    last_digit = re.search(r"^.*(\d)[a-zA-Z]*$", input_string)
    number_string = first_digit.group(1) + last_digit.group(1)
    return int(number_string)


def main():
    '''Main program to bolt all the bits n bobs together as well as handle admin
    such as loading the inputs and printing the result'''
    print("I am Groot")
    inputs = load_string()
    total = 0
    for input_string in inputs:
        total += find_first_n_last_digit(input_string)

    print(f"Part 1: the total is {total}")

if __name__ == "__main__":
    main()
