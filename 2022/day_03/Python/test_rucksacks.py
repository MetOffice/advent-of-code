import pytest

from .rucksacks import *

@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp", "p"),
    ]
)
def test_get_common_item(a, b, expected):
    assert get_common_item(a, b) == expected

def test_find_answer():
    assert find_answer("day_03/sample_input.txt") == 157


def test_find_answer_2():
    assert find_answer_2("day_03/sample_input.txt") == 70
