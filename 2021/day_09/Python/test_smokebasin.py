import numpy as np

from smokebasin import load_input, part1, part2

test_input = np.array([
    [2,1,9,9,9,4,3,2,1,0],
    [3,9,8,7,8,9,4,9,2,1],
    [9,8,5,6,7,8,9,8,9,2],
    [8,7,6,7,8,9,6,7,8,9],
    [9,8,9,9,9,6,5,6,7,8]
])

def test_loader():
    loaded_input = load_input("./test_input.txt")
    assert np.all(test_input == loaded_input), "Loaded input is not as expected"

def test_part1():
    assert part1(test_input) == 15

def test_part2():
    assert part2(test_input) == 1134