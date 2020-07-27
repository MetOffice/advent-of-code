from pathlib import Path


def get_input():
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_list = file.readlines()

    input_list = [line.strip() for line in input_list]
    return input_list
