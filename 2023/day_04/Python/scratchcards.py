from loaders import load_string


def number_of_matches(input_string: str):
    winning_numbers, chosen_numbers = input_string.split(": ")[1].split(" | ")
    winning_numbers = {int(x) for x in winning_numbers.split()}
    chosen_numbers = {int(x) for x in chosen_numbers.split()}
    return len(winning_numbers.intersection(chosen_numbers))


def calculate_card_points(input_string: str):
    return int(2 ** (number_of_matches(input_string) - 1))


def calculate_total_points(cards: list[str]):
    return sum([calculate_card_points(card) for card in cards])


def calculate_part2(cards: list[str]):
    copies_of_cards = [1] * len(cards)
    for i, card in enumerate(cards):
        matches = number_of_matches(card)
        for j in range(matches):
            if i+j+1 > len(cards):
                raise Exception("We have overrun the number of scratchcards!")
            copies_of_cards[i+j+1] += copies_of_cards[i]
    return sum(copies_of_cards)


if __name__ == "__main__":
    scratchcards = load_string()
    print("Part 1: ", calculate_total_points(scratchcards))
    print("Part 2: ", calculate_part2(scratchcards))
