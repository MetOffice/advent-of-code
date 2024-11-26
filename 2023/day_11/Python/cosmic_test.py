from cosmic import expand, find_galaxies, all_pairs, Coordinate

input_str = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
expanded_str = """\
....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""


def test_find_galaxies():
    input_grid = [list(i.strip()) for i in input_str.split("\n")]
    result = find_galaxies(input_grid)

    expected_coords = [Coordinate(3, 0), Coordinate(1, 7), Coordinate(2, 0), Coordinate(4, 6), Coordinate(6, 8),
                       Coordinate(8, 6), Coordinate(9, 0), Coordinate(9, 4)]
    assert result == expected_coords


def test_expand():
    input_grid = [list(i.strip()) for i in input_str.split("\n")]
    result = expand(input_grid)

    expected_grid = [list(i.strip()) for i in expanded_str.split("\n")]
    assert result == expected_grid


def test_total():
    input_grid = [list(i.strip()) for i in input_str.split("\n")]
    galaxies = find_galaxies(input_grid)
    expand(input_grid)
    result = all_pairs(galaxies)
    assert result == 374


small_input = """\
..#..
.....
...#.
.....
.....\
"""

def test_small():
    input_grid = [list(i.strip()) for i in small_input.split("\n")]
    galaxies = find_galaxies(input_grid)
    expand(input_grid)
    result = all_pairs(galaxies)
    #assert galaxies == [Coordinate(4,0),Coordinate(5,3)]
    assert result == 4