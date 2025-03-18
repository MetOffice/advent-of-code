# type: ignore

import numpy as np

# FIXME problems with looking outside of bounds too early and erroring,
#       need to think about when we do bounds checks

CLOCKWISE = np.array([[0, -1], [1, 0]])


def walk(area, cursor, direction) -> tuple[np.ndarray, np.ndarray, bool]:
    """
    Always takes a step but might have to turn first

    Modifies `area` in place

    Returns (new_cursor, new_position_not_yet_visited)
    """
    next_cursor = cursor + direction

    while area[tuple(next_cursor)] == "#":
        direction = CLOCKWISE @ direction
        next_cursor = cursor + direction

    area[tuple(cursor)] = "X"

    return next_cursor, direction, area[tuple(next_cursor)] == "."


def out_of_bounds(area, cursor) -> bool:
    return any(
        cursor[i] < 0 or cursor[i] >= area.shape[i] for i in range(len(area.shape))
    )


def count_paces(area_str: str) -> int:
    area_list_of_lists = [list(line) for line in area_str.splitlines()[1:]]
    area = np.array(area_list_of_lists)

    (cursor,) = np.argwhere(area == "^")
    direction = np.array([0, -1])

    total_visited = 1
    newly_visited = True

    while not out_of_bounds(area, cursor):
        total_visited += newly_visited
        cursor, direction, newly_visited = walk(area, cursor, direction)

    return total_visited
