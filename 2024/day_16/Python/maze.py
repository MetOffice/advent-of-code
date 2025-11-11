from queue import PriorityQueue

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


def calculate_costs(maze, thingy):
    current_cost, point, direction = thingy

    forward = (current_cost + 1, (point[0] + direction[0], point[1] + direction[1]), direction)
    left = (current_cost + 1001, (point[0] - direction[1], point[1] + direction[0]), (-direction[1], direction[0]))
    right = (current_cost + 1001, (point[0] + direction[1], point[1] - direction[0]), (direction[1], -direction[0]))

    valid_moves = [x for x in [forward, left, right] if maze[x[1]] in '.E']

    return valid_moves


def bfs(maze: np.ndarray, start: tuple, end: tuple):
    start_direction = (0, 1)
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, start_direction))

    while True:
        nex = queue.get()
        visited.add(nex[1])
        if maze[nex[1]] == "E":
            return nex[0]
        thing = calculate_costs(maze, nex)
        [queue.put(t) for t in thing if t[1] not in visited]


def main():
    maze = read_input("input")
    start = find_start(maze)
    end = find_end(maze)
    result = bfs(maze, start, end)
    print(result)


if __name__ == "__main__":
    main()
