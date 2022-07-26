from unittest import mock
import pytest
import numpy as np

from bingo import Board

text = """22 13 17 11  0
          8  2 23  4 24
          21  9 14 16  7
          6 10  3 18  5
          1 12 20 15 19"""

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


def test_mark():
    board = Board.from_text(text)
    board.mark(7)
    assert board.marks[14]


@mock.patch("bingo.Board.check_bingo")
def test_mark_row_and_col(mock_check_bingo):
    board = Board.from_text(text)
    board.mark(7)
    mock_check_bingo.assert_called_once_with(2, 4)


@pytest.mark.parametrize(("start", "stop", "row_to_check", "expected"), [
    (0, 5, 0, True),
    (0, 6, 0, True),
    (5, 10, 1, True),
    (6, 11, 1, False)])
def test_check_bingo_row(start, stop, row_to_check, expected):
    board = Board.from_text(text)
    board.marks[start:stop] = [True] * int((stop - start))
    board.check_bingo(row_to_check, 0)
    assert board.bingo is expected


@pytest.mark.parametrize(("start", "stride", "column_to_check", "expected"), [
    (0, 5, 0, True),
    (5, 5, 1, False)])
def test_check_bingo_column(start, stride, column_to_check, expected):
    board = Board.from_text(text)
    board.marks[start:25:stride] = [True] * int(np.floor((25 - start)/stride))
    board.check_bingo(0, column_to_check)
    assert board.bingo is expected


@pytest.mark.parametrize("final_call, expected", [(1, 237), (2, 474), (10, 2370)])
def test_score(final_call, expected):
    board = Board.from_text(text)
    board.marks[0:5] = [True] * 5
    board.bingo = True
    assert board.score(final_call) == expected


def test_load_input():
    """
    Test that the calls list and multiple boards loads successfully
    """
    pass
