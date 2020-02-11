from part1 import calculate_fuel

def test_case_1():
    mass = 12
    expected = 2
    output = calculate_fuel(mass)

    assert output == expected
