import re
import numpy as np
import sys

sys.path.append("C:/Users/Rowan.baker/Advent-of-code/2023")

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
                list_of_part_indicators.append((i, j))
    return list_of_part_indicators


def find_part_numbers(list_of_part_indicators, schematic_array):
    row, column = schematic_array.shape
    boundary_array = np.empty((row + 2, column + 2), dtype=str)
    boundary_array[1:-1, 1:-1] = schematic_array
    part_number = ""
    for i, j in list_of_part_indicators:
        i += 1
        j += 1
        for mod_i in range(-1, 2):
            for mod_j in range(-1, 2):
                if boundary_array[i + mod_i, j + mod_j].isnumeric():
                    x_index = i + mod_i
                    part_number = ""
                    while boundary_array[x_index, j + mod_j].isnumeric():
                        part_number = boundary_array[x_index, j + mod_j] + part_number
                        x_index -= 1
                    x_index = i + mod_i + 1
                    while boundary_array[x_index, j + mod_j].isnumeric():
                        part_number = part_number + boundary_array[x_index, j + mod_j]
                        x_index += 1

            print(part_number)
            # Parts number's borked. Gives us single digits, not multidigit numbers.
            # Also, we ought to write tests, I guess? Not enough testing up in this.


if __name__ == "__main__":
    input_schematic = parse_input()
    schematic_array = string_to_array(input_schematic)
    list_of_part_indicators = find_parts(schematic_array)
    find_part_numbers(list_of_part_indicators, schematic_array)
