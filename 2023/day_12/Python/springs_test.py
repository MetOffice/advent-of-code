import pytest
from springs import calculate_arrangements


@pytest.mark.parametrize(
    "input_string, expected_arrangements",
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ],
)
def test_arrangements(input_string, expected_arrangements):
    # Assuming a function `calculate_arrangements` exists that takes the input string and returns the number of arrangements
    assert calculate_arrangements(input_string) == expected_arrangements