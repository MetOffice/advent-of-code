from itertools import permutations
from typing import List, Optional, Tuple

from load_input import get_input


class Computer:
    """
    The program list contains one or more instructions and corresponding
    parameters. An instruction may contain one digit, e.g. 1 (a
    one-digit opcode with the leading zero removed), three digits, e.g.
    102 (a two-digit opcode and one parameter mode with two leading
    zeros removed), or four digits, e.g. 1002 (a two-digit opcode and
    two parameters modes with one leading zero removed):

    ABCDE
     1002

    DE - two-digit opcode
    C - mode of 1st parameter
    B - mode of 2nd parameter
    A - mode of 3rd parameter

    where:

    02 == opcode 2
    0 == position mode
    1 == immediate mode
    0 == position mode, omitted due to being a leading zero

    The mode can be either 0 or 1, where 0 refers to position mode,
    which means the value of the item refers to the index in the program
    list to be used, and 1 refers to immediate mode, which means the
    value of the item in the program list is used directly.

    ``parameter_modes`` is a list containing 3 integers corresponding
    to the modes of the 1st, 2nd and 3rd parameter, respectively (which
    differs from the description in the puzzles as described above, see
    also the ``parse_opcode`` method).
    """
    def __init__(self, program: List[int], input_buffer: List[int] = None):
        """
        Parameters
        ----------
        program: list of integers
            The intcode program.
        input_buffer: list of integers
            The input.
        """
        self.program = program
        self.running = True
        self.next_instruction_index = 0
        self.input_buffer = input_buffer
        if self.input_buffer is None:
            self.input_buffer = []
        self.last_output = None
        self.status = "created"

    # Function prototypes for opcodes

    # opcode 1
    def add(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.next_instruction_index + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.next_instruction_index + 2)]
        dest = self.get_address(parameter_modes[2], self.next_instruction_index + 3)
        self.program[dest] = value1 + value2
        self.next_instruction_index += 4

    # opcode 2
    def mult(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.next_instruction_index + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.next_instruction_index + 2)]
        dest = self.get_address(parameter_modes[2], self.next_instruction_index + 3)
        self.program[dest] = value1 * value2
        self.next_instruction_index += 4

    # opcode 3
    def get_and_store_input(self, parameter_modes):
        """
        Get an input. Consume inputs from the input buffer before prompting
        with input().
        """
        dest = self.get_address(parameter_modes[0], self.next_instruction_index + 1)
        if len(self.input_buffer) > 0:
            input_int = self.input_buffer.pop(0)
        else:
            self.wait()
            return
        self.program[dest] = input_int
        self.next_instruction_index += 2

    # opcode 4
    def output_int(self, parameter_modes):
        value = self.get_address(parameter_modes[0], self.next_instruction_index + 1)
        #print(self.program[value])
        self.last_output = self.program[value]
        self.next_instruction_index += 2

    # opcode 5
    def jump_if_true(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.next_instruction_index + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.next_instruction_index + 2)]
        if value1 != 0:
            self.next_instruction_index = value2
        else:
            self.next_instruction_index += 3

    # opcode 6
    def jump_if_false(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.next_instruction_index + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.next_instruction_index + 2)]
        if value1 == 0:
            self.next_instruction_index = value2
        else:
            self.next_instruction_index += 3

    # opcode 7
    def less_than(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.next_instruction_index + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.next_instruction_index + 2)]
        dest = self.get_address(parameter_modes[2], self.next_instruction_index + 3)
        if value1 < value2:
            self.program[dest] = 1
        else:
            self.program[dest] = 0
        self.next_instruction_index += 4

    # opcode 8
    def equals(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.next_instruction_index + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.next_instruction_index + 2)]
        dest = self.get_address(parameter_modes[2], self.next_instruction_index + 3)
        if value1 == value2:
            self.program[dest] = 1
        else:
            self.program[dest] = 0
        self.next_instruction_index += 4

    # opcode 99
    def die(self):
        self.running = False
        self.status = "completed"

    def wait(self):
        self.running = False
        self.status = "waiting"

    def get_address(self, mode, value):
        if mode == 0:
            result = self.program[value]
        else:
            result = value
        return result

    def parse_opcode(self):
        instruction = str(self.program[self.next_instruction_index])
        opcode = int(instruction[-2:])

        parameter_modes = [0, 0, 0]
        if len(instruction) == 3:
            parameter_modes[0] = int(instruction[0])
        elif len(instruction) == 4:
            parameter_modes[0] = int(instruction[1])
            parameter_modes[1] = int(instruction[0])
        elif len(instruction) == 5:
            parameter_modes[0] = int(instruction[2])
            parameter_modes[1] = int(instruction[1])
            parameter_modes[2] = int(instruction[0])

        return opcode, parameter_modes

    def parse_instruction(self):
        (opcode, parameter_modes) = self.parse_opcode()
        # Do something magical with opcodes here
        if opcode == 1:
            # add
            self.add(parameter_modes)
        elif opcode == 2:
            # multiply
            self.mult(parameter_modes)
        elif opcode == 3:
            self.get_and_store_input(parameter_modes)
        elif opcode == 4:
            self.output_int(parameter_modes)
        elif opcode == 5:
            self.jump_if_true(parameter_modes)
        elif opcode == 6:
            self.jump_if_false(parameter_modes)
        elif opcode == 7:
            self.less_than(parameter_modes)
        elif opcode == 8:
            self.equals(parameter_modes)
        elif opcode == 99:
            self.die()
        else:
            raise Exception(
                "Unrecognised opcode: "
                + str(opcode)
                + " at position "
                + str(self.next_instruction_index)
            )

        return self.running

    def run(self):
        if self.status == "completed":
            raise Exception("Computer has already completed - can't run again")
        else:
            self.running = True
            self.status = "running"

        while self.running:
            self.parse_instruction()

    def add_input(self, _input):
        self.input_buffer.append(_input)


def run_feedback_loop(program: List[int], phases: List[int]) -> int:
    amplifiers = []
    for phase in phases:
        input_buffer = [phase]
        amplifiers.append(Computer(program.copy(), input_buffer))

    first = True
    while True:
        if amplifiers[-1].status == "completed":
            break
        for i, amp in enumerate(amplifiers):
            if first == True:
                _input = 0
                first = False
            elif i == 0:
                _input = amplifiers[-1].last_output
            else:
                _input = amplifiers[i-1].last_output
            amp.add_input(_input)
            amp.run()

    return amplifiers[-1].last_output


def find_settings(program: List[int]) -> Tuple[List[int], int]:
    max_value = 0
    max_setting = None
    for setting in permutations(range(5, 10)):
        result = run_feedback_loop(program, setting)
        if result > max_value:
            max_value = result
            max_setting = setting

    return (list(max_setting), max_value)


if __name__ == "__main__":
    input_data = get_input()
    settings = find_settings(input_data)
    print(settings)
