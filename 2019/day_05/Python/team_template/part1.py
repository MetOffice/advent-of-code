from typing import List

from load_input import get_input

class Computer:
    def __init__(self, program: List):
        self.program = list(map(int, program))
        self.running = True
        self.pointer = 0
    
    # Function prototypes for opcodes

    # opcode 1
    def add(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.pointer + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.pointer + 2)]
        dest   = self.get_address(parameter_modes[2], self.pointer + 3)
        self.program[dest] = value1 + value2
        self.pointer += 4
    
    # opcode 2
    def mult(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.pointer + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.pointer + 2)]
        dest   = self.get_address(parameter_modes[2], self.pointer + 3)
        self.program[dest] = value1 * value2
        self.pointer += 4
    
    # opcode 3
    def get_and_store_input(self, parameter_modes):
        dest = self.get_address(parameter_modes[0], self.pointer + 1)
        input_int = int(input("Type a number."))
        self.program[dest] = input_int
        self.pointer += 2
    
    # opcode 4
    def output_int(self, parameter_modes):
        value = self.get_address(parameter_modes[0], self.pointer + 1)
        print(self.program[value])
        self.pointer += 2

    # opcode 5
    def jump_if_true(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.pointer + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.pointer + 2)]
        if value1 != 0:
            self.pointer = value2
        else:
            self.pointer += 3

    # opcode 6
    def jump_if_false(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.pointer + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.pointer + 2)]
        if value1 == 0:
            self.pointer = value2
        else:
            self.pointer += 3

    # opcode 7
    def less_than(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.pointer + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.pointer + 2)]
        dest   = self.get_address(parameter_modes[2], self.pointer + 3)
        if value1 < value2:
            self.program[dest] = 1
        else:
            self.program[dest] = 0
        self.pointer += 4
    
    # opcode 8
    def equals(self, parameter_modes):
        value1 = self.program[self.get_address(parameter_modes[0], self.pointer + 1)]
        value2 = self.program[self.get_address(parameter_modes[1], self.pointer + 2)]
        dest   = self.get_address(parameter_modes[2], self.pointer + 3)
        if value1 == value2:
            self.program[dest] = 1
        else:
            self.program[dest] = 0
        self.pointer += 4

    # opcode 99
    def die(self):
        self.running = False

    def get_address(self, mode, value):
        if mode == 0:
            result = self.program[value]
        else:
            result = value
        return result

    def parse_opcode(self):
        instruction = str(self.program[self.pointer])
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
            raise Exception("Unrecognised opcode: "
                  + str(opcode) + " at position " + str(self.pointer))

        return self.running


def intcode(input_data: List[str]) -> List:
    # load program
    computer = Computer(input_data)

    while computer.running:
        computer.parse_instruction()

    return computer.program


if __name__ == "__main__":
    input_data = get_input()
    intcode(input_data)
