from typing import LiteralString


def load_input(filename: str) -> str:
    """
    Load the puzzle input from a file.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines][0]


def rearrange_inplace_part1(inp: list[str]) -> None:
    first_free_space = next_free_space(inp, 0)
    last_char = next_char_backwards(inp, len(inp) - 1)

    while first_free_space <= last_char:
        inp[first_free_space] = inp[last_char]
        inp[last_char] = '.'
        first_free_space = next_free_space(inp, first_free_space)
        last_char = next_char_backwards(inp, last_char)


def scan_for_space(inp, size_of_file, max):
    next_free = next_free_space(inp, 0)

    while (size_of_space := get_size_of_space(inp, next_free)) < size_of_file:
        next_free = next_free_space(inp, next_free + size_of_space)
        if next_free > max:
            raise IndexError
    return next_free


def rearrange_inplace_part2(inp: list[str]) -> None:
    last_visited = 0
    last_char = next_char_backwards(inp, len(inp) - 1)

    processed_ids = set()

    while True:

        print(inp[last_char])
        size_of_file = get_size_of_file(inp, last_char)
        if inp[last_char] in processed_ids:
            print(f"Already seen {inp[last_char]}")
            last_char = next_char_backwards(inp, last_char - size_of_file)
            continue
        if last_char - size_of_file == 0:
            print("end")
            break
        processed_ids.add(inp[last_char])
        try:
            index_of_space = scan_for_space(inp, size_of_file, last_char)
        except IndexError:
            print(f"Could not find space for file {inp[last_char]} with size {size_of_file}")
        else:
            place_in_position(inp, inp[last_char], index_of_space, size_of_file)
            place_in_position(inp, '.', last_char - size_of_file + 1, size_of_file)
            last_visited = index_of_space
        last_char = next_char_backwards(inp, last_char - size_of_file)


def place_in_position(inp: list[int | str], chr: int | str, start: int, length: int):
    for i in range(start, start + length):
        inp[i] = chr


def next_free_space(inp: list[str], current_index) -> int:
    while inp[current_index] != ".":
        current_index += 1
    return current_index


def get_size_of_space(inp: list[str | int], start_index):
    index = start_index
    while inp[index] == ".":
        index += 1
        if index >= len(inp):
            raise IndexError
    return index - start_index


def get_size_of_file(inp: list[str | int], start_index):
    index = start_index
    chr = inp[start_index]
    while inp[index] == chr and index > 0:
        index -= 1
    return start_index - index


def next_char_backwards(inp: list[str], current_index) -> int:
    while inp[current_index] == ".":
        current_index -= 1
    return current_index


def expand_input(inp: list[str]) -> list[str]:
    end_size = sum(int(x) for x in inp)
    result = ['.'] * end_size

    current_type = 'FILE'
    current_index = 0
    for input_index, x in enumerate(inp):
        if current_type == 'FILE':
            for i in range(current_index, current_index + int(x)):
                result[i] = input_index // 2
                current_index += 1
        elif current_type == 'SPACE':
            current_index += int(x)
        if current_type == 'FILE':
            current_type = 'SPACE'
        elif current_type == 'SPACE':
            current_type = 'FILE'

    return result


def checksum(inp: list[str]) -> int:
    return sum(i * j for i, j in enumerate(inp) if j != '.')


def main():
    input_line = load_input("input")
    files = input_line[::2]
    space = input_line[1::2]

    expanded = expand_input(input_line)
    rearrange_inplace_part2(expanded)
    result = checksum(expanded)
    print(result)


if __name__ == "__main__":
    main()
