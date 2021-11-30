#!/usr/bin/env python
import copy
from common import loaders


def process_puzzle_input(puzzle_input):
    """
    Converts our raw puzzle_input into required format
    """
    # puzzle_input is a list of strings
    # return list of list of strings (1-char strings)
    return [list(string) for string in puzzle_input]

def count_occupied_seats(puzzle_input):
    """
    In a given seat configuration, find the number of occupied seats.
    """
    return sum([row.count('#') for row in puzzle_input])

def get_adjacent_seats(seat_layout, seat_location):
    """
    Given a seat_layout and a seat_location, return a list of seat 'chars'.
    """
    seat_location_x, seat_location_y = seat_location

    # find adjacent seats by loop
    adjacent_seats = []

    seat_x = max(seat_location_x - 1, 0)
    seat_y = max(seat_location_y - 1, 0)
    for x in range(seat_x, seat_location_x + 2):
        for y in range(seat_y, seat_location_y + 2):
            if (x != seat_location_x or y != seat_location_y): # don't count the seat we're on!!
                try:
                    adjacent_seats.append(seat_layout[x][y])
                except IndexError:
                    pass

    return adjacent_seats


# Add apply rules for part2
# new function for get_visible_seats
def get_visible_seats(seat_layout, seat_location):
    """
    Given a seat_layout and a seat_location, return a list of seat 'chars' of
    first visible seat in each direction.  Seats returned north west first,
    and raster order.

    """
    seat_location_x, seat_location_y = seat_location

    # find visible seats by loop
    visible_seats = ['.', '.', '.', '.', '.', '.', '.', '.']

    for n in range(1, max(len(seat_layout), len(seat_layout[0])) + 1):
        # stop condition?
        seat_x = max(seat_location_x - n, 0)
        seat_y = max(seat_location_y - n, 0)

        for x in range(seat_x, seat_location_x + n + 1, n):
            for y in range(seat_y, seat_location_y + n + 1, n):
                if (x != seat_location_x or y != seat_location_y): # don't count the seat we're on!!
                    try:
                        # only update visible seats if it's a floor
                        direction_index = (n-1) % 8
                        if visible_seats[direction_index] == '.':
                            visible_seats[direction_index] = seat_layout[x][y]
                        print(f"where we are: {x, y} seat layout: {seat_layout[x][y]}")
                    except IndexError:
                        pass
                if '.' not in visible_seats:
                    return visible_seats
    return visible_seats


def apply_part1_rules(seat_layout):
    """
    Apply rules once to the seat configuration.
    """
    new_seat_layout = copy.deepcopy(seat_layout)

    for row_index, row in enumerate(seat_layout):

        for col_index, seat in enumerate(row):
            adjacent_seats = get_adjacent_seats(seat_layout, (row_index, col_index))
            number_of_occupied_seats = adjacent_seats.count('#')
            if seat == 'L' and number_of_occupied_seats == 0:
                new_seat = '#'
            elif seat == '#' and number_of_occupied_seats >= 4:
                new_seat = 'L'
            else:
                new_seat = seat
            #print(new_seat_layout[row_index])
            new_seat_layout[row_index][col_index] = new_seat

    return new_seat_layout


def run(initial_seat_layout):
    """
    Apply rules until the configuration reaches 'equilbrium' - applying the rules again changes nothing
    """
    # iterate apply rules until seat layout doesn't change
    previous_layout = initial_seat_layout
    new_layout = apply_part1_rules(initial_seat_layout)
    while new_layout != previous_layout:
        previous_layout = new_layout
        new_layout = apply_part1_rules(previous_layout)
    return new_layout


if __name__ == "__main__":
    # load initial seat layout and run
    initial_layout = loaders.load_string()
    initial_layout = process_puzzle_input(initial_layout)
    final_layout = run(initial_layout)
    number_of_seats = count_occupied_seats(final_layout)
    print(f'Part 1: {number_of_seats}')
