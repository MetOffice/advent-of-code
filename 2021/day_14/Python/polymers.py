from common import loaders
from itertools import tee
from collections import Counter

# TODO:

# come up with a way of applying the rules
# apply the rules lots of times
# count the letters


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def parse_input(input_data):
    """

    Parameters
    ----------
    input_data

    Returns
    -------

    """

    polymer_template = input_data.pop(0)
    _ = input_data.pop(0)  # remove the blank line
    insertion_rules = {item.split(" -> ")[0]: item.split(" -> ")[1] for item in input_data}

    return polymer_template, insertion_rules


def apply_rules(polymer, insertion_rules):
    """

    Parameters
    ----------
    polymer
    insertion_rules

    Returns
    -------

    """
    pairs = pairwise(polymer)
    result = []
    for pair in pairs:
        result.append(pair[0])
        k = "".join(pair)
        if k in insertion_rules.keys():
            result.append(insertion_rules[k])

    result.append(polymer[-1])

    new_polymer = "".join(result)
    return new_polymer


def multiple_apply_rules(start, rules, number):
    result = start
    for i in range(0, number):
        result = apply_rules(result, rules)

    return result


def count_letters(polymer):

    c = Counter(polymer)

    ordered = c.most_common()
    most = ordered[0]
    least = ordered[-1]

    return most, least


if __name__ == "__main__":
    input_file = loaders.load_string()
    start, rules = parse_input(input_file)
    result_part1 = multiple_apply_rules(start, rules, 10)
    most, least = count_letters(result_part1)

    print(f"Answer part 1: {most[1] - least[1]}")

    result_part2 = multiple_apply_rules(start, rules, 40)
    most, least = count_letters(result_part2)

    print(f"Answer part 2: {most[1] - least[1]}")
