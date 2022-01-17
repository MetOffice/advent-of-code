import numpy as np

def load_file_complete():
    """
    Loads the file as a single string
    """
    with open("./2020/day_16/input.txt", "r") as file:
        content = file.read()
    return content

def read_policy(line:str):
    """
    Interpret a string as a fild policy line.
    These have format "name: xx-xx or xx-xx"
    """
    name, policy = line.split(":")
    range_a, range_b = policy.split("or")
    low_a, high_a = range_a.split("-")
    low_b, high_b = range_b.split("-")

    return name, int(low_a), int(high_a), int(low_b), int(high_b)

def read_ticket(line:str):
    """
    Interpret a string as a ticket
    A ticket is a list of comma seperated ints
    """
    numbers = line.split(",")
    return [int(number) for number in numbers]

def read_input():
    """
    Reads and interprets the input file
    """
    content = load_file_complete()
    # distinct blocks are sperated by blank lines
    blocks = content.split("\n\n")
    # split blocks into lines, store in seperate variables
    policy_block, myticket_block, tickets_block = [block.split("\n") for block in blocks]
    # read policy block
    policies = [read_policy(line) for line in policy_block]
    # read my ticket, ignoring the title line
    myticket = read_ticket(myticket_block[1])
    # read other tickets, ignoring title line
    tickets = [read_ticket(line) for line in tickets_block[1:]]

    return policies, myticket, tickets

def ticket_scanning_error():
    """
    Determine the sum of all values on tickets not valid for any field
    """
    policies, myticket, tickets = read_input()
    # we do not care about our ticket specifically
    tickets += [myticket]
    # get list of all numbers
    numbers = [number for ticket in tickets for number in ticket]
    # compute allowed ranges
    ranges = policy_sum(policies)

    sum = 0
    for number in numbers:
        if not x_in_any_range(number, ranges):
            sum += number

    return sum

def ranges(policies):
    """
    Extract all ranges from list of policies
    Returns an iterable of each range
    """
    for policy in policies:
        n, la, ha, lb, hb = policy
        yield la, ha
        yield lb, hb

def policy_sum(policies):
    """
    Reduce policies to a single set of bounds, the union of all allowed values
    """
    # initialise with empty list
    sum = []
    # for all ranges
    for range in ranges(policies):
        # first value copies
        if not sum:
            sum = [range]
        else:
            # create new sum to avoid mutating a list during iteration
            newsum = []
            # otherwise go through all current ranges
            for range2 in sum:
                # ranges overlap if either contains and endpoint of the other
                if x_in_range(range[0], range2) or x_in_range(range[1], range2):
                    # consider union of ranges instead
                    # range is local to the loop, it is not trying to change the output of the iterator
                    range = (min(range[0], range2[0]), max(range[1], range2[1]))
                else:
                    # current range remains preserved
                    newsum.append(range2)
            # add new range
            newsum.append(range)
            # update sum
            sum = newsum.copy()
    return sum

def x_in_range(x, range):
    """
    Determine if x is in the given range, endpoints inclusive
    """
    #   for numpy broadcasting
    return np.logical_and(range[0] <= x, x <= range[1])

def x_in_any_range(x, ranges):
    """
    Determine if x is in any range in given list
    """
    valid = False
    for range in ranges:
        # valid if in any bounds
        valid |= x_in_range(x, range)
    return valid