import pytest
import adapters


def test_find_chain():
    adapters_list = "16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4".strip().split(",")
    output = adapters.find_chain(adapters_list)
    expected = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    assert output == expected


def test_find_jolt_distribution():
    input = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    output = adapters.find_jolt_distribution(input)
    expected = [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    assert output == expected


def test_count_jolt_distribution():
    input = [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    output = adapters.count_jolt_distribution(input)
    expected = (7, 0, 5)
    assert output == expected


def test_count_combinations():
    input = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    combinations = adapters.count_combinations(input)
    expected = 8
    assert combinations == expected



@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (1, 2, True),
        (1, 3, True),
        (3, 6, True),
        (0, 2, True),
        (3, 7, False),
        (0, 5, False),
        (21, 42, False),
    ]
)
def test_is_valid_jolt(input1, input2, expected):
    output = adapters.is_valid_jolt(input1, input2)
    assert output == expected


SMALL_INPUT = "16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4".strip().split(",")
LARGE_INPUT = (
    "28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, "
    "11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3".strip().split(","))

@pytest.mark.parametrize(
    "input, expected",
    [
        (LARGE_INPUT, 220),
        (SMALL_INPUT, 7 * 5),
    ]
)
def test_main_part1(input, expected):
    output = adapters.main_part1(input=input)
    assert output == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (SMALL_INPUT, 8),
        (LARGE_INPUT, 19208),
    ]
)
def test_main_part2(input, expected):
    output = adapters.main_part2(input=input)
    assert output == expected
