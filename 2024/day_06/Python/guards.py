# type: ignore

import numpy as np

# FIXME problems with looking outside of bounds too early and erroring,
#       need to think about when we do bounds checks

CLOCKWISE = np.array([[0, 1], [-1, 0]])


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


def has_loop(area) -> int:
    direction = np.array([-1, 0])

    total_visited = 0
    newly_visited = True
    visited_set = set()
    (cursor,) = np.argwhere(area == "^")



    while not (area[tuple(cursor)] == "_" or (tuple(cursor),tuple(direction)) in visited_set):
        visited_set.add((tuple(cursor),tuple(direction)))
        total_visited += newly_visited
        cursor, direction, newly_visited = walk(area, cursor, direction)

    return (tuple(cursor),tuple(direction)) in visited_set

def iterate_obstacles(area_str: str):
    area_list_of_lists = [list(line) for line in area_str.splitlines()[1:]]
    area = np.array(area_list_of_lists)
    area_padded = np.pad(area,1, "constant",constant_values='_')
    loops = 0

    for x_pos in range(1, area_padded.shape[0]-1):
        for y_pos in range(1, area_padded.shape[1]-1):
            area_copy = area_padded.copy()
            # print(x_pos, y_pos)
            if area_padded[(x_pos, y_pos)] == "^":
                print("HELP ME")
            else:
                area_copy[(x_pos,y_pos)] = "#"
                if has_loop(area_copy):
                    loops+=1
        print(x_pos)

    return loops


def main():
    with open("input","r") as f:
        data = f.read()
    print(iterate_obstacles(data))


if __name__ == "__main__":
    main()