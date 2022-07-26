from common.loaders import load_string
import numpy as np


def parse_display_code(display_code):
    """

    Parameters
    ----------
    display_code: str

    Returns
    -------
    tuple: (list, list)

    """
    definition_string, four_digits_string = display_code.split("|")

    four_digits = four_digits_string.split()
    definition = definition_string.split()

    return definition, four_digits


def count_unique_segments(four_digits):
    """
    """
    segment_numbers_for_each_digit = {"1": 2, "4": 4, "7": 3, "8": 7}

    unique_digits = [
        digit
        for digit in four_digits
        if len(digit) in segment_numbers_for_each_digit.values()
    ]

    return len(unique_digits)


def main_part_1(display_codes):
    count = 0

    for display_code in display_codes:
        definition, four_digits = parse_display_code(display_code)

        number_of_unique_segments = count_unique_segments(four_digits)

        count += number_of_unique_segments

    return count


def find_a():
    pass
    # a is 7 - 1


def find_b():
    pass
    # b is


def find_c():
    pass
    # c is missing element of 1 from digits of length 6


def find_d():
    pass
    # d is


def find_e():
    pass
    # e is


def find_f():
    pass
    # f is


def find_g():
    pass
    # g is


def main_part_2(display_codes):
    """
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

    """

    # VERY DRAFT

    segment_numbers_for_each_digit = {
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
        "0": 6,
    }

    # Will need loop later
    definition, four_digits = parse_display_code(display_code)

    # 1 is only definition with 2 elements
    # 7 is only definition with 3 elements
    # 4 is only definition with 4 elements
    # 8 is only definition with 7 elements

    decoding_definitions = set([char for char in definition])


if __name__ == "__main__":
    display_codes = load_string()

    count = main_part_1(display_codes)

    print(f"Part 1: {count}")
