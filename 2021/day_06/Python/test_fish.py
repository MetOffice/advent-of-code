from fish_part1 import simulate_fish, calculate_total_fish


def test_calculate_total_fish():
    initial_state = [3, 4, 3, 1, 2]
    number_of_days = 80
    expected = 5934
    actual = calculate_total_fish(initial_state, number_of_days)
    assert actual == expected


def test_simulate_fish():
    initial_state = [3, 4, 3, 1, 2]
    number_of_days = 5
    expected = [5, 6, 5, 3, 4, 5, 6, 7, 7, 8]
    actual = simulate_fish(initial_state, number_of_days)
    assert actual == expected
