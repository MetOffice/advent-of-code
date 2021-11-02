from common import loaders
import collections
import itertools


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


def find_chain(adapters):
    """
    Sorts the adapters into a chain that works

    Parameters
    ----------
    adapters - list of strings

    Returns
    -------
    chain - a list of ints

    """
    adapters = [int(i) for i in adapters]
    sorted_adapters = sorted(adapters)
    sorted_adapters.insert(0, 0)
    sorted_adapters.append(sorted_adapters[-1] + 3)
    return sorted_adapters


def find_jolt_distribution(chain):
    """
    Return the differences between the numbers in the chain.

    Parameters
    ----------
    chain - a list of ints

    Returns
    -------
    tuple
    """
    diffs = []
    for i in range(0, len(chain) - 1):
        diffs.append(chain[i + 1] - chain[i])

    return diffs


def count_jolt_distribution(diffs):
    """
    Finds the number of 1, 2 or 3 jolt differences in the chain.
    """
    return diffs.count(1), diffs.count(2), diffs.count(3)


def count_combinations(sorted_chain):
    """
    Takes a sorted chain, in the longest possible formation.
    Counts the number of other valid combinations.

    Parameters
    ----------
    sorted_chain a list of ints

    Returns
    -------
    int

    """
    # f(0) and f(1), which are both 1.
    # The 'answers' list will only ever have 3 elements thanks to the
    # "double-ended queue", see
    # https://docs.python.org/3/library/collections.html#collections.deque.
    answers = collections.deque([1, 1], maxlen=3)

    # f(2).
    answers.append(1 + is_valid_jolt(sorted_chain[0], sorted_chain[2]))

    # f(k); get answers for remaining items in list.
    for index, number in enumerate(sorted_chain[3:], start=3):
        first_term = answers[-1]
        second_term = (
            is_valid_jolt(sorted_chain[index - 2], sorted_chain[index])
            * answers[-2]
        )
        third_term = (
            is_valid_jolt(sorted_chain[index - 3], sorted_chain[index])
            * answers[-3]
        )
        answers.append(first_term + second_term + third_term)
    return answers[-1]


def is_valid_jolt(input1, input2):
    return input2 - input1 <= 3


def main_part1(input=None):
    if input is None:
        input = loaders.load_string()
    # read input
    chain = find_chain(input)
    dist = find_jolt_distribution(chain)
    count = count_jolt_distribution(dist)
    result = count[0] * count[2]

    return result


def main_part2(input=None):
    if input is None:
        input = loaders.load_string()
    chain = find_chain(input)
    return count_combinations(chain)


if __name__ == "__main__":
    print(f"Part 1: {main_part1()}")
    print(f"Part 2: {main_part2()}")
