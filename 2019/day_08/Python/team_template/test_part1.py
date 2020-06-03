"""
Test part 1.
To run, first, pip or conda install pytest
Then, from the team directory, run `python -m pytest .`
or, if using Cloud9 on AWS, run `python3 -m pytest .`
"""
import numpy as np

from part1 import (
    meaningless_calculation, decode_image, decode_image_using_numpy)
import pytest


def test_meaningless_calculation():
    image_data = '123456789012'
    width = 3
    height = 2
    value = meaningless_calculation(image_data, width, height)
    assert value == 1


def test_meaningless_calculation_1():
    image_data = '123122789012'
    width = 3
    height = 2
    value = meaningless_calculation(image_data, width, height)
    assert value == 6


def test_decode_image():
    image_data = '0222112222120000'
    width = 2
    height = 2
    reference = '01\n10'
    output = decode_image(image_data, width, height)
    assert output == reference


def test_decode_image_using_numpy():
    image_data_string = '0222112222120000'
    image_data = np.array([int(char) for char in image_data_string])
    width = 2
    height = 2
    reference = np.array([0, 1, 1, 0]).reshape(width, height)
    output = decode_image_using_numpy(image_data, width, height)
    assert np.all(output == reference)
