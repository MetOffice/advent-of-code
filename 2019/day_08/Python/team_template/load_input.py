from pathlib import Path

def get_input() -> str:
    input_file = Path(__file__).resolve().parent.parent.parent / "input.txt"
    with open(input_file, "r") as file:
        input_str = file.readline()

    return input_str
