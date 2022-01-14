from rainrisk_jam import manhattan_distance
import pytest

def test_manhattan():
    testinput = ['F10', 'N3', 'F7', 'R90', 'F11']
    expected = 25
    actual = manhattan_distance(testinput)
    assert expected == actual

test_manhattan()