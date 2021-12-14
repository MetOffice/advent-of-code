import pytest
import seats
import layouts


def test_count_occupied_seats():
    layout = seats.process_puzzle_input(layouts.input6)
    expected = 37
    output = seats.count_occupied_seats(layout)
    assert output == expected


@pytest.mark.parametrize(
    "layout,expected",
    [
        [layouts.input1, layouts.input2],
        [layouts.input2, layouts.input3],
        [layouts.input3, layouts.input4],
        [layouts.input4, layouts.input5],
        [layouts.input5, layouts.input6],
    ],
)
def test_apply_rules(layout, expected):
    output = seats.apply_part1_rules(seats.process_puzzle_input(layout))
    processed_expected = seats.process_puzzle_input(expected)
    assert output == processed_expected


@pytest.mark.parametrize(
    "seat_location,expected",
    [
        [(0, 0), [".", "#", "L"]],
        [(3, 5), ["L", ".", ".", ".", "L", ".", "L", "L"]],
        [(4, 0), ["#", "L", ".", "#", "."]],
    ],
)
def test_get_adjacent_seats(seat_location, expected):
    output = seats.get_adjacent_seats(layouts.input3, seat_location)
    assert output == expected


@pytest.mark.parametrize(
    "example_input,seat_location,expected",
    [
        [layouts.part2_example1, (4, 3), ["#", "#", "#", "#", "#", "#", "#", "#"]],
        [layouts.part2_example2, (1, 1), [".", ".", ".", ".", ".", ".", "L", "."]],
        [layouts.part2_example3, (3, 3), [".", ".", ".", ".", ".", ".", ".", "."]],
    ],
)
def test_get_visible_seats(example_input, seat_location, expected):
    output = seats.get_visible_seats(example_input, seat_location)
    assert output == expected
