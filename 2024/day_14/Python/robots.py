import dataclasses
import os
import re
from typing import Self, Sequence


# 101 tiles wide and 103 tiles tall

WIDTH = 101
HEIGHT = 103


@dataclasses.dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int

    def position_after(self, seconds: int) -> Self:
        return dataclasses.replace(
            self,
            x=(self.x + self.vx * seconds) % WIDTH,
            y=(self.y + self.vy * seconds) % HEIGHT,
        )


def load_file(input_file: str) -> list[Robot]:
    regex = r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)"
    robots: list[Robot] = []
    with open(input_file, "r") as in_file:
        lines = in_file.readlines()
        for line in lines:
            (x, y, vx, vy) = re.findall(regex, line.strip())[0]
            robots.append(Robot(int(x), int(y), int(vx), int(vy)))

    return robots


def count_quadrant(grid: list[list[int]]):
    x_bound = WIDTH // 2
    y_bound = HEIGHT // 2

    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0

    for x in range(WIDTH):
        for y in range(HEIGHT):
            match (x, y):
                case _ if x < x_bound and y < y_bound:
                    top_left += grid[y][x]
                case _ if x < x_bound and y > y_bound:
                    bottom_left += grid[y][x]
                case _ if x > x_bound and y > y_bound:
                    bottom_right += grid[y][x]
                case _ if x > x_bound and y < y_bound:
                    top_right += grid[y][x]

    print(f"Top Left: {top_left}")
    print(f"Top Right: {top_right}")
    print(f"Bottom Left: {bottom_left}")
    print(f"Bottom Right: {bottom_right}")
    result = top_left * top_right * bottom_left * bottom_right
    print(f"Result: {result}")


def main():
    # Part 1
    robots = load_file("./input")
    final_posistions = [robot.position_after(100) for robot in robots]
    print_robots(final_posistions)
    count_quadrant(make_robot_grid(final_posistions))
    print(len(robots))

    # Part 2
    positions = [robot.position_after(13) for robot in robots]
    index = 13
    h = 52
    v = 49
    while True:
        # os.system("cls" if os.name == "nt" else "clear")
        print_robots(positions)
        print("*** ", index, " ***")
        positions = [robot.position_after(h) for robot in positions]
        index += h
        h += 2
        input()

        print_robots(positions)
        print("*** ", index, " ***")
        positions = [robot.position_after(v) for robot in positions]
        index += v
        v -= 2
        input()


def make_robot_grid(robots: Sequence[Robot]):
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        grid[robot.y][robot.x] = grid[robot.y][robot.x] + 1
    return grid


def print_robots(robots):
    grid = make_robot_grid(robots)
    for thing in grid:
        print("".join([str(thingy) if thingy > 0 else "." for thingy in thing]))


if __name__ == "__main__":
    main()
