import numpy as np

from crabs import calculate_fuel_consumption_pt1
from crabs import calculate_fuel_consumption_pt2


def test_calculate_fuel_consumption():
    input = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    median = np.median(input)
    result = calculate_fuel_consumption_pt1(input, median)

    assert result == 37


def test_calculate_fuel_consumption2():
    input = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    mean = np.round(np.mean(input))
    result = calculate_fuel_consumption_pt2(input, mean)

    assert result == 168

