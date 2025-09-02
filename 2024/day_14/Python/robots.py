import dataclasses
import re


# 101 tiles wide and 103 tiles tall

WIDTH = 101
HEIGHT = 103

@dataclasses.dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int

    def position_after(self, seconds: int) -> tuple[int, int]:
        return (
            (self.x + self.vx * seconds) % WIDTH ,
            (self.y + self.vy * seconds) % HEIGHT
        )


def load_file(input_file: str) -> list[Robot]:
    regex = r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)"
    robots: list[Robot] = []
    with open(input_file, 'r') as in_file:
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
            match (x,y):
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
    robots = load_file("./input")
    final_posistions = [ robot.position_after(100) for robot in robots]
    print_robots(final_posistions)
    count_quadrant(make_robot_grid(final_posistions))
    print(len(robots))

def make_robot_grid(robots):
    grid = [ [0]*WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        grid[robot[1]][robot[0]] = grid[robot[1]][robot[0]] + 1
    return grid

def print_robots(robots):
    grid = make_robot_grid(robots)
    for thing in grid:
        print("".join([str(thingy) if thingy > 0 else "." for thingy in thing]))

if __name__ == "__main__":
    main()

