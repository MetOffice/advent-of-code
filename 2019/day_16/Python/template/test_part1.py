from load_input import get_input
from unittest.mock import patch, mock_open
from part1 import calculate_digit, calculate_phase, perturb_pattern

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
