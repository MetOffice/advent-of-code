import pytest

from encoding import format_input, validate

def test_format_input():
    input_values = ['1', '2', '3']
    expected = [1, 2, 3]

    actual = format_input(input_values)

    assert expected == actual

def test_validate():
    int_list = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
    expected = 127

    actual = validate(int_list, 5)

    assert expected == actual
