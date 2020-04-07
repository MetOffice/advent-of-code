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
    program = ["3","0","4","0","99"]
    input_ = "1234"
    mock_input.return_value = input_
    part1.intcode(program)
    mock_input.assert_called_once()
    mock_print.assert_called_once_with(input_)


def test_access_modes_simple():
    input_ = ["1002","4","3","4","33"]
    expected = ["1002", "4", "3", "4", "99"]
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
        assert (call == mock.call(0) or call == mock.call("0"))
    assert mock_print.call_args_list[-1] != mock.call(0)
    assert mock_print.call_args_list[-1] != mock.call("0")
