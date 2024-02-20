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
            if re.match(r"[^\d|\.]", schematic_array[i,j]):
                list_of_things.append((i,j))
    return list_of_things

def find_part_numbers(list_of_things, schematic_array):
    row, column  = schematic_array.shape
    boundary_array = np.empty(row+2,column+2)
    boundary_array[1:,1:] = schematic_array
    for i,j in list_of_things:
        i+=1
        j+=1

# Check if there's a number in the window we've built
# and then regex back and forth until hitting a non-numerical character
# and package those numbers found up as a part schematic number