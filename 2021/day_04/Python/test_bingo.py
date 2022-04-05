import pytest

from bingo import Board


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (
            """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19""",
            [
                22,
                13,
                17,
                11,
                0,
                8,
                2,
                23,
                4,
                24,
                21,
                9,
                14,
                16,
                7,
                6,
                10,
                3,
                18,
                5,
                1,
                12,
                20,
                15,
                19,
            ],
        )
    ],
)
def test_board_from_text(text, expected):
    board = Board.from_text(text)
    assert board.numbers == expected

def test_load_input():
    """
    Test that the calls list and multiple boards loads successfully
    """
    pass
