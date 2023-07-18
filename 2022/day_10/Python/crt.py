
class CPU:
    def __init__(self, instruction_set) -> None:
        self.instruction_set = instruction_set
        self.reset()


    def reset(self):
        """
        Resets cycle number and x value to initial
        """
        self.cycle = 0
        self.x = 1


    def execute_program(self):
        """
        Executes an instruction set from a string
        """
        self.reset()
        instructions = self.instruction_set.splitlines()

        for instruction in instructions:
            self.execute_instruction(instruction)
            yield self.cycle, self.x


    def execute_instruction(self, instruction:str):
        """
        Execute a single instruction
        """
        command = instruction[:4]
        match command:
            case "addx":
                arg = int(instruction[4:])
                self.addx(arg)
            case "noop":
                self.noop()
            case _:
                raise Exception(f"{command} is not a real command")


    def noop(self):
        """
        Executes a noop command
        """
        self.cycle += 1 # pass cycles method?


    def addx(self, arg):
        """
        Executes an addx command, adding arg to x value
        """
        self.cycle += 2
        self.x += int(arg)


def x_at_cycles(instruction_set, output_cycles:list):
    """
    For a list of cycles of interest, output the
    values at those cycles
    """
    cpu = CPU(instruction_set)
    for cycle, x in cpu.execute_program():
        