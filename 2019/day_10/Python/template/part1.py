import math
from pathlib import Path


def get_input():
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_list = file.readlines()

    input_list = [line.strip() for line in input_list]
    return input_list


def find_angle(origin, destination):
    xdiff = destination[0] - origin[0]
    # Puzzle defines positive y as downwards.
    ydiff = origin[1] - destination[1]

    if xdiff == 0 and ydiff == 0:
        result = None
    else:
        # atan2 returns b/w -pi and pi
        radians = math.atan2(ydiff, xdiff) + math.pi
        # * 100 prior to cast and then / 100 to workaround for precision issues.
        result = int(math.degrees(radians) * 100) / 100.

    return result


def map_to_positions(input_map):
    result = list()
    for y_index, line in enumerate(input_map):
        for x_index, character in enumerate(line):
            if character == '#':
                result.append((x_index, y_index))
    return result


def visible_asteroid_count(position, position_map):
    angles = set()
    for destination in position_map:
        angle = find_angle(position, destination)
        if angle is not None:
            angles.add(angle)
    return len(angles)


def main():
    input_list = get_input()
    position_map = map_to_positions(input_list)
    maximum_asteroid_count = 0
    for position in position_map:
        asteroid_count = visible_asteroid_count(position, position_map)
        if asteroid_count > maximum_asteroid_count:
            maximum_asteroid_count = asteroid_count
    return maximum_asteroid_count


if __name__ == '__main__':
    result = main()
    print(result)
