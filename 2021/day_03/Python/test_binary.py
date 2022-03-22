from binary import (
    find_most_common_bit,
    find_least_common_bit,
    get_gamma_rate,
    get_epsilon_rate,
    find_oxygen_rating,
    find_co2_rating
)
import pytest


input_strings = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


@pytest.mark.parametrize(
    ("column", "expected"), [(0, 1), (1, 0), (2, 1), (3, 1), (4, 0),]
)
def test_find_most_common_bit(column, expected):
    actual = find_most_common_bit(input_strings, column)

    assert actual == expected


@pytest.mark.parametrize(
    ("column", "expected"), [(0, 0), (1, 1), (2, 0), (3, 0), (4, 1),]
)
def test_find_least_common_bit(column, expected):
    actual = find_least_common_bit(input_strings, column)

    assert actual == expected


def test_get_gamma_rate():
    actual = get_gamma_rate(input_strings)

    expected = 22

    assert actual == expected


def test_get_epsilon_rate():
    actual = get_epsilon_rate(input_strings)

    expected = 9

    assert actual == expected

def test_find_oxygen_rating():
    actual = find_oxygen_rating(input_strings)
    
    expected = 23

    assert actual == expected

def test_find_co2_rating():
    actual = find_co2_rating(input_strings)
    
    expected = 10

    assert actual == expected
