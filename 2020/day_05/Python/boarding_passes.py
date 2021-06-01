from common.loaders import load_string


def convert_binary_to_integer(a_string, zero="F", one="B"):
    """
    Converts a string of letters to an integer,
    assuming one letter is 0 and one is 1 and interpreting it as binary.

    Parameters
    ----------
    a_string: str
        A string comprising the letters given in zero and one
    zero: char
        The letter to convert to zeros
    one: char
        The letter to convert to ones

    Returns
    -------
    int
        The integer corresponding to the string (a_string)

    """

    a_string = a_string.replace(zero, "0").replace(one, "1")

    decimal = int(a_string, base=2)

    return decimal


def compute_seat_id(boarding_pass: str) -> int:
    """

    Parameters
    ----------
    boarding_pass:
        A boarding pass string

    Returns
    -------
    :
        The seat id as an integer

    """

    row = boarding_pass[0:7]
    column = boarding_pass[7:]

    row_int = convert_binary_to_integer(row)
    column_int = convert_binary_to_integer(column, zero="L", one="R")

    return row_int * 8 + column_int


def part1():
    maximum_seat_id = 0

    for boarding_pass in load_string():
        seat_id = compute_seat_id(boarding_pass)
        maximum_seat_id = max(seat_id, maximum_seat_id)

    return maximum_seat_id


def part2():

    seats = set()

    for boarding_pass in load_string():
        seat_id = compute_seat_id(boarding_pass)
        seats.add(seat_id)

    all_seats = set(range(min(seats), max(seats) + 1))

    my_seat = all_seats - seats
    if len(my_seat) != 1:
        raise ValueError(f"Your butt does not need {len(my_seat)} seats!")

    my_seat = my_seat.pop()

    return my_seat


if __name__ == "__main__":
    print(f"Dear Roddy, the answer to part 1 is {part1()}, Regards, The elves")
    print(f"Dear Roddy, the answer to part 2 is {part2()}, Regards, The elves")
