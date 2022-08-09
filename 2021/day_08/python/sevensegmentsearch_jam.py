from dataclasses import dataclass
from xml.dom.minidom import Identified
import numpy as np

def string2array(string:str):
    """
    Takes a 7 segment string and outputs a 7 element numpy array
    The array indices 0-6 contain booleans corresponding to whether the string contains a-g
    """
    array = np.zeros(7)
    for idx, char in enumerate("abcdefg"):
        array[idx] = char in string
    return array

def decode_line(line:str):
    return np.array([string2array(digit) for digit in line.split()], dtype=int)

def get_input():
    """
    Get input as list of tuples of arrays
    List element is input line
    Tuple element is sample/output digits
    Array dim0 is digit
    Array dim1 is segment
    Segment value is whether that segment is lit
    """
    input = []
    with open("./2021/day_08/input.txt", "r") as file:
        for line in file:
            digits_string, out_string = line.split("|")
            digits = decode_line(digits_string)
            out = decode_line(out_string)
            input.append((digits, out))
    return input

def count_all_1478(input):

    total = 0
    for line in input:
        # this is a numpy array
        total += count1478(line[1])

    return total

def count1478(sample):
    """
    Counts the number of occurrences of 1, 4, 7 or 8
    Equal to number of digits with 2, 3, 4 or 7 segments lit
    """
    segments = np.sum(sample, axis=1)
    return np.sum(count1478.deltas[segments])
# A trick to only compute this value once
count1478.deltas = np.zeros(8, dtype=int)
count1478.deltas[np.array([2,3,4,7])] = 1


input = get_input()
count = count_all_1478(input)

print(count)

##########
# PART 2 #
##########

@dataclass
class IdentifyingInformation():
    """
    Contains data identifying a digit from its sample
    """
    total_segments : int
    has_b : bool
    has_e : bool
    has_f : bool
    has_ac : bool
    has_dg : bool

def sum_values(input):
    """
    Reads the input and returns the sum of all numbers in it
    """
    total = 0

    for line in input:
        sample, digits = line
        identity_map = identify_digits(sample)
        #total += decode_digits(digits, identity_map)

    return total

def identify_digits(sample:np.ndarray):
    """
    Create an identity map taking segment data and returning the digit
    """
    identity_map = dict()

    print(np.sum(sample, axis=0))
    print(np.sum(sample, axis=1))

    # these are segments with unique counts of appearances within the digits
    b_idx, e_idx, f_idx, ac_idx, ca_idx, dg_idx, gd_idx = letter_indices(sample)

    

    return identity_map

def letter_indices(sample):
    """
    Get the indices of the different segments.
    b, e and f are unique, a-c and d-g are shared
    """
    segment_counts = np.sum(sample, axis=0)
    b_idx = np.nonzero(segment_counts == 6)[0][0]
    e_idx = np.nonzero(segment_counts == 4)[0][0]
    f_idx = np.nonzero(segment_counts == 9)[0][0]

    ac_idx = np.nonzero(segment_counts == 8)[0][0]
    ca_idx = np.nonzero(segment_counts == 8)[1][0]

    dg_idx = np.nonzero(segment_counts == 7)[0][0]
    gd_idx = np.nonzero(segment_counts == 7)[1][0]


    return b_idx, e_idx, f_idx, ac_idx, ca_idx, dg_idx, gd_idx



sum_values(input)