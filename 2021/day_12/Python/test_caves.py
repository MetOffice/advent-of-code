import pytest

from caves import interpret_input, pathfind, pathfind_2
from common import loaders


@pytest.mark.parametrize(["input_", "expected"], [("../test_1.txt", 10), ("../test_2.txt", 19) ])
def test_pathfind(input_, expected):
    input = loaders.load_string(input_)
    caves = interpret_input(input)
    result = pathfind(caves, ["start"])
    assert result == expected


@pytest.mark.parametrize(["input_", "expected"], [("../test_1.txt", 36), ("../test_2.txt", 103)])
def test_pathfind_2(input_, expected):
    input = loaders.load_string(input_)
    caves = interpret_input(input)
    result = pathfind_2(caves, ["start"])
    assert result == expected
