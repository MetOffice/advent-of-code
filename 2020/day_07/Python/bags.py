def count_bag_colours(my_bag, bag_rules):
    """"""
    pass


def parse_bag_rules(bag_rule):
    """"""
    # "light red bags contain 1 bright white bag, 2 muted yellow bags."
    # ["light red", "1 bright white", "2 muted yellow"],
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
