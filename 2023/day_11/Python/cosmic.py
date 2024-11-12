from collections import namedtuple
from dataclasses import dataclass

Grid = list[list[str]]

def load_file(file_path: str) -> Grid:
    with open(file_path) as file:
        return [list(i.strip()) for i in file]

def row_is_empty(grid: Grid, row: int) -> bool:
    return all(cell == "." for cell in grid[row])

def column_is_empty(grid: Grid, column: int) -> bool:
    return all(row[column] == "." for row in grid)

def expand_grid_rows(grid: Grid) -> Grid:
    new_grid :Grid = []
    for idx, row in enumerate(grid):
        new_grid.append(row)
        if row_is_empty(grid,idx):
            new_grid.append(row)
    return new_grid

def expand(grid: Grid) -> Grid:
    return transpose(expand_grid_rows(transpose(expand_grid_rows(grid))))


def transpose(grid: Grid) -> Grid:
    return [list(x) for x in list(zip(*grid))]

namedtuple("Test",["x","y"])

@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

def find_galaxies(grid: Grid) -> list[Coordinate]:
    coords = []
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "#":
                coords.append(Coordinate(column,row))
    return coords

def distance(coord1: Coordinate, coord2: Coordinate) -> int:
    return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)

def all_pairs(coords: list[Coordinate]) -> int:
    total = 0
    for i in range(len(coords)):
        for j in range(i):
            total+=distance(coords[i],coords[j])
    return total


def main():
    grid = load_file("../input")
    expanded = expand(grid)
    galaxies = find_galaxies(expanded)
    result = all_pairs(galaxies)
    print(result)
    print("Hello, World!")

if __name__ == "__main__":
    main()