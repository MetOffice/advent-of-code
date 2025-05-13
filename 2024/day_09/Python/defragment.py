from typing import LiteralString


def load_input(filename: str) -> str:
    """
    Load the puzzle input from a file.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines][0]


def rearrange_inplace(inp: list[str]) -> None:
    first_free_space = next_free_space(inp, 0)
    last_char = next_char_backwards(inp, len(inp) - 1)

    while first_free_space <= last_char:
        inp[first_free_space] = inp[last_char]
        inp[last_char] = '.'
        first_free_space = next_free_space(inp, first_free_space)
        last_char = next_char_backwards(inp, last_char)



def next_free_space(inp: list[str], current_index) -> int:
    while inp[current_index] != ".":
        current_index += 1
    return current_index


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
    return sum(i*j for i,j in enumerate(inp) if j != '.')

def main():
    input_line = load_input("input")

    expanded = expand_input(input_line)
    rearrange_inplace(expanded)
    result = checksum(expanded)
    print(result)


if __name__ == "__main__":
    main()
