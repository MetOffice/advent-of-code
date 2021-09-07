from typing import List, Optional

from common.loaders import load_string


class InfiniteLoopException(RuntimeError):
    def __init__(self, accumulator):
        message = f"Infinite loop error - accumulator = {accumulator}"
        super().__init__(message)
        self.accumulator = accumulator


def run(program):
    """
    Run the program until the final instruction in the list is run or a loop is found.

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
    raise InfiniteLoopException(accumulator_value)


def fix_program(program: List[str]) -> Optional[int]:
    for index, instruction in enumerate(program):
        if instruction.startswith("acc"):
            continue
        new_program = program.copy()
        if instruction.startswith("jmp"):
            new_program[index] = new_program[index].replace("jmp", "nop")
        elif instruction.startswith("nop"):
            new_program[index] = new_program[index].replace("nop", "jmp")
        else:
            raise RuntimeError(f"Invalid instruction: {instruction}")
        try:
            accumulator_value = run(new_program)
            print(
                f"Edited instruction at index {index}: "
                f"{program[index]} --> {new_program[index]}"
            )
            return accumulator_value
        except RuntimeError:
            continue
    return None


if __name__ == "__main__":
    file_contents = load_string()
    try:
        accumulator_value_2 = run(file_contents)
        raise Exception("No loop found")
    except InfiniteLoopException as exc:
        print(f"Part 1: {exc.accumulator}")

    accumulator_value = fix_program(file_contents)
    print(f"Part 2: {accumulator_value}")
