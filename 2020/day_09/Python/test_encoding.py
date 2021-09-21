import pytest

from encoding import format_input, find_invalid_number, find_chunk, calculate_result

def test_format_input():
    input_values = ['1', '2', '3']
    expected = [1, 2, 3]

    actual = format_input(input_values)

    assert expected == actual

def test_find_invalid_number():
    int_list = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
    expected = 127

    actual = find_invalid_number(int_list, 5)

def test_find_chunk():
    int_list = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
    expected = [15, 25, 47, 40]
    target = 127

    actual = find_chunk(int_list, target)
    
    assert expected == actual

def test_calculate_result():
    int_list = [15, 25, 47, 40]    
    expected = 62

    actual = calculate_result(int_list)

    assert expected == actual
