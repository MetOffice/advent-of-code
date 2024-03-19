import re
import numpy as np
import sys

from common.loaders import load_string

def parse_input():
    # taking from loaders.py in common, turning our input into readable strings
    input_schematic = load_string()
    return input_schematic


def string_to_array(input_schematic):
    schematic_array = np.asarray(input_schematic, dtype=str)
    new_array = np.empty((len(schematic_array), len(schematic_array[0])), dtype=str)
    for i in range(len(schematic_array)):
        for j, character in enumerate(schematic_array[i]):
            new_array[i, j] = character
    return new_array


def find_parts(schematic_array):  # start with symbols and look for numbers
    row, column = schematic_array.shape
    list_of_part_indicators = []
    for i in range(row):
        for j in range(column):
            if re.match(r"[^\d|\.]", schematic_array[i, j]):
                list_of_part_indicators.append((j, i))
    return list_of_part_indicators


def find_part_numbers(list_of_part_indicators, schematic_array):
    row, column = schematic_array.shape
    boundary_array = np.empty((row + 2, column + 2), dtype=str)
    mask = np.zeros((row + 2, column + 2))
    boundary_array[1:-1, 1:-1] = schematic_array

    part_numbers = []
    for i, j in list_of_part_indicators:
        # TODO: we need to be able to tell if one symbol has more than one number it matches
        i += 1
        j += 1
        part_number = ""
        for mod_i in range(-1, 2):
            for mod_j in range(-1, 2):
                if (boundary_array[j + mod_j, i + mod_i].isnumeric()) and (mask[j + mod_j, i + mod_i] == 0):
                    x_index = i + mod_i
                    while (boundary_array[j + mod_j, x_index].isnumeric()) and (mask[j + mod_j, x_index] == 0):
                        part_number = boundary_array[j + mod_j, x_index] + part_number
                        mask[j + mod_j, x_index] = 1
                        x_index -= 1
                    x_index = i + mod_i + 1
                    while (boundary_array[j + mod_j, x_index].isnumeric()) and (mask[j + mod_j, x_index] == 0):
                        part_number = part_number + boundary_array[j + mod_j, x_index]
                        mask[j + mod_j, x_index] = 1
                        x_index += 1
                    part_numbers.append(part_number)
                    part_number = ""

    return part_numbers
            # Parts number's borked. Gives us single digits, not multidigit numbers.
            # Also, we ought to write tests, I guess? Not enough testing up in this.


if __name__ == "__main__":
    input_schematic = parse_input()
    schematic_array = string_to_array(input_schematic)
    list_of_part_indicators = find_parts(schematic_array)
    part_numbers = find_part_numbers(list_of_part_indicators, schematic_array)
    part_numbers = [int(number) for number in part_numbers]

    result = sum(part_numbers)
    print(result)
