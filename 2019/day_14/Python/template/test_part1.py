from part1 import parse_input, calculate_total_ore


def make_reactions():
    reactions = {
        'A': {'quantity': 10, 'recipe': {'ORE': 10}},
        'B': {'quantity': 1, 'recipe': {'ORE': 1}},
        'C': {'quantity': 1, 'recipe': {'A': 7, 'B': 1}},
        'D': {'quantity': 1, 'recipe': {'A': 7, 'C': 1}},
        'E': {'quantity': 1, 'recipe': {'A': 7, 'D': 1}},
        'FUEL': {'quantity': 1, 'recipe': {'A': 7, 'E': 1}}
    }
    return reactions


def test_parse_input():
    reactions = [
        '10 ORE => 10 A',
        '1 ORE => 1 B',
        '7 A, 1 B => 1 C',
        '7 A, 1 C => 1 D',
        '7 A, 1 D => 1 E',
        '7 A, 1 E => 1 FUEL',
    ]
    output = parse_input(reactions)
    expected = make_reactions()
    assert output == expected


def test_calculate_total_ore():
    reactions = make_reactions()
    output = calculate_total_ore(reactions)
    expected = 31
    assert output == expected