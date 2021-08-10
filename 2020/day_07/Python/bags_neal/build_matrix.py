import re
import numpy as np

def regex_simplify(file_contents):
    """
    Remove noise from the input file- words like 'bags' and so on.
    """
    new_file_contents = []
    for line in file_contents:
        new_line = re.sub("bag[s,.]*", "", line)
        new_line = re.sub("contain[s]*", ":", new_line)
        new_line = re.sub("no other", "", new_line)
        new_file_contents.append(new_line)
    return new_file_contents

def build_colour_dict(file_contents, first_colour):
    colour_dict = dict()
    index = 1
    for line in file_contents:
        colour = line.split(":")[0].strip()
        if colour == first_colour:
            colour_dict[colour] = 0
        else:
            colour_dict[colour] = index
            index += 1

    return colour_dict

def build_bag_matrix_from_file(file_contents, colour_dict):

    # first construct the matrix and fill it with zeroes
    number_of_colours = len(colour_dict)
    bag_matrix = np.zeros((number_of_colours, number_of_colours), dtype=np.int64)

    # now use file_contents to fill the bag_matrix
    line_count = 0
    for line in file_contents:
        # split line into space-separated tokens
        tokens = line.split()
        # reconstruct the line colour from the first two words - this assumes all colours
        # are two words long! this is a bit of a hack, got to be honest
        line_colour = tokens[0] + " " + tokens[1]
        # recover which row of the matrix this is
        line_index = colour_dict[line_colour]

        # now move through tokens, three at a time - should be an int, and then two tokens
        # for the colour (if not, something is horribly wrong)
        count = 3
        while count < len(tokens):
            number_of_bags = int(tokens[count])
            colour = tokens[count + 1] + " " + tokens[count + 2]
            colour_index = colour_dict[colour]
            bag_matrix[line_index, colour_index] = number_of_bags
            count += 3
    
    return bag_matrix

def build_matrix(file_contents, first_colour):
    file_contents = regex_simplify(file_contents)
    colour_dict = build_colour_dict(file_contents, first_colour)
    bag_matrix = build_bag_matrix_from_file(file_contents, colour_dict)

    return bag_matrix
