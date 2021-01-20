from pathlib import Path


def get_input():
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_list = file.readlines()

    lines = []
    for line in input_list:
        result = []
        for character in line.strip():
            result.append(character)
        lines.append(result)

    return lines
