import loaders
import re
import numpy as np



def parse_input():
    # taking from loaders.py in common, turning our input into readable strings
    input_schematic = loaders.load_string(input.txt)
    return input_schematic

def string_to_array(input_schematic):
    schematic_array = np.asarray(input_schematic, dtype=str)
    return schematic_array

def find_parts(schematic_array):     # start with symbols and look for numbers
    row, column = schematic_array.shape
    list_of_things = []
    for i in range(row):
        for j in range(column):
            if re.match(r"[^\d|\.]"):
                list_of_things.append((i,j))
    return list_of_things

def g(list_of_things):