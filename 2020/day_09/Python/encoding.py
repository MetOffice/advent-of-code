from common.loaders import load_string

from itertools import combinations

def format_input(file_contents):
    
    file_contents = [int(entry) for entry in file_contents]
    return file_contents

def validate(file_contents, preamble_length=25):
    for index in range(preamble_length, len(file_contents)):
        buffer = file_contents[index - preamble_length : index]
        if not check_combinations(file_contents[index], buffer):
            return file_contents[index]
    raise RuntimeError('All values can be calculated from previous values')


def check_combinations(target_value, combination_values):
    potential_targets = combinations(combination_values, 2)

    for potential_target in potential_targets:
        if sum(potential_target) == target_value:
            return True
    return False
    
if __name__ == "__main__":
    file_contents = load_string()
    input_list = format_input(file_contents)
    print(validate(input_list))
    
