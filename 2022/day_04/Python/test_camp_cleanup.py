import pytest

from camp_cleanup import check_inside, check_overlap

test_elfs = [((2, 4), (6, 8)),
             ((2, 3), (4, 5)),
             ((5, 7), (7, 9)),
             ((2, 8), (3, 7)),
             ((6, 6), (4, 6)),
             ((2, 6), (4, 8)),
             ]


@pytest.mark.parametrize("elf0, elf1, expected", [((2, 4), (6, 8), False),
                                                  ((2, 3), (4, 5), False),
                                                  ((6, 6), (4, 6), True)])
def test_check_inside(elf0, elf1, expected):
    result = check_inside(elf0, elf1)

    assert result == expected


@pytest.mark.parametrize("elf0, elf1, expected", [((2, 4), (6, 8), False),
                                                  ((2, 3), (4, 5), False),
                                                  ((6, 6), (4, 6), True),
                                                  ((2, 8), (3, 7), False),
                                                  ((6, 6), (4, 6), True),
                                                  ((2, 6), (4, 8), True)])
def test_check_overlap(elf0, elf1, expected):
    result = check_overlap(elf0, elf1)

    assert expected == result