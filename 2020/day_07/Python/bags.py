import numpy as np

def main():
    pass


def count_bag_colours(my_bag, bag_rules):
    """
    Return how many outermost bag colors can eventually contain at least one
    my_bag.


    Parameters
    ----------
    my_bag : str
        Bag colour we want to carry.
    bag_rules : str
        Single string of all bag rules.

    Returns
    -------
    : int
        Count of how many outermost bag colors can eventually contain at least
        one my_bag.

    """
    # TODO: Refactor into separate function
    # Break up bag rules by parent bag colour into nested dictionary structure.
    bag_rules = bag_rules.split('\n')
    organised_rules = dict()
    for bag_rule in bag_rules:
        parsed_rule = parse_bag_rule(bag_rule)
        bag_colour, bag_contents = organise_bag_rule(parsed_rule)
        if bag_colour in organised_rules:
            raise ValueError(f"{bag_colour} already in organised rules.")
        organised_rules[bag_colour] = bag_contents

    count = 0
    # TODO: Recurse nested dictionary structure looking for my_bag

    return count


def parse_bag_rule(bag_rule):
    """

    Parameters
    ----------
    bag_rule

    Returns
    -------

    Examples
    --------
    >>> parse_bag_rule("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    ['light red', '1 bright white', '2 muted yellow']

    >>> a = "light red bags contain 1 bright white bag, 2 muted yellow bags." #notatest
    >>> parse_bag_rule(a)
    ['light red', '1 bright white', '2 muted yellow']

    # >>> for s in [1,2,3]:
    # ...     for t in [4,5,6]:
    # ...         print(s*t)

    # >>> a = np.ones([9, 5, 7, 4])
    # >>> c = np.ones([9, 5, 4, 3])
    # >>> np.dot(a, c).shape
    # (9, 5, 7, 9, 5, 3)
    # >>> np.matmul(a, c).shape
    # (9, 5, 7, 3)
    #
    # # n is 7, k is 4, m is 3
    """


    results = []
    contains_str = "bags contain"
    cleaned = [item.strip() for item in bag_rule.split(contains_str)]

    # We've finished with the 1st element - remove it!
    results.append(cleaned.pop(0))

    multi_str = ", "
    contained = cleaned[0].split(multi_str)
    contained = [
        item.replace("bags", "").replace("bag", "").replace(".", "").strip()
        for item in contained
    ]

    results.extend(contained)

    return results


def organise_bag_rule(parsed_rule):
    """
    Reformats list describing rule into tuple.

    e.g. converts
        ["light red", "1 bright white", "2 muted yellow"]
    into:
        ("light red", {"bright white": 1, "muted yellow": 2})

    Parameters
    ----------
    parsed_rule : list of str
        Parent bag colour followed by zero or more child bag count and colours.

    Returns
    -------
    : tuple
        First element of tuple is parent bag colour.  Second element is a
        dictionary, where dictionary has keys of child bag colours
        and values of child bag counts.

    Examples
    --------
    >>> organise_bag_rule(["light red", "1 bright white", "2 muted yellow"])
    ('light red', {'bright white': 1, 'muted yellow': 2})

    """
    key = parsed_rule.pop(0)
    inner_dict = dict()
    for item in parsed_rule:
        number, bag_colour = item.split(maxsplit=1)
        try:
            inner_dict[bag_colour] = int(number)
        except ValueError:
            """Handling the no other case: 'no' isn't an integer."""
            pass
    return (key, inner_dict)
