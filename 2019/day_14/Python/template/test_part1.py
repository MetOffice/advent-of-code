part1 import parse_input, calculate_total_ore


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


def test_calculate_total_ore_2():
    reactions = ['2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG',
                '17 NVRVD, 3 JNWZP => 8 VPVL',
                '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL',
                '22 VJHF, 37 MNCFX => 5 FWMGM',
                '139 ORE => 4 NVRVD',
                '144 ORE => 7 JNWZP',
                '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC',
                '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV',
                '145 ORE => 6 MNCFX',
                '1 NVRVD => 8 CXFTF',
                '1 VJHF, 6 MNCFX => 4 RFSQX',
                '176 ORE => 6 VJHF']
    output = calculate_total_ore(parse_input(reactions))
    expected = 180697
    assert output == expected

def test_calculate_total_ore_3():
    reactions = ['157 ORE => 5 NZVS',
            '165 ORE => 6 DCFZ',
            '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
            '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
            '179 ORE => 7 PSHF',
            '177 ORE => 5 HKGWZ',
            '7 DCFZ, 7 PSHF => 2 XJWVT',
            '165 ORE => 2 GPVTF',
            '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']
    output = calculate_total_ore(parse_input(reactions))
    expected = 13312
    assert output == expected