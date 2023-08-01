
class CPU:
    def __init__(self, instruction_set) -> None:
        self.instruction_set = instruction_set
        self.reset()


    def reset(self):
        """
        Resets cycle number and x value to initial
        """
        # Cycle starts at 1 to account for difference between the end and middle of cycles in adds.
        self.cycle = 1
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


def x_at_cycle(instruction_set, output_cycle: int) -> tuple[int, int]:
    """
    For a single cycle of interest, execute the program until the cycle is reached.
    If an add occurs over the boundary we stop at output_cycle+1, then take the previous value of x
    As the add would not have completed at output_cycle.
    Line #160/161 of the test is causing an issue (addx 2, addx 1) at cycle 216/218
    This could be adapted to only require one pass for all the output cycles required (but let's get this working first!)
    :param instruction_set:
    :param output_cycle:
    :return:
    """
    cpu = CPU(instruction_set)
    x_old = cpu.x
    for cycle, x in cpu.execute_program():
        if cycle == output_cycle:
            return cycle, x
        elif cycle == output_cycle + 1:
            return (cycle - 1), x_old
        x_old = x
    raise Exception("Unreachable")


def signal_strength_at_cycles(instruction_set, output_cycles: list[int]) -> list[int]:
    """
    For a list of cycles of interest, calculate the signal strength (x_register * cycle)
    """
    result = [x_at_cycle(instruction_set, val) for val in output_cycles]
    return [a * b for a, b in result]

def signal_strength(instruction_set, output_cycles: list[int]) -> int:
    return sum(signal_strength_at_cycles(instruction_set, output_cycles))
