import itertools
from math import ceil


def read_file(file_path) -> list[list[str]]:
    with open(file_path, 'r') as file:
        line = file.readline()
    return [rang.split("-") for rang in line.split(",")]


def invalid_in_range(rang: list[str]) -> list[str]:
    start, end = rang
    half_length = ceil(len(start) / 2) # 4
    start_half = start[:half_length]

    poissible_numbers = generate_ids_of_length(half_length, int(start_half))
    invalid = [i for i in poissible_numbers if int(start) <= i <= int(end)]
    return invalid


def generate_ids_of_length(half_length, start_number: int):
    numbers = []
    for i in range(start_number, int("9"*half_length)):
        actual_number = i + i*(10**half_length)
        numbers.append(actual_number)
    return numbers



def main():
    data = read_file("../input.txt")
    all_invalid = list(itertools.chain.from_iterable(invalid_in_range(a) for a in data))
    result = sum(all_invalid)
    print(result)


if __name__ == "__main__":
    main()
