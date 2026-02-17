from tqdm import tqdm
from math import ceil, floor


def read_file(file_path) -> list[list[str]]:
    with open(file_path, 'r') as file:
        line = file.readline()
    return [rang.split("-") for rang in line.split(",")]


def string_mirror_check(number: int) -> bool:
    string_number = str(number)
    Nchar = len(string_number)
    if Nchar % 2:
        # It's odd
        return False
    first, second = string_number[:Nchar//2], string_number[Nchar//2:]
    if first == second:
        return True


def string_chunk_check(number: int) -> bool:
    string_number = str(number)
    SN_length = len(string_number)
    longest = floor(len(string_number)//2)
    for length in range(1, longest+1):
        if not SN_length % length:
            if string_number[:length] * (SN_length//length) == string_number:
                return True
    else:
        return False


def main():
    data = read_file("../input.txt")
    invalid_ids = []
    invalid_ids2 = []
    for thing in tqdm(data, total=len(data)):
        for thing2 in range(int(thing[0]), int(thing[1])+1):
            if string_mirror_check(thing2):
                invalid_ids.append(thing2)
            if string_chunk_check(thing2):
                invalid_ids2.append(thing2)
    result = sum(invalid_ids)
    print("Part 1 answer:", result)
    result2 = sum(invalid_ids2)
    print("Part 2 answer:", result2)


if __name__ == "__main__":
    main()
