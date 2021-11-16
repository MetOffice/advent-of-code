import copy

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
    layout_size_x = len(seat_layout[0])
    layout_size_y = len(seat_layout)

    seat_location_x = seat_location[0]
    seat_location_y = seat_location[1]

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

def apply_rules(seat_layout):
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
    pass