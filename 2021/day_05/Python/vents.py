#from common.loaders import load_string

def main():
    vent_location_lists = load_string()


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


def create_map():
    pass

def calculate_overlap_points():
    pass



