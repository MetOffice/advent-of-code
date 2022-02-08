
def load_input():
    with open("./2021/day_01/input.txt", "r") as file:
        out = file.readlines()
    return out

def count_increases(depths:list):
    """
    Counts the number of items in the list that are larger than the previous item in the list
    """
    # sum of list comprehension of bools is the count of True values
    return sum([
        # previous item less than next item
        pair[0] < pair[1]
        for pair
        # zip of first n-1 elements to last n-1 creates list of pairs with indices (0,1),(1,2),...
        # while this looks wasteful, zip is creating an iterator that indexes into depths so its not actually duplicating the list
        in zip(depths[:-1], depths[1:])
    ])

def sum_3_sliding_window(depths):
    """
    Given a list, return the list of sums of each triple of consecutive elements
    """
    return [
        # sum each three consecutive elements
        sum(triple)
        for triple
        # triple index starting from 0, 1 and 2
        # as zip terminates when any of its iterables terminate the end indices are not necessary but are included for readability
        in zip(depths[:-2], depths[1:-1], depths[2:])
    ]

def part1():
    input = load_input()
    depths = [int(line) for line in input]
    return count_increases(depths)

def part2():
    input = load_input()
    depths = [int(line) for line in input]
    smooth_depths = sum_3_sliding_window(depths)
    return count_increases(smooth_depths)

print(part2())