from input_data import get_input
from part1 import intcode

if __name__ == "__main__":
    for noun in range(99):
        for verb in range(99):
            input_data = get_input()
            input_data[1] = noun
            input_data[2] = verb
            try:
                output_data = intcode(input_data)
            except:
                print(f"Error for noun: {noun}, verb: {verb}")
            if output_data[0] == 19690720:
                print(f"Noun: {noun}, Verb: {verb}, answer: {100*noun + verb}")
