"""
Test part 2.
To run, first, pip or conda install pytest
Then, from the team directory, run `python -m pytest .`
or, if using Cloud9 on AWS, run `python3 -m pytest .`
"""
import pytest

from part2 import is_valid_password


@pytest.mark.parametrize("password, expected",
    [
        ("111111", False),
        ("223450", False),
        ("123789", False),
        ("840000", False),
        ("112233", True),
        ("123444", False),
        ("111122", True),
        ("111123", False),

    ]
)
def test_password_validator(password, expected):
    assert is_valid_password(password) == expected
