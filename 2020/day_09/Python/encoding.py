from common.loaders import load_string

from itertools import combinations

def format_input(file_contents):
    
    file_contents = [int(entry) for entry in file_contents]
    return file_contents

def find_invalid_number(file_contents, preamble_length=25):
    for index in range(preamble_length, len(file_contents)):
        buffer = file_contents[index - preamble_length : index]
        if not validate_target(file_contents[index], buffer):
            return file_contents[index]
    raise RuntimeError('All values can be calculated from previous values')


def validate_target(target_value, combination_values):
    potential_targets = combinations(combination_values, 2)

    for potential_target in potential_targets:
        if sum(potential_target) == target_value:
            return True
    return False


def find_chunk(values, target):
    start_index = 0
    end_index = 2

    while sum(values[start_index : end_index]) != target:
        total = sum(values[start_index : end_index])
        if total < target:
            end_index += 1
        else:
            start_index += 1
        
    return values[start_index : end_index]

            
def calculate_result(values):
    return min(values) + max(values)


if __name__ == "__main__":
    file_contents = load_string()
    input_list = format_input(file_contents)
    target = find_invalid_number(input_list)

    chunk = find_chunk(input_list, target)
    result = calculate_result(chunk)
    
    print(f'Part 1: Target {target}, Part 2: Result {result}')
