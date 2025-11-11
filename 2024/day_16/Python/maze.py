from queue import PriorityQueue
from typing import NamedTuple, Any, Optional

import numpy as np


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
    parent: Optional["Item"]


def calculate_costs(maze, thingy: Item) -> list[Item]:
    current_cost, point, direction, parent = thingy

    forward = Item(current_cost + 1, (point[0] + direction[0], point[1] + direction[1]), direction, thingy)
    left = Item(current_cost + 1001, (point[0] - direction[1], point[1] + direction[0]), (-direction[1], direction[0]),
                thingy)
    right = Item(current_cost + 1001, (point[0] + direction[1], point[1] - direction[0]), (direction[1], -direction[0]),
                 thingy)

    valid_moves = [x for x in [forward, left, right] if maze[x.position] in '.E']

    return valid_moves


def bfs(maze: np.ndarray, start: tuple[int, int]):
    start_direction = (0, 1)
    visited = set()
    queue: PriorityQueue[Item] = PriorityQueue()
    queue.put(Item(0, start, start_direction, None))

    while True:
        nex = queue.get()
        visited.add(nex.position)
        if maze[nex.position] == "E":
            return nex.cost
        things = calculate_costs(maze, nex)
        [queue.put(t) for t in things if t.position not in visited]


def main():
    maze = read_input("input")
    start = find_start(maze)
    result = bfs(maze, start)
    print(result)


if __name__ == "__main__":
    main()
