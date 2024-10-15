import collections
from enum import Enum
from typing import Iterable, NamedTuple, Tuple, Dict, Set, List

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Coordinate = collections.namedtuple("Coordinate", ["row", "column", "direction"])
Grid = list[list[str]]


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def opposite(self):
        match self:
            case Direction.NORTH:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.NORTH
            case Direction.EAST:
                return Direction.WEST
            case Direction.WEST:
                return Direction.EAST

    def apply(self, coordinate: Coordinate):
        match self:
            case Direction.NORTH:
                return Coordinate(
                    coordinate.row - 1, coordinate.column, coordinate.direction
                )
            case Direction.SOUTH:
                return Coordinate(
                    coordinate.row + 1, coordinate.column, coordinate.direction
                )
            case Direction.EAST:
                return Coordinate(
                    coordinate.row, coordinate.column + 1, coordinate.direction
                )
            case Direction.WEST:
                return Coordinate(
                    coordinate.row, coordinate.column - 1, coordinate.direction
                )


directions_mapping: dict[str, set[Direction]] = {
    "|": {Direction.NORTH, Direction.SOUTH},
    "-": {Direction.EAST, Direction.WEST},
    "L": {Direction.NORTH, Direction.EAST},
    "J": {Direction.NORTH, Direction.WEST},
    "7": {Direction.SOUTH, Direction.WEST},
    "F": {Direction.SOUTH, Direction.EAST},
}


def load_grid(lines: Iterable[str]) -> list[list[str]]:  # Row,Column
    return [list(i) for i in lines]


def find_start_coordinate(grid: Grid) -> Coordinate:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                return Coordinate(y, x, 1)
    raise Exception("No start found")


def find_start_direction(grid: Grid, position: Coordinate) -> set[Direction]:
    directions = set()
    if grid[position.row + 1][position.column] in "|LJ":  # SOUTH
        directions.add(Direction.SOUTH)
    if grid[position.row - 1][position.column] in "|7F":  # NORTH
        directions.add(Direction.NORTH)
    if grid[position.row][position.column + 1] in "-J7":  # EAST
        directions.add(Direction.EAST)
    if grid[position.row][position.column - 1] in "-FL":  # WEST
        directions.add(Direction.WEST)
    return directions


def next_move(
    grid: Grid, current_position: Coordinate, last_move: Direction
) -> Direction:
    current_shape = grid[current_position.row][current_position.column]
    possible_directions = set(directions_mapping[current_shape])
    possible_directions.remove(last_move.opposite())
    if len(possible_directions) != 1:
        raise ValueError("No or too many possible directions")
    return possible_directions.pop()


def find_longest_distance(grid: Grid) -> int:
    start = find_start_coordinate(grid)
    first_moves = find_start_direction(grid, start)

    directions = list(first_moves)

    coordinates: list[Coordinate] = [
        directions[0].apply(start),
        directions[1].apply(start),
    ]
    moves = 1
    while coordinates[0] != coordinates[1]:
        directions[0] = next_move(grid, coordinates[0], directions[0])
        directions[1] = next_move(grid, coordinates[1], directions[1])
        coordinates[0] = directions[0].apply(coordinates[0])
        coordinates[1] = directions[1].apply(coordinates[1])

        moves += 1

    return moves


def main():
    with open("../input", "r") as f:
        grid = load_grid(f)

    print(find_longest_distance(grid))


if __name__ == "__main__":
    main()
