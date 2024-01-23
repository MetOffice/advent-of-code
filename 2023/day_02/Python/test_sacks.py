import pytest
import sacks


@pytest.mark.parametrize("input_string, is_possible",
                         [
                             ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
                             ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
                             ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False),
                             ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False),
                             ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
                         ]
                         )
def test_find_first_n_last_digit(input_string, is_possible):
    '''This is a duck string'''
    answer = sacks.single_game(input_string)
    assert answer == is_possible
