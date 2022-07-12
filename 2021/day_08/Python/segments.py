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

    unique_digits = [digit for digit in four_digits if len(digit) in segment_numbers_for_each_digit.values()]

    return len(unique_digits)


def main_part_1(display_codes):
    count = 0

    for display_code in display_codes:
        definition, four_digits = parse_display_code(display_code)

        number_of_unique_segments = count_unique_segments(four_digits)

        count += number_of_unique_segments

    return count


if __name__ == "__main__":
    display_codes = load_string()

    count = main_part_1(display_codes)

    print(f"Part 1: {count}")
