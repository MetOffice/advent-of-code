import pytest
from boarding_passes import convert_binary_to_integer, compute_seat_id


@pytest.mark.parametrize(
    "a_string, zero, one, expected",
    [
        ("FBFBBFF", "F", "B", 44),
        ("BFFFBBF", "F", "B", 70),
        ("FFFBBBF", "F", "B", 14),
        ("BBFFBBF", "F", "B", 102),
        ("RLR", "L", "R", 5),
        ("RRR", "L", "R", 7),
        ("RLL", "L", "R", 4),
    ],
)
def test_convert_binary_to_integer(a_string, zero, one, expected):

    result = convert_binary_to_integer(a_string, zero, one)

    assert result == expected


@pytest.mark.parametrize(
    "boarding_pass,  expected",
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_compute_seat_id(boarding_pass, expected):

    result = compute_seat_id(boarding_pass)

    assert result == expected
