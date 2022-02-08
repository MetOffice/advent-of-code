from solution_day02 import (
    
)

SAMPLE_INPUT_day02 = _input = [
forward 5,
down 5,
forward 8,
up 3,
down 8,
forward 2,
]


def test_part1_day02():
    expected =150
    assert multiply_depth_and_hposition(SAMPLE_INPUT_day02) == expected


# below from day01
SAMPLE_INPUT = _input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_part1():
    expected = 7
    assert count_depth_increases(SAMPLE_INPUT) == expected

def test_part1_zip_approach():
    expected = 7
    assert count_depth_increases_zip(SAMPLE_INPUT) == expected


def test_smooth_depths():
    expected = [607, 618, 618, 617, 647, 716, 769, 792]
    assert smooth_depths(SAMPLE_INPUT) == expected


def test_smooth_depths_toolz():
    expected = [607, 618, 618, 617, 647, 716, 769, 792]
    assert smooth_depths_toolz(SAMPLE_INPUT) == expected


def test_part2():
    expected = 5
    assert count_depth_increases_smoothed(SAMPLE_INPUT) == expected
