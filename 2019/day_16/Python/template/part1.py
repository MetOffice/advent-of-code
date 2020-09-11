from datetime import datetime

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
    last_digit = abs(result) % 10
    return int(last_digit)
        

def calculate_phase(input_value):
    result = []
    base_pattern = [0, 1, 0, -1]
    for index in range(1, len(input_value)+1):
        pattern = perturb_pattern(base_pattern, index)
        start = datetime.now()
        digit = calculate_digit(input_value, pattern)
        end = datetime.now()
        duration = end - start
        print(f'Duration of calculate_digit for iteration {index} of '
              f'{len(input_value)}: {duration.total_seconds()} seconds')
        result.append(digit)
    return result


def perturb_pattern(pattern, repetition):
    output_list = []
    for digit in pattern:
        for index in range(repetition):
            output_list.append(digit)
    return output_list


def main():
    phase_input = get_input()
    message_location = int(''.join(str(digit) for digit in phase_input[:7]))
    phase_input = phase_input * 10000
    num_phases = 100
    for phase in range(num_phases):
        print(f'Calculating digits for phase {phase} of {num_phases}')
        start = datetime.now()
        phase_input = calculate_phase(phase_input)
        end = datetime.now()
        duration = end - start
        print(f'Duration of calculate_phase for phase {phase} of '
              f'{num_phases}: {duration.total_seconds()} seconds')
    return phase_input[message_location:message_location + 8]


if __name__ == '__main__':
    print(main())
