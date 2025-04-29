import inspect
from antinodes import (
    array_from_lines,
    find_antinodes_from_antennas,
    find_antinodes_part_2,
)


def test_antinodes_part_2():
    grid = inspect.cleandoc(
        """
        .......
        .......
        ....A..
        .......
        ..A....
        .......
        .......
        """
    ).strip()

    assert (
        inspect.cleandoc(
            """
            ......#
            .....#.
            ....A..
            ...#...
            ..A....
            .#.....
            #......
            """
        ).strip()
        == find_antinodes_from_antennas(
            find_antinodes_part_2, array_from_lines(grid.split("\n"))
        )
    )
