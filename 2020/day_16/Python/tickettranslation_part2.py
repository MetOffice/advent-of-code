from tickettranslation import *
# large, rectangular array handling
import numpy as np

def departure_product():
    """
    Determines the field names on tickets and returns the product of fields beinning with "departure"
    """
    # read input file
    policies, myticket, tickets = read_input()
    # remove invalid tickets
    tickets = valid_tickets(policies, tickets)
    # my ticket is known to be valid
    tickets += [myticket]
    # numpy array for fast pivot
    tickets = np.array(tickets)

    # store possible fields for each column
    possible_fields = [[] for i in range(len(policies))]

    for policy in policies:
        # record policy name in each field where it fits
        possible_fields = find_possible_fields(tickets, policy, possible_fields)

    # choose a combination of fields that matches all tickets
    # except unless there is exactly 1 combination
    fields = pick_fields(possible_fields)
    # return the product of fields beginning with departure
    return compute_departure_product(fields, myticket)

def valid_tickets(policies, tickets):
    """
    Remove all tickets that are definitely invalid, returning all valid tickets
    """
    # create return list
    valid = []
    # compute allowed ranges
    ranges = policy_sum(policies)

    for ticket in tickets:
        # If all numbers fit into an allowable range
        if all([x_in_any_range(x, ranges) for x in ticket]):
            # add the ticket
            valid += [ticket]
    return valid

def find_possible_fields(tickets:np.array, policy, possible_fields):
    """
    Record policy name into each index of possible_fields where it can fit
    """
    # get ranges from policy
    policy_ranges = list(ranges([policy]))
    # broadcast over numpy array
    valid = x_in_any_range(tickets, policy_ranges)
    # aggregate to find columns where all tickets are valid
    valid = np.all(valid, axis=0)
    # write policy name into possible_fields
    for i in range(len(valid)):
        if valid[i]:
            possible_fields[i].append(policy[0])
    return possible_fields

def pick_fields(possible_fields):
    """
    Given a list of lists of possible fields for each column of the ticket, choose a permutation of field names
    such that each field name appears in its corresponding list.

    Hall's Marriage Problem. For bipartite graph where one group is field, the other column, find total matching and demonstrate it is unique.

    This is non-trivial in the general case. The naive solution below seems to work for AoC test input.
    """
    # initialise a list to place our choices
    choice = [None] * len(possible_fields)
    # repeat until all fields are filled
    for _ in choice:
        # look for length 1 sublists
        for i in range(len(choice)):
            if len(possible_fields[i]) == 1:
                # choose this field for this column
                field = possible_fields[i][0]
                choice[i] = field
                # remove this element from all lists
                for fields_list in possible_fields:
                    if field in fields_list:
                        fields_list.remove(field)
    return choice

def compute_departure_product(fields, ticket):
    """
    Finds all numbers on ticket where field name begins with 'departure' and returns their product
    """
    # find all departure fields. No field has departure anywhere else in its name.
    departures = ["departure" in field for field in fields]
    # numpyfy for indexing
    departures = np.array(departures)
    ticket = np.array(ticket)
    # get all ticket values where departures is true
    values = ticket[departures]
    # product
    return np.product(values)

print(departure_product())