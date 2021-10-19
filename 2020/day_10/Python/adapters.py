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
    Finds the number of 1, 2 or 3 jolt differences in the chain

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
    return diffs.count(1), diffs.count(2), diffs.count(3)


def count_combinations(sorted_chain):
    """
    Takes a sorted chain, in the longest possible formation. Counts the number of other valid combinations.

    Parameters
    ----------
    sorted_chain a list of ints

    Returns
    -------
    int
    """
    if find_jolt_distribution(sorted_chain)[0:1] == (0, 0):
        # stop now
        pass


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
    dist = find_jolt_distribution(chain)

    blocks = []
    new_block = []
    for i, item in enumerate(dist):
        new_block.append(chain[i])

        if item == 3:
            blocks.append(new_block)
            new_block = []
            # we have hit the end of a block

    num_combinations = 1  # the initial combo
    # [4, 5, 6, 7, 9, 10, 11]
    # [1, 1, 1, 1, 2, 1, 1]

    # [4, 6, 7, 9, 10, 11]
    # [4, 5, 7, 9, 10, 11]
    # [4, 7, 9, 10, 11]
    # [4, 7, 9, 10, 11]
    # [4, 6, 9, 10]
    # [4, 5, 6, 7, 9, 10]
    # [4, 7, 10]

    for small_block in blocks:
        # if len(small_block) > 4:
        #     small_block_dist = find_jolt_distribution(small_block)
        #     for group in sliding_window(small_block_dist, 4):
        #         # [1, 1, 1, 1] = 4
        #         # [1, 1, 1, 2] = 3
        #         # [1, 1, 2, 1] = 3
        #         # [1, 2, 1, 1] = 3
        #         # [2, 1, 1, 1] = 3
        #         # [1, 1, 2, 2] =
        #         # [1, 2, 1, 2] =
        #         # [1, 2, 2, 1] =
        #         # [2, 1, 2, 1] =
        #         # [2, 2, 2, 1] =
        #         # [
        #         if sum(group) == 4:
        #             num_combinations *= 4
        #         elif sum(group) == 5:
        #             num_combinations *= 3
        #
        # elif len(small_block) == 4:
        #     # [1, 1, 1] = 3
        #     # [1, 1, 2] = 2
        #     # [1, 2, 1] = 2
        #     # [2, 1, 1] = 2
        #     # [2, 2, 1] = 2
        #     # [1, 2, 2] = 2
        #     # [2, 2, 2]
        #     small_block_dist = find_jolt_distribution(small_block)
        #     if sum(small_block_dist) == 3:
        #         num_combinations *= 4
        #     elif sum(small_block_dist) == 4:
        #         num_combinations *= 3

        if len(small_block) >= 3:
            small_block_dist = find_jolt_distribution(small_block)
            # e.g. [10, 11, 12], [10, 12, 13], [10, 11, 13]
            # [1, 1] = 2
            # [1, 2] = 2
            # [2, 1] = 2
            # [2, 2] = 1

            for group in sliding_window(small_block_dist, 2):

                if sum(group) == 4:
                    num_combinations *= 1
                else:
                    num_combinations *= 2

    return num_combinations



if __name__ == "__main__":
    result = main_part2()
    print(result)
