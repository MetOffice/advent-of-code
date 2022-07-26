from vents import input_vents_parser, filter_vents, create_map, calculate_overlap_points
from collections import Counter

def test_input_vents_parser():
    # x1, y1 -> x2, y2
    input_str = '0, 9 -> 5, 9'

    # x1, x2 -> y1, y2
    expected = ((0, 5), (9, 9))
    output = input_vents_parser(input_str)

    assert expected == output


def test_filter_vents():
    input_list = ['0,9 -> 5,9',
                 '8,0 -> 0,8',
                 '9,4 -> 3,4',
                 '2,2 -> 2,1',
                 '7,0 -> 7,4',
                 '6,4 -> 2,0',
                 '0,9 -> 2,9',
                 '3,4 -> 1,4',
                 '0,0 -> 8,8',
                 '5,5 -> 8,2',
                 ]

    expected = [((0, 5), (9, 9)), ((9, 3), (4, 4)), ((2, 2), (2, 1)), ((7, 7), (0, 4)), ((0, 2), (9, 9)), ((3, 1), (4, 4))]

    load_input = [input_vents_parser(input_str) for input_str in input_list]

    output = filter_vents(load_input)

    assert expected == output


def test_create_map_filtered():
    input = [((0, 5), (9, 9)), ((9, 3), (4, 4)), ((2, 2), (2, 1)), ((7, 7), (0, 4)), ((0, 2), (9, 9)), ((3, 1), (4, 4))]

    expected = Counter({(0, 9): 2, (1, 9): 2, (2, 9): 2, (7, 4): 2, (3, 4): 2,
                        (3, 9): 1, (4, 9): 1, (5, 9): 1, (9, 4): 1, (8, 4): 1,
                        (6, 4): 1, (5, 4): 1, (4, 4): 1, (2, 2): 1, (2, 1): 1,
                        (7, 0): 1, (7, 1): 1, (7, 2): 1, (7, 3): 1, (2, 4): 1, (1, 4): 1})
    output = create_map(input)

    assert expected == output


def test_create_map_unfiltered():
    input = [((0, 5), (9, 9)), ((8, 0), (0, 8)), ((9, 3), (4, 4)), ((2, 2), (2, 1)),
             ((7, 7), (0, 4)), ((6, 2), (4, 0)), ((0, 2), (9, 9)), ((3, 1), (4, 4)),
             ((0, 8), (0, 8)), ((5, 8), (5, 2))]
    expected = Counter({(4, 4): 3, (6, 4): 3, (0, 9): 2, (1, 9): 2, (2, 9): 2, (7, 1): 2, (5, 3): 2, (7, 4): 2, (3, 4): 2, (2, 2): 2, (7, 3): 2, (5, 5): 2, (3, 9): 1, (4, 9): 1, (5, 9): 1, (8, 0): 1, (6, 2): 1, (3, 5): 1, (2, 6): 1, (1, 7): 1, (0, 8): 1, (9, 4): 1, (8, 4): 1, (5, 4): 1, (2, 1): 1, (7, 0): 1, (7, 2): 1, (4, 2): 1, (3, 1): 1, (2, 0): 1, (2, 4): 1, (1, 4): 1, (0, 0): 1, (1, 1): 1, (3, 3): 1, (6, 6): 1, (7, 7): 1, (8, 8): 1, (8, 2): 1})
    output = create_map(input)
    assert expected == output


def test_calculate_overlap_points():
    input = Counter({(0, 9): 2, (1, 9): 2, (2, 9): 2, (7, 4): 2, (3, 4): 2,
                        (3, 9): 1, (4, 9): 1, (5, 9): 1, (9, 4): 1, (8, 4): 1,
                        (6, 4): 1, (5, 4): 1, (4, 4): 1, (2, 2): 1, (2, 1): 1,
                        (7, 0): 1, (7, 1): 1, (7, 2): 1, (7, 3): 1, (2, 4): 1, (1, 4): 1})
    expected = 5

    output = calculate_overlap_points(input)
    assert output == expected