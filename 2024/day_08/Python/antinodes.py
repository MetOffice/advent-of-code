from fractions import Fraction
import string
from itertools import combinations
import numpy as np


def array_from_lines(lines):
    new_lines = []
    for line in lines:
        new_lines.append(np.array(list(line.strip())))

    return np.array(new_lines)


def load_input(filename):
    """
    Load the puzzle input from a file.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    return array_from_lines(lines)


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


def find_antinodes_part_2(coordinateA, coordinateB):
    diff = coordinateA - coordinateB
    fr = Fraction(*diff)
    diff_simplified = np.array([fr.numerator, fr.denominator])

    for i in range(100):
        yield coordinateA + i * diff_simplified
        yield coordinateA - i * diff_simplified


def find_antinodes_from_antennas(find_antinodes_fn, puzzle_input):
    puzzle_bounds = np.array(puzzle_input).shape

    frequencies = string.digits + string.ascii_lowercase + string.ascii_uppercase

    antinodes = []
    for freq in frequencies:
        # Find antennae
        antennae = find_antennae(puzzle_input, freq)

        # Find antinodes
        for antenna in combinations(antennae, 2):
            antinodes.extend(find_antinodes_fn(antenna[0], antenna[1]))

    antinodes = set(map(tuple, antinodes))

    # Remove out of bounds
    antinodes = [
        antinode
        for antinode in antinodes
        if all(0 <= coord < bound for coord, bound in zip(antinode, puzzle_bounds))
    ]

    puzzle_grid = np.array(puzzle_input)
    for antinode in antinodes:
        if puzzle_grid[antinode] == ".":
            puzzle_grid[antinode] = "#"

    row_strs = []
    for row in puzzle_grid:
        row_strs.append("".join(row))

    puzzle_grid_str = "\n".join(row_strs)

    print(puzzle_grid_str)

    print(len(antinodes))

    return puzzle_grid_str


if __name__ == "__main__":
    puzzle_input = load_input("input.txt")

    find_antinodes_from_antennas(find_antinodes, puzzle_input)

    # Part 2 here

    find_antinodes_from_antennas(find_antinodes_part_2, puzzle_input)
