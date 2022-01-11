from solution import (
    count_depth_increases,
    count_depth_increases_zip,
    count_depth_increases_smoothed,
    smooth_depths,
    smooth_depths_toolz,
)

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
