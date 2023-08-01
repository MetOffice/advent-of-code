clock_cycle_list = list[int]

def parse_instructions(instructions: str) -> clock_cycle_list:
    """
    Generates a list of integers for what is happening at that clock cycle.
    """
    clock_cycles = []
    for instruction in instructions.splitlines():
        command = instruction[:4]
        match command:
            case "addx":
                clock_cycles.append(0)
                clock_cycles.append(int(instruction[4:]))
            case "noop":
                clock_cycles.append(0)
            case _:
                raise Exception(f"{command} is not a real command")
    return clock_cycles

def sum_cycles(parsed_clock_cycles: clock_cycle_list, target_cycle: int) -> int:
    return sum(parsed_clock_cycles[:target_cycle]) + 1


def x_at_cycle(program: str, target_cycle: int) -> tuple[int, int]:
    return target_cycle, sum_cycles(parse_instructions(program), target_cycle)
