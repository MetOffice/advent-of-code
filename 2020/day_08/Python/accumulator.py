from copy import copy

from common.loaders import load_string

def calculate_accumulator_value_part_1(program):
    """
    Return the accumulator value immediately before the instructions are
    repeated.

    Instructions are in the form ``XXX +/-#``:
    

    Parameters
    ----------
    program: list
        The instructions in the program.

    """
    accumulator_value = 0
    index = 0
    seen_indices = set()
    while index not in seen_indices:
        seen_indices.add(index)
        instruction = program[index]
        operation, argument = instruction.split()
        argument = int(argument)
        if operation == "acc":
            accumulator_value += argument
            index += 1
        elif operation == "jmp":
            index += argument
        elif operation == "nop":
            index += 1
        else:
            raise RuntimeError(f"Invalid operation: {operation}")
    return accumulator_value
    

def calculate_accumulator_value_part_2(program):
    """
    Return the accumulator value immediately before the instructions are
    repeated.

    Instructions are in the form ``XXX +/-#``:
    

    Parameters
    ----------
    program: list
        The instructions in the program.

    """
    accumulator_value = 0
    index = 0
    seen_indices = set()
    while index not in seen_indices:
        seen_indices.add(index)
        try:
            instruction = program[index]
        except IndexError:
            if index == len(program):
                return accumulator_value
        operation, argument = instruction.split()
        argument = int(argument)
        if operation == "acc":
            accumulator_value += argument
            index += 1
        elif operation == "jmp":
            index += argument
        elif operation == "nop":
            index += 1
        else:
            raise RuntimeError(f"Invalid operation: {operation}")
    raise RuntimeError("Infinite loop")


def fix_program(program):
    orig_program = program
    accumulator_value = None
    for index, instruction in enumerate(orig_program):
        program = copy(orig_program)
        if instruction.startswith("acc"):
            continue
        elif instruction.startswith("jmp"):
            program[index] = program[index].replace("jmp", "nop")
        elif instruction.startswith("nop"):
            program[index] = program[index].replace("nop", "jmp")
        else:
            raise RuntimeError(f"Invalid instruction: {instruction}")
        try:
            accumulator_value = calculate_accumulator_value_part_2(program)
        except RuntimeError:
            pass
        if accumulator_value:
            print(f"Edited instruction at index {index}: "
                  f"{orig_program[index]} --> {program[index]}")
            break
    return accumulator_value
    

if __name__ == "__main__":
    file_contents = load_string()
    accumulator_value = calculate_accumulator_value_part_1(file_contents)
    print(f"Part 1: {accumulator_value}")
    accumulator_value = fix_program(file_contents)
    print(f"Part 2: {accumulator_value}")
    
