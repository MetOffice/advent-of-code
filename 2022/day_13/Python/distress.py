import numpy as np
from functools import cmp_to_key

def read_input(path="../input.txt"):
    """
    Reads the input file and spits out a list of tuples of the packets
    """
    pairs = []
    with open(path) as file:
        pair = []
        for line in file:
            line = line.strip()
            if line:
                pair.append(listify(line))
            else:
                pairs.append(pair)
                pair = []
        if pair:
            pairs.append(pair)
    return pairs


def listify(string):
    """
    Turn the string into a list a la eval
    """
    # WOOOOOOO
    return eval(string)


def compare(packet_1, packet_2):
    """
    Packet_1 and packet_2 are the two packets we're copring, they can be lists or integers.
    Returns negative if packet_1 < packet_2, 0 if packet_1 = packet_2, positive if packet_1 > packet_2
    """
    # If both are integers simply compare them
    if isinstance(packet_1, int) and isinstance(packet_2, int):
        return np.sign(packet_1 - packet_2)

    # If only one is an integer, wrap it in a one-element list
    if isinstance(packet_1, int):
        packet_1 = [packet_1]
    if isinstance(packet_2, int):
        packet_2 = [packet_2]

    # If both are lists, or are now both lists, compare each of their elements in turn
    for left, right in zip(packet_1, packet_2):
        out = compare(left, right)
        if out:
            return out

    # If we run out of elements, compare the lengths of the lists
    return np.sign(len(packet_1) - len(packet_2))


def part_1(pairs):
    """
    For each pair of inputs, compare them, add together the indices of those
    that are in the correct (<) order.
    Equal elements are assumed to be in the correct order but a warning is shown.
    """
    total = 0
    for i, (left, right) in enumerate(pairs):
        comparison = compare(left, right)
        # if less than or equal
        if comparison <= 0:
            total += i + 1
        if comparison == 0:
            print(f"Warning! Pair at {i} is equal.")
    return total

def part_2(pairs):
    """
    Given the list of pairs of inputs, sort the whole list and the two divier packets.
    Find the indices of the divider packets in the final list and return their product.
    """
    # include dividers
    packets = [[[2]], [[6]]]

    # flatten list of packets
    for pair in pairs:
        packets += pair

    # argsort. The indcies to which each item is sorted
    packets = sorted(packets, key=cmp_to_key(compare))

    index1 = packets.index([[2]])
    index2 = packets.index([[6]])

    return (index1 + 1) * (index2 + 1)

if __name__ == "__main__":
    pairs = read_input()

    total = part_1(pairs)
    print(f"The total is {total}.")

    decoder = part_2(pairs)
    print(f"The decoder key is {decoder}.")