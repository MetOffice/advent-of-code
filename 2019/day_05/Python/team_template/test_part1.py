"""
Test part 1.
To run, first, pip or conda install pytest
Then, from the team directory, run `python -m pytest .`
or, if using Cloud9 on AWS, run `python3 -m pytest .`
"""
from unittest import mock

from load_input import get_input
import part1


# patch input() and print() builtins
@mock.patch("part1.print")
@mock.patch("part1.input")
def test_input_output(mock_input, mock_print):
    program = ["3", "0", "4", "0", "99"]
    input_ = 1234
    mock_input.return_value = input_
    part1.intcode(program)
    mock_input.assert_called_once()
    mock_print.assert_called_once_with(input_)


def test_access_modes_simple():
    input_ = ["1002", "4", "3", "4", "33"]
    expected = [1002, 4, 3, 4, 99]
    end_state = part1.intcode(input_)
    assert end_state == expected


@mock.patch("part1.print")
@mock.patch("part1.input", return_value="1")
def test_run_diagnostic(mock_input, mock_print):
    part1.intcode(get_input())
    # should get input once
    assert mock_input.call_count == 1
    # Every diagnostic except the last should be 0
    assert len(mock_print.call_args_list) > 1
    for call in mock_print.call_args_list[:-1]:
        assert call == mock.call(0) or call == mock.call("0")
    assert mock_print.call_args_list[-1] != mock.call(0)
    assert mock_print.call_args_list[-1] != mock.call("0")


def test_negative_number():
    input_ = ["1101", "100", "-1", "4", "0"]

    expected = [1101, 100, -1, 4, 99]
    actual = part1.intcode(input_)

    assert actual == expected


# @mock.patch('part1.input', return_value=0)
# def test_part2_example1():
#     programme = ["3","12","6","12","15","1","13","14","13","4","13","99","-1","0","1","9"]
#     expected = 0
#
#     actual = part1.intcode(programme)
#
#     assert actual == expected
#
# @mock.patch('part1.input', return_value=99)
# def test_part2_example2():
#     programme = ["3","12","6","12","15","1","13","14","13","4","13","99","-1","0","1","9"]
#     expected = 1
#
#     actual = part1.intcode(programme)
#
#     assert actual == expected
#
# @mock.patch('part1.input', return_value=0)
# def test_part2_example3():
#     programme = ["3","3","1105","-1","9","1101","0","0","12","4","12","99","1"]
#     expected = 0
#
#     actual = part1.intcode(programme)
#
#     assert actual == expected
#
# @mock.patch('part1.input', return_value=99)
# def test_part2_example4():
#     programme = ["3","3","1105","-1","9","1101","0","0","12","4","12","99","1"]
#     expected = 1
#
#     actual = part1.intcode(programme)
#
#     assert actual == expected


@mock.patch("part1.print")
@mock.patch("part1.input", return_value=7)
def test_part2_example5(mock_input, mock_print):
    programme = [
        "3",
        "21",
        "1008",
        "21",
        "8",
        "20",
        "1005",
        "20",
        "22",
        "107",
        "8",
        "21",
        "20",
        "1006",
        "20",
        "31",
        "1106",
        "0",
        "36",
        "98",
        "0",
        "0",
        "1002",
        "21",
        "125",
        "20",
        "4",
        "20",
        "1105",
        "1",
        "46",
        "104",
        "999",
        "1105",
        "1",
        "46",
        "1101",
        "1000",
        "1",
        "20",
        "4",
        "20",
        "1105",
        "1",
        "46",
        "98",
        "99",
    ]

    expected = 999

    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


@mock.patch("part1.print")
@mock.patch("part1.input", return_value=8)
def test_part2_example6(mock_input, mock_print):
    programme = [
        "3",
        "21",
        "1008",
        "21",
        "8",
        "20",
        "1005",
        "20",
        "22",
        "107",
        "8",
        "21",
        "20",
        "1006",
        "20",
        "31",
        "1106",
        "0",
        "36",
        "98",
        "0",
        "0",
        "1002",
        "21",
        "125",
        "20",
        "4",
        "20",
        "1105",
        "1",
        "46",
        "104",
        "999",
        "1105",
        "1",
        "46",
        "1101",
        "1000",
        "1",
        "20",
        "4",
        "20",
        "1105",
        "1",
        "46",
        "98",
        "99",
    ]

    expected = 1000

    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


@mock.patch("part1.print")
@mock.patch("part1.input", return_value=9)
def test_part2_example7(mock_input, mock_print):
    programme = [
        "3",
        "21",
        "1008",
        "21",
        "8",
        "20",
        "1005",
        "20",
        "22",
        "107",
        "8",
        "21",
        "20",
        "1006",
        "20",
        "31",
        "1106",
        "0",
        "36",
        "98",
        "0",
        "0",
        "1002",
        "21",
        "125",
        "20",
        "4",
        "20",
        "1105",
        "1",
        "46",
        "104",
        "999",
        "1105",
        "1",
        "46",
        "1101",
        "1000",
        "1",
        "20",
        "4",
        "20",
        "1105",
        "1",
        "46",
        "98",
        "99",
    ]

    expected = 1001

    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)
