from typing import List

from load_input import get_input

class Computer:
    def __init__(self, program: List):
        self.program = list(map(int, program))
        self.running = True
        self.pointer = 0
    
    # Function prototypes for opcodes

    # opcode 1
    def add(self):
        value1 = self.program[self.pointer + 1]
        value2 = self.program[self.pointer + 2]
        dest   = self.program[self.pointer + 3]
        self.program[dest] = value1 + value2
        self.pointer += 4
    
    # opcode 2
    def mult(self):
        value1 = self.program[self.pointer + 1]
        value2 = self.program[self.pointer + 2]
        dest   = self.program[self.pointer + 3]
        self.program[dest] = value1 * value2
        self.pointer += 4
    
    # opcode 3
    def get_and_store_input(self):
        dest = self.program[self.pointer + 1]
        input_int = int(input("Type a number."))
        self.program[dest] = input_int
        self.pointer += 2
    
    # opcode 4
    def output_int(self):
        value = self.program[self.pointer + 1]
        print(self.program[value])
        self.pointer += 2
    
    # opcode 99
    def die(self):
        self.running = False
    
    def parse_instruction(self):
        opcode = self.program[self.pointer]

        # Do something magical with opcodes here
        if opcode == 1:
            # add
            self.add()
        elif opcode == 2:
            # multiply
            self.mult()
        elif opcode == 3:
            self.get_and_store_input()
        elif opcode == 4:
            self.output_int()
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


if __name__ == "__main__":
    input_data = get_input()
    ID_input = 1
    intcode(input_data)
