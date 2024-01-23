from trebuchet import find_first_n_last_digit, main
import pytest
 
@pytest.mark.parametrize("input_string, result",
[
    ("1abc2",12),
    ("pqr3stu8vwx",38),
    ("a1b2c3d4e5f",15),
    ("treb7uchet",77),
]
)
def test_find_first_n_last_digit(input_string, result):
    '''This is a duck string'''
    answer = find_first_n_last_digit(input_string)
    assert answer == result

@pytest.mark.parametrize("input_string, result",
[
    ("two1nine",29),
    ("eightwothree",83),
    ("abcone2threexyz",13),
    ("xtwone3four",24),
    ("4nineeightseven2",42),
    ("zoneight234",14),
    ("7pqrstsixteen",76),
]
)
def test_find_first_n_last_digit(input_string, result):
    '''This is a duck string'''
    answer = find_first_n_last_digit(input_string)
    assert answer == result
