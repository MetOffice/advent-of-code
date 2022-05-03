from vents import input_vents_parser, filter_vents, create_map, calculate_overlap_points

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


