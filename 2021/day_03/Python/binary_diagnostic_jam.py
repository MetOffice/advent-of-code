import numpy as np

def arr2bin(arr):
    """
    Interprets a boolean array as a binary string
    """
    # [...,16,8,4,2,1,0]
    bases = 2 ** np.arange(len(arr))[::-1]
    return np.sum(arr * bases)

def line2row(line:str):
    """
    Takes a string line from file and returns it as an integer array
    """
    return np.array([int(char) for char in line.strip()])

with open("./input.txt", "r") as f:
    input = []
    for line in f:
        input.append(line2row(line))
    
input = np.array(input)

# array of number of 1s for each column
counts = np.sum(input, axis=0)
# half the length of the array
half_len = len(input) / 2
# anywhere where there are equal numbers of 0 and 1
ambiguities = counts == half_len
# This is the single most readable line of code
# I think I've ever written
assert not np.any(ambiguities)
#
epsbits = counts > half_len

epsilon = arr2bin(epsbits)
gamma = arr2bin(~epsbits)
print(epsilon * gamma)

def bit_criteria(input:np.ndarray, index:int, mode:int):
    """
    Recursively resolve the bit criteria on the input.
    Index is the current column to match.
    mode=1 for keeping more common result and 1 as default.
    mode=0 for leeping less common result and 0 as default.
    """
    # return last value
    if len(input) == 1:
        return input[0]
    # count number of ones
    ones = np.sum(input[:,index])
    # if mode is 1, pick 1 if ones >= half length
    # if mode is 0, pick 0 if ones >= half length
    pick = mode ^ (ones < len(input) / 2)
    # recursively call with filtered inputs and next index
    return bit_criteria(
        input[input[:,index] == pick],
        index +1,
        mode
    )

oxy_bits = bit_criteria(input, 0, 1)
oxy = arr2bin(oxy_bits)

co2_bits = bit_criteria(input, 0, 0)
co2 = arr2bin(co2_bits)

print(oxy * co2)