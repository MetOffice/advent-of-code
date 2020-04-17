"""
Test part 1.
To run, first, pip or conda install pytest
Then, from the team directory, run `python -m pytest .`
or, if using Cloud9 on AWS, run `python3 -m pytest .`
"""
import pytest
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


"""Following three tests for this example from instructions:

For example, here are several programs that take one input, compare it to the
value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is
equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is
less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is
equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is
less than 8; output 1 (if it is) or 0 (if it is not)."""


@pytest.mark.parametrize(
    "programme",
    (
        ["3", "9", "8", "9", "10", "9", "4", "9", "99", "-1", "8"],
        ["3", "9", "7", "9", "10", "9", "4", "9", "99", "-1", "8"],
        ["3", "3", "1108", "-1", "8", "3", "4", "3", "99"],
        ["3", "3", "1107", "-1", "8", "3", "4", "3", "99"],
    ),
)
@mock.patch("part1.print")
@mock.patch("part1.input", return_value=9)
def test_part2_comparison_examples_with_input_above_8(
    mock_input, mock_print, programme
):
    """All cases, input > 8 => expected of 0"""
    expected = 0

    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    "programme, expected",
    (
        (["3", "9", "8", "9", "10", "9", "4", "9", "99", "-1", "8"], 1),
        (["3", "9", "7", "9", "10", "9", "4", "9", "99", "-1", "8"], 0),
        (["3", "3", "1108", "-1", "8", "3", "4", "3", "99"], 1),
        (["3", "3", "1107", "-1", "8", "3", "4", "3", "99"], 0),
    ),
)
@mock.patch("part1.print")
@mock.patch("part1.input", return_value=8)
def test_part2_comparison_examples_with_input_of_8(
    mock_input, mock_print, programme, expected
):
    """First and third cases expect 1 for input of 8, other cases expect 0"""
    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    "programme, expected",
    (
        (["3", "9", "8", "9", "10", "9", "4", "9", "99", "-1", "8"], 0),
        (["3", "9", "7", "9", "10", "9", "4", "9", "99", "-1", "8"], 1),
        (["3", "3", "1108", "-1", "8", "3", "4", "3", "99"], 0),
        (["3", "3", "1107", "-1", "8", "3", "4", "3", "99"], 1),
    ),
)
@mock.patch("part1.print")
@mock.patch("part1.input", return_value=7)
def test_part2_comparison_examples_with_input_below_8(
        mock_input, mock_print, programme, expected
):
    """First and third cases expect 0 for input < 8, other cases expect 1"""
    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


"""Following two tests for this example from instructions:

Here are some jump tests that take an input, then output 0 if the input was
zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
"""


@pytest.mark.parametrize(
    "programme",
    (
        [
            "3",
            "12",
            "6",
            "12",
            "15",
            "1",
            "13",
            "14",
            "13",
            "4",
            "13",
            "99",
            "-1",
            "0",
            "1",
            "9",
        ],
        ["3", "3", "1105", "-1", "9", "1101", "0", "0", "12", "4", "12", "99", "1"],
    ),
)
@mock.patch("part1.print")
@mock.patch("part1.input", return_value=0)
def test_part2_jump_examples_with_input_0(mock_input, mock_print, programme):
    """All cases, input == 0 => expected of 0"""
    expected = 0

    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    "programme",
    (
        [
            "3",
            "12",
            "6",
            "12",
            "15",
            "1",
            "13",
            "14",
            "13",
            "4",
            "13",
            "99",
            "-1",
            "0",
            "1",
            "9",
        ],
        ["3", "3", "1105", "-1", "9", "1101", "0", "0", "12", "4", "12", "99", "1"],
    ),
)
@mock.patch("part1.print")
@mock.patch("part1.input", return_value=99)
def test_part2_jump_examples_with_input_nonzero(mock_input, mock_print, programme):
    """All cases, input != 0 => expected of 0"""
    expected = 1

    part1.intcode(programme)

    mock_print.assert_called_once_with(expected)


'''Next three tests from this example in the instructions:

Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number.
The program will then output 999 if the input value is below 8, output 1000 if
the input value is equal to 8, or output 1001 if the input value is greater
than 8.
'''
@mock.patch("part1.print")
@mock.patch("part1.input", return_value=7)
def test_part2_input_below_8(mock_input, mock_print):
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
def test_part2_input_of_8(mock_input, mock_print):
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
def test_part2_input_above_8(mock_input, mock_print):
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
