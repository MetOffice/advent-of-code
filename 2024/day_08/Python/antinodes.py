import string
from itertools import combinations
import numpy as np

def load_input(filename):
    """
    Load the puzzle input from a file.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(np.array(list(line.strip())))

    return np.array(new_lines)


def find_antennae(puzzle_input, freq):
    """
    Find the antennae, for this frequency, in the puzzle input.
    """

    return np.argwhere(puzzle_input == freq)


def find_antinodes(coordinateA, coordinateB):
    """
    Find the antinodes for the given antenna in the puzzle input.
    """
    # Difference between the two antennae
    diff = coordinateA - coordinateB
    antinodeA = coordinateA + diff
    antinodeB = coordinateB - diff

    return antinodeA, antinodeB

if __name__ == "__main__":
    puzzle_input = load_input("input.txt")

    puzzle_bounds = np.array(puzzle_input).shape

    frequencies = string.digits + string.ascii_lowercase + string.ascii_uppercase

    antinodes = []
    for freq in frequencies:
        # Find antennae
        antennae = find_antennae(puzzle_input, freq)

        # Find antinodes
        for antenna in combinations(antennae, 2):
            antinodes.extend(find_antinodes(antenna[0], antenna[1]))


    antinodes = set(map(tuple, antinodes))
    print(antinodes)

    # Remove out of bounds
    antinodes = [
        antinode for antinode in antinodes if all(0 <= coord < bound for coord, bound in zip(antinode, puzzle_bounds))
    ]
    print(len(antinodes))

    # Part 2 here