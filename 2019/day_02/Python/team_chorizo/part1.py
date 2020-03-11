from typing import List


def read_input(input_data) -> List:
    """
    Takes an intcode program text file and returns the integers inside it
    :param input_data: Path to file containing intcode
    :return: intcode as a list of integers
    """
    # read in the text file
    # output a list
    with open(input_data, 'r') as file_handle:
        integers = [int(item) for item in file_handle.readline().split(',')]

    return integers


def intcode(input_data: List) -> List:
    """
    incode parses a list of intcode integers and operates on it
    :param input_data: list of intocode integers
    :return: the intcode once all operations are done
    """

    # instruction_pointer = the address (index) of an opcode, i.e. the first element in a set of 4
    # opcode = the value of the intcode at address of the instruction_pointer
    # instruction = the three (or more?) values immediately after an opcode
    # pointers to parameters = the address (index) of each parameter
    # parameter = the values after an opcode

    for instruction_pointer in range(0, len(input_data), 4):

        opcode = input_data[instruction_pointer]

        if opcode == 99:
            break

        pointer_parameter_1 = instruction_pointer + 1
        pointer_parameter_2 = instruction_pointer + 2

        pointer_parameter_3 = instruction_pointer + 3
        value_3 = input_data[pointer_parameter_3]

        parameter_1 = input_data[pointer_parameter_1]
        value_1 = input_data[parameter_1]

        parameter_2 = input_data[pointer_parameter_2]
        value_2 = input_data[parameter_2]

        if opcode == 1:
            input_data[value_3] = value_1 + value_2

        elif opcode == 2:
            input_data[value_3] = value_1 * value_2

        else:
            raise RuntimeError("Received unknown opcode {}".format(opcode))

    return input_data


if __name__ == '__main__':
    filepath = "../../input.txt"
    integers = read_input(filepath)
    integers[1] = 12
    integers[2] = 2

    out = intcode(integers)
    print(out[0])
