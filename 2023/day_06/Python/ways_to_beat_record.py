# Wait for x seconds
# Travel at x mm / second from x ms until race end (n ms)

# distance = x * time of movement
# distance = x * (n - x)

# our distance > record distance
# x * (n - x) > r (the record)

# The solutions of x * (n - x) - r = 0 will be the start and end of our winning charge up times

# -x^2 + nx - r = 0
# x^2 - nx + r = 0
#
# a = 1, b = -n, c = r

# x = (n ± √(n^2 - 4r)) / 2

# |x - n/2| = √(n^2 - 4r) / 2
# (x - n/2)^2 = (n^2 - 4r) / 4
# the difference from half time (squared) = (n/2)^2 - r

import math

def get_num_of_record_beating_charge_up_times(race_length: int, record: int):
    difference_from_half_time = math.sqrt((race_length / 2) ** 2 - record)

    start = math.floor(race_length / 2 - difference_from_half_time) + 1
    end = math.ceil(race_length / 2 + difference_from_half_time) - 1

    return end - start + 1


if __name__ == "__main__":
    with open("../input.txt") as f:
        times, distances = map(lambda l: tuple(map(int, l.split()[1:])), f)

    print(math.prod(
        get_num_of_record_beating_charge_up_times(time, distance)
        for time, distance in zip(times, distances)
    ))

    with open("../input.txt") as f:
        time, distance = map(lambda l: int("".join(l.split()[1:])), f)

    print(get_num_of_record_beating_charge_up_times(time, distance))
