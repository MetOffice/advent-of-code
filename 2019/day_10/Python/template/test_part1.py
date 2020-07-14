"""
Test part 1.
To run, first, pip or conda install pytest
Then, from the team directory, run `python -m pytest .`
or, if using Cloud9 on AWS, run `python3 -m pytest .`
"""
from unittest.mock import patch, mock_open
from part1 import get_input, find_angle, map_to_positions, visible_asteroid_count, main
import pytest


def test_get_input():
    input_data = """.#..#
.....
#####
....#
...##
"""
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual = get_input()

    expected = [
        ".#..#",
        ".....",
        "#####",
        "....#",
        "...##",
    ]

    assert actual == expected


def test_map_to_positions():
    expected = [(1, 0), (1, 1)]

    mock_data = [
        ".#",
        ".#",
    ]
    actual = map_to_positions(mock_data)

    assert actual == expected


@pytest.mark.parametrize(
    'destination, expected', [
        ((0, 0), 315),
        ((0, 1), 360),
        ((0, 2), 45),
        ((1, 0), 270),
        ((1, 1), None),
        ((1, 2), 90),
        ((2, 0), 225),
        ((2, 1), 180),
        ((2, 2), 135),
        ])
def test_find_angle(destination, expected):
    origin = (1, 1)
    actual = find_angle(origin, destination)

    assert actual == expected


# TODO: parameterise test on mock_position
def test_visible_asteroid_count():
    expected = 1

    mock_position = (0, 0)
    mock_map = [(0, 0), (3, 1), (6, 2)]
    actual = visible_asteroid_count(mock_position, mock_map)

    assert actual == expected


def test_example_1():
    expected = 33

    mock_data = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
'''
    with patch("builtins.open", mock_open(read_data=mock_data)):
        actual = main()

    assert actual == expected


def test_final_example():
    expected = 210

    mock_data = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
'''
    with patch("builtins.open", mock_open(read_data=mock_data)):
        actual = main()

    assert actual == expected
