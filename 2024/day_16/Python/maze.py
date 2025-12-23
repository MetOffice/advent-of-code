from queue import PriorityQueue
from typing import NamedTuple, Any, Optional

import numpy as np
from numpy import savetxt


def read_input(filename: str):
    with open(filename) as f:
        input_str = f.read()

    maze = input_str.strip().split("\n")
    print(maze)
    l = [list(line) for line in maze]

    return np.array(l)


def find_start(maze: np.ndarray):
    start_pos = np.where(maze == 'S')
    return start_pos[0][0], start_pos[1][0]


def find_end(maze: np.ndarray):
    end_pos = np.where(maze == 'E')
    return end_pos[0][0], end_pos[1][0]


class Item(NamedTuple):
    cost: int
    position: tuple[int, int]
    direction: tuple[int, int]
    parent: None | tuple["Item"] | tuple["Item", "Item"]


def calculate_costs(maze, item: Item) -> list[Item]:
    current_cost, point, direction, parent = item

    forward = Item(current_cost + 1, (point[0] + direction[0], point[1] + direction[1]), direction, item)
    left = Item(current_cost + 1001, (point[0] - direction[1], point[1] + direction[0]), (-direction[1], direction[0]),
                item)
    right = Item(current_cost + 1001, (point[0] + direction[1], point[1] - direction[0]), (direction[1], -direction[0]),
                 item)

    valid_moves = [x for x in [forward, left, right] if maze[x.position] in '.E']

    return valid_moves


def bfs(maze: np.ndarray, start: tuple[int, int]):
    start_direction = (0, 1) # East

    positions: dict[tuple[int,int], Item] = dict()

    queue: PriorityQueue[Item] = PriorityQueue()
    queue.put(Item(0, start, start_direction, None))

    while True:
        nex = queue.get()
        positions[nex.position] =  nex
        if maze[nex.position] == "E":
            d = debug_view(maze,positions)
            return nex.cost
        possible_paths: list[Item] = calculate_costs(maze, nex)
        for future_pos in possible_paths:
            already_visited_pos = positions.get(future_pos.position,None)

            if future_pos.position not in positions.keys() :
                queue.put(future_pos)
            else:
                print(f"{already_visited_pos.position}={abs(future_pos.cost - already_visited_pos.cost)}")
                if future_pos.cost == already_visited_pos.cost:
                    print(f"TWO PARENTS! {already_visited_pos}")


def debug_view(maze, positions: dict[tuple[int,int], Item]):
    maze2 = maze.astype('<U5')
    for pos in positions.values():
        maze2[pos.position] = pos.cost
    print()
    savetxt("help.csv",maze2,"%s",",")


def main():
    maze = read_input("input")
    start = find_start(maze)
    result = bfs(maze, start)
    print(result)


if __name__ == "__main__":
    main()
