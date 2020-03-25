"""
Test part 1.
To run, first, pip or conda install pytest
Then, from the team directory, run `python -m pytest .`
or, if using Cloud9 on AWS, run `python3 -m pytest .`
"""
import pytest

from part1 import is_valid_password


@pytest.mark.parametrize("password, expected",
    [
        ("111111", True),
        ("223450", False),
        ("123789", False),
    ]
)
def test_password_validator(password, expected):
    assert is_valid_password(password) == expected
