from common.loaders import load_string

def calculate_accumulator_value(program):
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
    

if __name__ == "__main__":
    file_contents = load_string()
    accumulator_value = calculate_accumulator_value(file_contents)
    print(f"Part 1: {accumulator_value}")
