from guards import iterate_obstacles

INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def test_guards():
    assert iterate_obstacles(INPUT) == 6
