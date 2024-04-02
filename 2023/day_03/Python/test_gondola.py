import gondola
import numpy as np

test_input =['467..114..',
             '...*......',
             '..35..633.',
             '......#...',
             '617*......',
             '.....+.58.',
             '..592.....',
             '......755.',
             '...$.*....',
             '.664.598..']


test_array = np.array([list(word) for word in test_input])

part_indicators = [(3, 1), (6, 3), (3, 4), (5, 5), (3, 8), (5, 8)]
def test_string_to_array():
    result = gondola.string_to_array(test_input)

    assert np.array_equal(result, test_array)


def test_find_parts():
    parts = gondola.find_parts(test_array)

    assert parts == part_indicators


def test_find_part_numbers():
    part_numbers = ['467', '35', '633', '617', '592', '755', '664', '598']

    result = gondola.find_part_numbers(part_indicators, test_array)

    assert set(result) == set(part_numbers)

def test_part2():
    result = gondola.find_gear_ratios(part_indicators, test_array)
    assert result == 467835
