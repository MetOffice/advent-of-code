import pytest

from camel_cards import Category, Hand
import camel_cards

@pytest.mark.parametrize(
    "input_string, expected_category",
    [
        ("AAAAA", Category.FIVE_OF_A_KIND),
        ("AA8AA", Category.FOUR_OF_A_KIND),
        ("23332", Category.FULL_HOUSE),
        ("TTT98", Category.THREE_OF_A_KIND),
        ("23432", Category.TWO_PAIRS),
        ("A23A4", Category.ONE_PAIR),
        ("23456", Category.HIGH_CARD),
    ],
)
def test_category(input_string, expected_category):
    hand = Hand(input_string, 0)
    assert hand.category == expected_category


test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def test_input_test():
    result = camel_cards.calulate_for_string(test_input.split('\n'))
    assert result == 6440

