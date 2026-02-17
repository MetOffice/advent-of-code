from tqdm import tqdm
import itertools


def load_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def lyes_way(bank:str) -> int:
    """Does the thing. But dear lord who knows how
    For part 1 only
    """
    return max([int(a+b) for (a,b) in itertools.combinations(bank,2)])


def find_first_largest_index(bank: str, required_battery_length: int) -> int:
    """This finds the first occurence of the largest number in a string of numbers.
    But only if that number is <required_battery_length> characters before the end.

    Args:
        bank (str): The bank of batteries
        required_battery_length (int): The size of the battery required

    Returns:
        int: The index of the first occurance of the largest number
    """
    batteries = [int(battery) for battery in bank]
    # Don't find the largest one if it's last
    largest_battery = str(max(batteries[:-required_battery_length]))
    return bank.find(largest_battery)


def find_largest_battery_in_bank(bank: str, required_battery_length: int) -> int:
    """For a bank of batteries (string of digits) this function finds the largest
    possible number, of the required length, linearly through the bank.

    Args:
        bank (str): The bank of batteries
        required_battery_length (int): The length required of the battery

    Returns:
        int: The largest battery
    """
    new_bank = bank
    indices = []
    while len(indices) < required_battery_length:
        indices.append(find_first_largest_index(new_bank, required_battery_length-len(indices)))
        new_bank = new_bank[indices[-1]:]

    largest_battery = ""
    for index in indices:
        largest_battery += bank[index]

    return int(largest_battery)


if __name__ == "__main__":
    banks = load_input("../input.txt")
    found = []
    for bank in tqdm(banks, total=len(banks)):
        found.append(lyes_way(bank))

    result1 = sum(found)
    print(f"Part 1: {result1}")

    # Part 2
    required_battery_length = 12
    individual_batteries = []
    for bank in banks:
        individual_batteries.append(find_largest_battery_in_bank(bank, required_battery_length))

    result2 = sum(individual_batteries)
    print(f"Part 2: {result2}") # ! This is currently too low. Needs to be bigger than 164033353432636