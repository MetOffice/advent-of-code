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
        self._running = True
        self._next_instruction_index = 0
        self._input_buffer = input_buffer
        if self._input_buffer is None:
            self._input_buffer = []
        self.last_output = None
        self._status = "created"

    # Function prototypes for opcodes

    # opcode 1
    def _add(self, parameter_modes):
        value1 = self.program[self._get_address(parameter_modes[0], self._next_instruction_index + 1)]
        value2 = self.program[self._get_address(parameter_modes[1], self._next_instruction_index + 2)]
        dest = self._get_address(parameter_modes[2], self._next_instruction_index + 3)
        self.program[dest] = value1 + value2
        self._next_instruction_index += 4

    # opcode 2
    def _mult(self, parameter_modes):
        value1 = self.program[self._get_address(parameter_modes[0], self._next_instruction_index + 1)]
        value2 = self.program[self._get_address(parameter_modes[1], self._next_instruction_index + 2)]
        dest = self._get_address(parameter_modes[2], self._next_instruction_index + 3)
        self.program[dest] = value1 * value2
        self._next_instruction_index += 4

    # opcode 3
    def _get_and_store_input(self, parameter_modes):
        """
        Get an input. Consume inputs from the input buffer before prompting
        with input().
        """
        dest = self._get_address(parameter_modes[0], self._next_instruction_index + 1)
        if len(self._input_buffer) > 0:
            input_int = self._input_buffer.pop(0)
        else:
            self._wait()
            return
        self.program[dest] = input_int
        self._next_instruction_index += 2

    # opcode 4
    def _output_int(self, parameter_modes):
        value = self._get_address(parameter_modes[0], self._next_instruction_index + 1)
        #print(self.program[value])
        self.last_output = self.program[value]
        self._next_instruction_index += 2

    # opcode 5
    def _jump_if_true(self, parameter_modes):
        value1 = self.program[self._get_address(parameter_modes[0], self._next_instruction_index + 1)]
        value2 = self.program[self._get_address(parameter_modes[1], self._next_instruction_index + 2)]
        if value1 != 0:
            self._next_instruction_index = value2
        else:
            self._next_instruction_index += 3

    # opcode 6
    def _jump_if_false(self, parameter_modes):
        value1 = self.program[self._get_address(parameter_modes[0], self._next_instruction_index + 1)]
        value2 = self.program[self._get_address(parameter_modes[1], self._next_instruction_index + 2)]
        if value1 == 0:
            self._next_instruction_index = value2
        else:
            self._next_instruction_index += 3

    # opcode 7
    def _less_than(self, parameter_modes):
        value1 = self.program[self._get_address(parameter_modes[0], self._next_instruction_index + 1)]
        value2 = self.program[self._get_address(parameter_modes[1], self._next_instruction_index + 2)]
        dest = self._get_address(parameter_modes[2], self._next_instruction_index + 3)
        if value1 < value2:
            self.program[dest] = 1
        else:
            self.program[dest] = 0
        self._next_instruction_index += 4

    # opcode 8
    def _equals(self, parameter_modes):
        value1 = self.program[self._get_address(parameter_modes[0], self._next_instruction_index + 1)]
        value2 = self.program[self._get_address(parameter_modes[1], self._next_instruction_index + 2)]
        dest = self._get_address(parameter_modes[2], self._next_instruction_index + 3)
        if value1 == value2:
            self.program[dest] = 1
        else:
            self.program[dest] = 0
        self._next_instruction_index += 4

    # opcode 99
    def _die(self):
        self._running = False
        self._status = "completed"

    def _wait(self):
        self._running = False
        self._status = "waiting"

    def _get_address(self, mode, value):
        if mode == 0:
            result = self.program[value]
        else:
            result = value
        return result

    def _parse_opcode(self):
        instruction = str(self.program[self._next_instruction_index])
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

    def _parse_instruction(self):
        (opcode, parameter_modes) = self._parse_opcode()
        # Do something magical with opcodes here
        if opcode == 1:
            # add
            self._add(parameter_modes)
        elif opcode == 2:
            # multiply
            self._mult(parameter_modes)
        elif opcode == 3:
            self._get_and_store_input(parameter_modes)
        elif opcode == 4:
            self._output_int(parameter_modes)
        elif opcode == 5:
            self._jump_if_true(parameter_modes)
        elif opcode == 6:
            self._jump_if_false(parameter_modes)
        elif opcode == 7:
            self._less_than(parameter_modes)
        elif opcode == 8:
            self._equals(parameter_modes)
        elif opcode == 99:
            self._die()
        else:
            raise Exception(
                "Unrecognised opcode: "
                + str(opcode)
                + " at position "
                + str(self._next_instruction_index)
            )

        return self._running

    def run(self):
        if self._status == "completed":
            raise Exception("Computer has already completed - can't run again")
        else:
            self._running = True
            self._status = "running"

        while self._running:
            self._parse_instruction()

    def _add_input(self, _input):
        self._input_buffer.append(_input)


def run_feedback_loop(program: List[int], phases: List[int]) -> int:
    """
    Returns output from last amplifier after all amplifiers have run.

    TODO: Evaluate if this belongs in day 7 only, or should be part of the
    common computer code.

    This is the infrastructure for part 2 of day 7.  There's multiple
    amplifiers in sequence, where each amplifier is an instance of the intcode
    computer.  All amplifiers run the same program.  One amplifier is
    generated for each provided phase (5 phases for the day 7 puzzle).  The
    phase is the first input for each amplifier.  At the start, an input value
    of zero is provided as the second input for the first amplifier.
    Subsequently, The output for amplifier N is plumbed to the input for
    amplifier N+1.  For the final amplifier in the chain, the output is
    plumbed to the input of the first amplifier.

    An amplifier continues running until it either reaches the stop opcode
    (99), or it requests input that has not yet been provided by the output
    from the preceding amplifier.  Once an amplifier executes the stop opcode,
    it does not resume execution.  An amplifier waiting for input will resume
    when the input is provided.

    Returns the final output for the final amplifier when all amplfiers have
    stopped.

    """
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
    """
    Return combination of phases to maximise the output of the chain of
    amplifiers.

    TODO: Evaluate if this belongs in day 7 only, or should be part of the
    common computer code.

    Finds which sequence of phases (5, 6, 7, 8, 9), results in the largest
    signal from the amplifier chain.  See run_feedback_loop for details of the
    amplifiers, and how the phase is interpreted.

    """
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
