import bags_rhiannon
import pytest

read_bag_rules = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                  "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                  "bright white bags contain 1 shiny gold bag.",
                  "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                  "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                  "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                  "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                  "faded blue bags contain no other bags.",
                  "dotted black bags contain no other bags."]


@pytest.mark.parametrize(("in_list", "expected_list"),
                         [([[0, 1, 2], [3, 4, 5]],
                          [0, 1, 2, 3, 4, 5]),
                          ([["a", "nested", "string", "list"]],
                           ["a", "nested", "string", "list"]),
                          (["a", "string", "list"],
                           ["a", "string", "list"]),
                         ([1, 2], [1, 2]),
                         ([], [])])
def test_flatten(in_list, expected_list):

    assert bags_rhiannon.flatten(in_list) == expected_list


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
    assert bags_rhiannon.parse_bag_rule(bag_rule) == expected


def test_parse_bag_rules():
    rules = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
             "bright white bags contain 1 shiny gold bag.",
             "dotted black bags contain no other bags."]

    expected = {"light red": [{"bright white": 1}, {"muted yellow": 2}],
                "bright white": [{"shiny gold": 1}],
                "dotted black": []}

    assert bags_rhiannon.parse_bag_rules(rules) == expected


def test_find_count_possible_outermost_bags():
    assert bags_rhiannon.find_count_possible_outermost_bags(read_bag_rules, "shiny gold") == 4


def test_get_max_num_of_bags_inside():
    assert bags_rhiannon.get_max_num_of_bags_inside(read_bag_rules, "shiny gold") == 35
