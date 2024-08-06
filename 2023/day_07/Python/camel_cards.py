import collections
from dataclasses import dataclass
from enum import Enum
from functools import cache
from typing import List, Self

card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


class Category(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0



@dataclass(frozen=True)
class Hand:
    cards: str
    bid: int

    # Part 2 V change the categoriser
    @property
    @cache
    def category(self) -> Category:
        cards_without_jokers = self.cards.replace("J", "")
        return self._category(cards_without_jokers)

    @staticmethod
    def _category(cards: str) -> Category:
        card_counts = collections.Counter(cards)
        unique_card_count = len(card_counts)
        if unique_card_count == 1 or len(cards) == 0:
            return Category.FIVE_OF_A_KIND
        elif unique_card_count == 2:
            if 1 in card_counts.values():
                return Category.FOUR_OF_A_KIND
            else:
                return Category.FULL_HOUSE
        elif unique_card_count == 3:
            if 3 in card_counts.values() or len(cards) < 5:
                return Category.THREE_OF_A_KIND
            else:
                return Category.TWO_PAIRS
        elif unique_card_count == 4:
            return Category.ONE_PAIR

        return Category.HIGH_CARD

    def __lt__(self, other):
        if self.category != other.category:
            return self.category.value < other.category.value
        else:
            for (chr1, chr2) in zip(self.cards, other.cards):
                if chr1 != chr2:
                    return card_values[chr1] < card_values[chr2]
                else:
                    continue

    @classmethod
    def from_string(cls, line: str) -> Self:
        (cards, bid) = line.split()
        return cls(cards, int(bid))


def calulate_for_string(inp: list[str]) -> int:
    hands: list[Hand] = [Hand.from_string(l) for l in inp]
    sorted_hands = sorted(hands)
    print(sorted_hands)
    return sum([hand.bid * (i + 1) for i, hand in enumerate(sorted_hands)])


if __name__ == "__main__":
    with open("../input.txt") as f:
        print(calulate_for_string(f.readlines()))
