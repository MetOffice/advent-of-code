from pathlib import Path


def get_input():
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_string = file.readline()

    input_list = [int(number) for number in input_string.strip()]
    return input_list
