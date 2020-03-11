from typing import List

from input_data import get_input

def parse(input_data: List, pointer: int) -> List:
    opcode = input_data[pointer]
    value_a = input_data[input_data[pointer + 1]]
    value_b = input_data[input_data[pointer + 2]]
    result_pos = input_data[pointer + 3]
    result = 0
    if opcode == 1:
        # add
        result = value_a + value_b
    elif opcode == 2:
        # multiply
        result = value_a * value_b
    else:
        raise Exception("Unrecognised opcode")
    input_data[result_pos] = result
    return input_data

def intcode(input_data: List) -> List:
    pointer = 0
    while input_data[pointer] != 99:
        input_data = parse(input_data, pointer)
        pointer += 4

    return input_data

if __name__ == "__main__":
    input_data = get_input()
    input_data[1] = 12
    input_data[2] = 2
    output_data = intcode(input_data)
    print(output_data[0])