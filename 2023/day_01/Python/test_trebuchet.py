from trebuchet import find_first_n_last_digit
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
