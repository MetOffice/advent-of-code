import pytest
from red_nosed import check_report

#More of the above example's reports are now safe:

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.


@pytest.mark.parametrize(
    "input_report, is_safe",
    [
        ([7, 6, 4, 2, 1], "SAFE"),
        ([1, 2, 7, 8, 9], "UNSAFE"),
        ([9, 7, 6, 2, 1], "UNSAFE"),
        ([1, 3, 2, 4, 5], "SAFE"),
        ([8, 6, 4, 4, 1], "SAFE"),
        ([1, 3, 6, 7, 9], "SAFE"),
        ([5,1,2,3,4], "SAFE"),
        ([2,1,2,3,4], "SAFE"),
    ],
)
def test_pt2(input_report, is_safe):
    # Assuming a function `calculate_arrangements` exists that takes the input string and returns the number of arrangements
    assert check_report(input_report) == is_safe

def test():
    assert check_report([2,1,2,3,4]) == "SAFE"