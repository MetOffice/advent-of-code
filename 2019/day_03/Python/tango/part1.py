from typing import List

from load_input import get_input, get_wires

def parse_instruction(item):
    distance = int(item[1:])
    if item[0] == 'R':
        return (1, 0, distance)
    elif item[0] == 'L':
        return (-1, 0, distance)
    elif item[0] == 'U':
         return (0, 1, distance)
    elif item[0] == 'D':
        return (0, -1, distance)
    else:
        raise ValueError(item)
        
def calculate_intermediate_points(start_point, direction):
    intermediate_points_list = [(start_point[0] + n*direction[0], start_point[1] + n*direction[1]) for n in range(1, direction[2]+1)]
    return intermediate_points_list



def calc_closest_intersection(wire_a: List[str], wire_b: List[str]) -> int:
    coordinates_a = [(0, 0)]
    manhattan_distance_list = []
    for instruction in wire_a:
        direction = parse_instruction(instruction)
        coordinates_a += calculate_intermediate_points(coordinates_a[-1], direction)
    start_point = (0, 0)
    coordinates_a = set(coordinates_a)
    for i in range(len(wire_b)):
        instruction = wire_b[i]
        print(i, len(wire_b))
        direction = parse_instruction(instruction)
        coordinates_b = calculate_intermediate_points(start_point, direction)
        start_point = coordinates_b[-1]
        for coordinate in coordinates_b:
            if coordinate in coordinates_a:
                manhattan_distance_list.append(abs(coordinate[0]) + abs(coordinate[1]))
    manhattan_distance = min(manhattan_distance_list)
    return manhattan_distance


if __name__ == "__main__":
    wires = get_wires()
    print(calc_closest_intersection(wires[0], wires[1]))
