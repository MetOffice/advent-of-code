import os
import collections
import itertools
import __main__

def read_the_string():
    filepath = os.path.join(os.path.dirname(__main__.__file__), "../input.txt")
    with open(filepath) as file_handle:
        raw = file_handle.readlines()

    return raw



def sliding_window(iterable, n):
    # from https://docs.python.org/3/library/itertools.html#itertools-recipes
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def find_packet(signal, packet_length=4):
    # a packet is an un-repeating substring
    for i, part in enumerate(sliding_window(signal[0], packet_length)):
        if len(set(part)) == packet_length:
            return i+packet_length


if __name__ == "__main__":
    thing = read_the_string()
    packet_position = find_packet(thing)
    message_position = find_packet(thing, packet_length=14)
    print(f"packet position = {packet_position}")
    print(f"message position = {message_position}")
