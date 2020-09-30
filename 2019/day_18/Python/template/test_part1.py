from load_input import get_input
from unittest.mock import patch, mock_open
from part1 import count_steps, Solver


def test_get_input():
    input_data = """#########
#b.A.@.a#"""
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual = get_input()
    expected = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "b", ".", "A", ".", "@", ".", "a", "#"],
    ]
    assert actual == expected


def test_example_1():
    expected = 8

    input_data = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "b", ".", "A", ".", "@", ".", "a", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    actual = count_steps(input_data)

    assert actual == expected


def test_find_visible_keys_for_example_1():
    expected = [
        "a",
    ]

    input_data = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "b", ".", "A", ".", "@", ".", "a", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    solver = Solver(input_data)
    actual = solver._find_visible_keys()

    assert actual == expected


def test_find_at_for_example_1():
    expected = (1, 5)

    input_data = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "b", ".", "A", ".", "@", ".", "a", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    solver = Solver(input_data)
    solver._find_at()
    actual = solver.current_position

    assert actual == expected
