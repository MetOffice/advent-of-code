from collections import namedtuple
from dataclasses import dataclass
from typing import Literal, LiteralString, List


@dataclass
class Coordinate:
    x: int
    y: int


Grid = list[list[str | Coordinate]]


def load_file(file_path: str) -> Grid:
    with open(file_path) as file:
        return [list(i.strip()) for i in file]


def column_is_empty(grid: Grid, column: int) -> bool:
    return all(row[column] == "." for row in grid)


def offset_all_in_column(grid: Grid, column: int, offset: int,
                         coordinate_to_adjust: Literal["x"] | Literal["y"]) -> None:
    for row in grid:
        if isinstance(row[column], Coordinate):
            if coordinate_to_adjust == "x":
                row[column].x += offset
            else:
                row[column].y += offset


def offset_all_in_row(grid: Grid, row: int, offset: int, coordinate_to_adjust: Literal["x"] | Literal["y"]) -> None:
    for x in grid[row]:
        if isinstance(x, Coordinate):
            if coordinate_to_adjust == "x":
                x.x += offset
            else:
                x.y += offset


def adjust_coordinates(grid: Grid, coordinate_to_adjust: Literal["x"] | Literal["y"]) -> None:
    current_offset = 0
    for idx, row in enumerate(grid):
        if column_is_empty(grid, idx):
            current_offset += 1_000_000 - 1
        else:
            offset_all_in_column(grid, idx, current_offset, coordinate_to_adjust)


def expand(grid: Grid) -> None:
    adjust_coordinates(grid, 'x')
    grid = transpose(grid)
    adjust_coordinates(grid, 'y')


def find_galaxies(grid: Grid) -> list[Coordinate]:
    coords = []
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "#":
                new_coord = Coordinate(column, row)
                grid[row][column] = new_coord
                coords.append(new_coord)
    return coords


def transpose(grid: Grid) -> Grid:
    return [list(x) for x in list(zip(*grid))]


def distance(coord1: Coordinate, coord2: Coordinate) -> int:
    return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)


def all_pairs(coords: list[Coordinate]) -> int:
    total = 0
    for i in range(len(coords)):
        for j in range(i):
            total += distance(coords[i], coords[j])
    return total


def main():
    grid = load_file("../input")
    galaxies = find_galaxies(grid)
    expand(grid)
    result = all_pairs(galaxies)
    print(result)
    print("Hello, World!")


if __name__ == "__main__":
    main()
