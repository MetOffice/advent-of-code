from loaders import load_string


def calculate_card_points(input_string):
    winning_numbers, chosen_numbers = input_string.split(": ")[1].split(" | ")
    winning_numbers = {int(x) for x in winning_numbers.split()}
    chosen_numbers = {int(x) for x in chosen_numbers.split()}
    intersection = winning_numbers.intersection(chosen_numbers)
    return int(2 ** (len(intersection) - 1))


def calculate_total_points(cards):
    return sum([calculate_card_points(card) for card in cards])


if __name__ == "__main__":
    scratchcards = load_string()
    print(calculate_total_points(scratchcards))

