import common

def parse_input(contents):
    for line in contents:
        count, character, password = line.split()
        min_count, max_count = count.split('-')
        character = character.strip(':')
        yield int(min_count), int(max_count), character, password

def validate_password_part_1(min_count, max_count, character, password):
    """
    Return whether password is valid

    Returns
    -------
    : bool
        Whether the password is valid
    """
    return min_count <= password.count(character) <= max_count


def validate_password_part_2(position_1, position_2, character, password):
    """
    Return whether password is valid

    Returns
    -------
    : bool
        Whether the password is valid
    """
    position_1 = position_1 - 1
    position_2 = position_2 - 1

    matches = 0

    if password[position_1] == character:
        matches += 1
    
    if password[position_2] == character:
        matches += 1

    return matches == 1


def main():
    contents = common.loaders.load_string()
    valid_passwords_part_1 = 0
    valid_passwords_part_2 = 0
    for min_count, max_count, character, password in parse_input(contents):
        if validate_password_part_1(min_count, max_count, character, password):
            valid_passwords_part_1 += 1
        if validate_password_part_2(min_count, max_count, character, password):
            valid_passwords_part_2 += 1            
    return valid_passwords_part_1, valid_passwords_part_2


if __name__ == "__main__":
    result_part_1, result_part_2 = main()
    print(f'Number of valid passwords for part 1 = {result_part_1}')
    print(f'Number of valid passwords for part 2 = {result_part_2}')

