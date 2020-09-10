from load_input import get_input
from itertools import cycle


def calculate_digit(input_value, pattern):
    result = 0
    # Want to ignore the first digit in the pattern
    pattern_cycle = cycle(pattern)
    next(pattern_cycle)
    for (input_digit, pattern_digit) in zip(input_value, pattern_cycle):
        result += input_digit * pattern_digit
    # Only want to return the last digit of the sum
    result_string = str(result)[-1]
    return int(result_string)
        

def calculate_phase(input_value):
    result = []
    base_pattern = [0, 1, 0, -1]
    for index in range(1, len(input_value)+1):
        pattern = perturb_pattern(base_pattern, index)
        result.append(calculate_digit(input_value, pattern))
    return result


def perturb_pattern(pattern, repetition):
    output_list = []
    for digit in pattern:
        for index in range(repetition):
            output_list.append(digit)
    return output_list


def main():
    phase_input = get_input()
    for phase in range(100):
        phase_input = calculate_phase(phase_input)
    return phase_input[:8]

if __name__ == "__main__":
    print(main())
