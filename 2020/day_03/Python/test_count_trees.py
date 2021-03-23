import pytest
from toboggan import count_trees, multiply_all_the_trees


input_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")


@pytest.mark.parametrize(
    "right, down, expected", [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)]
)
def test_count_trees(right, down, expected):
    actual = count_trees(input_data, right, down)

    assert actual == expected


def test_multiply_all_the_trees():
    expected = 336

    actual = multiply_all_the_trees(input_data)

    assert actual == expected
