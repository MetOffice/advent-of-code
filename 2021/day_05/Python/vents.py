from common.loaders import load_string
from collections import Counter


def main():
    vent_location_lists = load_string()
    vents = []
    for vent_location in vent_location_lists:
        vents.append(input_vents_parser(vent_location))

    # filtered_vents = filter_vents(vents)
    map = create_map(vents)
    count = calculate_overlap_points(map)

    print(f"There are {count} overlapping points")


def input_vents_parser(vent_line):
    try:
        first, second = vent_line.split(' -> ')
        x1, y1 = first.split(',')
        x2, y2 = second.split(',')
    except ValueError:
        print(f'Incorrect vent line {vent_line}')

    x_points = (int(x1), int(x2))
    y_points = (int(y1), int(y2))

    return (x_points, y_points)


def filter_vents(vent_tuples):
    vent_filtered_list=[]

    for vent_tuple in vent_tuples:
        vent_x, vent_y = vent_tuple
        vent_x1, vent_x2 = vent_x
        vent_y1, vent_y2 = vent_y

        if vent_x1 == vent_x2 or vent_y1 == vent_y2:
            vent_filtered_list.append(((vent_x1, vent_x2), (vent_y1, vent_y2)))

    return vent_filtered_list


def create_map(filtered_vents):

    # Get all coords between (x1, x2), (y1, y2)
    # sort each tuple so we are always ascending?
    vent_line = []
    count_points = Counter()
    for filtered_vent_pair in filtered_vents:
        x_coords = filtered_vent_pair[0]
        y_coords = filtered_vent_pair[1]
        if x_coords[0] != x_coords[1] and y_coords[0] != y_coords[1]:
            # Have diagonal
            direction = (x_coords[1] - x_coords[0]) // abs(x_coords[1] - x_coords[0])
            x_line_coords = range(x_coords[0], x_coords[1] + direction, direction)
            direction = (y_coords[1] - y_coords[0]) // abs(y_coords[1] - y_coords[0])
            y_line_coords = range(y_coords[0], y_coords[1] + direction, direction)

        elif x_coords[0] != x_coords[1]:
            direction = (x_coords[1] - x_coords[0]) // abs(x_coords[1] - x_coords[0])
            x_line_coords = range(x_coords[0], x_coords[1] + direction, direction)
            y_line_coords = [y_coords[0]] * len(x_line_coords)
        elif y_coords[0] != y_coords[1]:
            direction = (y_coords[1] - y_coords[0]) // abs(y_coords[1] - y_coords[0])
            y_line_coords = range(y_coords[0], y_coords[1] + direction, direction)
            x_line_coords = [x_coords[0]] * len(y_line_coords)
        else:
            "we have a single point!"
            x_line_coords = [x_coords[0]]
            y_line_coords = [y_coords[0]]

        coords = zip(x_line_coords, y_line_coords)

        # assign to counter object/thing
        count_points.update(coords)

    return count_points


def calculate_overlap_points(count_points):
    overlap_points = [value for value in count_points.values() if value >= 2]
    count_overlaps = len(overlap_points)

    return count_overlaps


if __name__ == "__main__":
    main()

