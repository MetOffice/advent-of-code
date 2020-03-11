import sys
sys.path.extend(['../team_chorizo'])

import pytest
from part1 import intcode


def test_case_1():
    input_program = [1, 0, 0, 0, 99]
    expected_output = [2, 0, 0, 0, 99]
    output = intcode(input_program)

    assert output == expected_output


def test_case_2():
    input_program = [2, 3, 0, 3, 99]
    expected_output = [2, 3, 0, 6, 99]
    output = intcode(input_program)

    assert output == expected_output


def test_case_3():
    input_program = [2, 4, 4, 5, 99, 0]
    expected_output = [2, 4, 4, 5, 99, 9801]
    output = intcode(input_program)

    assert output == expected_output


def test_case_4():
    input_program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    expected_output = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    output = intcode(input_program)

    assert output == expected_output


def test_case_5():
    input_program = [1, 1, 1, 3, 1202, 5, 6, 0, 99]
    with pytest.raises(RuntimeError):
        output = intcode(input_program)

