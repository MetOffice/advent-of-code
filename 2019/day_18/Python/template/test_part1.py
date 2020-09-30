from load_input import get_input
from unittest.mock import patch, mock_open
from part1 import (
    calculate_digit, calculate_phase, perturb_pattern, calculate_output)

def test_get_input():
    input_data = '12345678'
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual = get_input()
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert actual == expected

def test_calculate_digit():
    input_value = [1, 2, 3, 4, 5, 6, 7, 8]
    pattern = [0, 1, 0, -1]
    output = calculate_digit(input_value, pattern)
    assert output == 4

def test_calculate_phase():
    input_value = [1, 2, 3, 4, 5, 6, 7, 8]
    output = calculate_phase(input_value)
    assert output == [4, 8, 2, 2, 6, 1, 5, 8]

def test_perturb_pattern():
    input_value = [0, 1, 0, -1]
    repetition = 2
    output = perturb_pattern(input_value, repetition)
    assert output == [0, 0, 1, 1, 0, 0, -1, -1]


def test_calculate_output():
    input_value = [1, 2, 3, 4, 5, 6, 7, 8]
    input_repetition = 10
    num_phases = 10
    output = calculate_output(input_value, input_repetition, num_phases)
    expected = [
        0, 4, 8, 5, 3, 5, 7, 1, 5, 0, 8, 5, 8, 5, 2, 0, 1, 7, 2, 1, 1, 0, 4, 1,
        5, 5, 3, 8, 8, 7, 3, 3, 6, 0, 3, 9, 6, 7, 9, 6, 2, 6, 1, 6, 2, 6, 5, 0,
        0, 6, 6, 6, 2, 8, 0, 2, 4, 2, 7, 6, 6, 6, 7, 2, 4, 8, 4, 4, 0, 6, 0, 8,
        8, 6, 9, 4, 0, 6, 7, 8]
    assert output == expected
