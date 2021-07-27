import pytest
import bags

bag_rules = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


def test_count_bag_colours():
    """End to end test"""
    my_bag = "shiny gold"
    actual_bag_count = bags.count_bag_colours(my_bag, bag_rules)
    expected_bag_count = 4
    error_msg = "".join(
        [
            f"Unexpected number of bags ({actual_bag_count}) for {my_bag}",
            f"Expected {expected_bag_count}.",
        ]
    )

    assert actual_bag_count == expected_bag_count, error_msg


@pytest.mark.parametrize(
    ("bag_rule", "expected"),
    [
        (
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            ["light red", "1 bright white", "2 muted yellow"],
        ),
        (
            "bright white bags contain 1 shiny gold bag.",
            ["bright white", "1 shiny gold"],
        ),
        (
            "dotted black bags contain no other bags.",
            ["dotted black", "no other"],
        ),
    ],
)
def test_parse_bag_rule(bag_rule, expected):
    """"""
    actual_split = bags.parse_bag_rule(bag_rule)
    error_msg = f"Unexpected bag split {actual_split}\nExpected {expected}"

    assert actual_split == expected, error_msg


@pytest.mark.parametrize(
    ("bag_rule", "expected"),
    [
        (
            ["light red", "1 bright white", "2 muted yellow"],
            ("light red", {"bright white": 1, "muted yellow": 2}),
        ),
        (
            ["bright white", "1 shiny gold"],
            ("bright white", {"shiny gold": 1}),
        ),
        (
            ["dotted black", "no other"],
            ("dotted black", dict()),
        ),
    ],
)
def test_organise_bag_rule(bag_rule, expected):
    """"""
    actual = bags.organise_bag_rule(bag_rule)
    error_msg = f"Unexpected item in the bag rule area {actual}\nExpected {expected}"

    assert actual == expected, error_msg
