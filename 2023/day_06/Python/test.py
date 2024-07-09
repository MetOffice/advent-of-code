from ways_to_beat_record import get_num_of_record_beating_charge_up_times

import math

test_input = (
    "Time:      7  15   30\n"
    "Distance:  9  40  200\n"
)

def test_part1():
    times, distances = map(lambda l: tuple(map(int, l.split()[1:])), test_input.splitlines())

    assert 288 == math.prod(
        get_num_of_record_beating_charge_up_times(time, distance)
        for time, distance in zip(times, distances)
    )

def test_part2():
    time, distance = map(lambda l: int("".join(l.split()[1:])), test_input.splitlines())

    assert 71503 == get_num_of_record_beating_charge_up_times(time, distance)
