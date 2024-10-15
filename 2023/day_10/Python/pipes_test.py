from pipes import next_move, Coordinate, Direction, load_grid, find_longest_distance


def test_next_move():
    result = next_move(
        [
            [".", ".", "."],
            ["L", "S", "J"],
            [".", ".", "."],
        ],
        Coordinate(1, 2, 0),
        Direction.EAST,
    )
    assert result == Direction.NORTH


"""
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""


def test_complex_loop():
    grid = load_grid(["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."])

    assert 8 == find_longest_distance(grid)
