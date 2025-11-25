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
    parents: list["Item"]


def calculate_valid_moves_and_costs(maze, thingy: Item) -> list[Item]:
    current_cost, point, direction, parent = thingy

    forward = Item(current_cost + 1, (point[0] + direction[0], point[1] + direction[1]), direction, [thingy])
    left = Item(current_cost + 1001, (point[0] - direction[1], point[1] + direction[0]), (-direction[1], direction[0]),
                [thingy])
    right = Item(current_cost + 1001, (point[0] + direction[1], point[1] - direction[0]), (direction[1], -direction[0]),
                 [thingy])

    valid_moves = [x for x in [forward, left, right] if maze[x.position] in '.E']

    return valid_moves



def bfs(maze: np.ndarray, start: tuple[int, int]):
    start_direction = (0, 1)
    visited_2 : dict[tuple[int, int], Item] = {}
    queue: PriorityQueue[Item] = PriorityQueue()
    queue.put(Item(0, start, start_direction, None))

    while True:
        current_item = queue.get()
        visited_2[current_item.position] = current_item
        if maze[current_item.position] == "E":
            return current_item
        moves = calculate_valid_moves_and_costs(maze, current_item)
        for move in moves:
            assert move.cost >= current_item.cost
            if move.position not in visited_2.keys():
                queue.put(move)
            elif abs(visited_2.get(move.position).cost - move.cost) in [1000,0,1]:
                print(f"SPLIT!{visited_2.get(move.position).cost}=?{move.cost},{move.position}")
                f = visited_2[move.position].parents
                f.append(current_item)
            else:
                print(f"     {visited_2.get(move.position).cost}=?{move.cost},{move.position}")

def traceback(item: Item) -> list[Item]:
    if item.parents is None:
        return [item]
    r = []
    r.extend(item.parents)
    print(len(item.parents))
    for i in item.parents:
        t = traceback(i)
        r.extend(t)
    return r


def main():
    maze = read_input("input")
    start = find_start(maze)
    result = bfs(maze, start)

    visited = set(i.position for i in traceback(result))

    print(len(visited))


if __name__ == "__main__":
    main()
