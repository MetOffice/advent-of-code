import fish_part1
import fish_part2


def test_calculate_total_fish_part1():
    initial_state = [3, 4, 3, 1, 2]
    number_of_days = 80
    expected = 5934
    actual = fish_part1.calculate_total_fish(initial_state, number_of_days)
    assert actual == expected


def test_simulate_fish_part1():
    initial_state = [3, 4, 3, 1, 2]
    number_of_days = 5
    expected = [5, 6, 5, 3, 4, 5, 6, 7, 7, 8]
    actual = fish_part1.simulate_fish(initial_state, number_of_days)
    assert actual == expected


def test_calculate_total_fish_part2():
    initial_state = [3, 4, 3, 1, 2]
    number_of_days = 256
    expected = 26984457539
    actual = fish_part2.calculate_total_fish(initial_state, number_of_days)
    assert actual == expected    
