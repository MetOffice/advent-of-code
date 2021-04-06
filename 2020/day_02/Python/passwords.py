import common
import re
from typing import List, Tuple


def parse_input(contents: List[str]) -> Tuple[int, int, str, str]:
    """
    Yield input extracted from the contents.

    This function uses regular expressions, useful references:

    * https://regex101.com/
    * https://alf.nu/RegexGolf
    * https://docs.python.org/3/library/re.html
    * :mod:`re`

    Parameters
    ----------
    contents : list[str]
        A list of strings of the format int-int char: password

    Yields
    ------
    tuple(int, int, char, password)
        input extracted from contents
    """

    # Example: 1-3 a: abcde
    pattern = r"""
    ^                      # start of line
    (?P<min_count>\d+)     # one or more digits, 1 from Example
    -                      # literal -
    (?P<max_count>\d+)     # one or more digits, 3 from Example
    \s*                    # 0 or more whitespace characters
    (?P<character>\w)      # One character, a from Example
    :                      # literal :
    \s*                    # 0 or more whitespace characters
    (?P<password>\w+)      # One or more characters, abcde from Example
    $                      # End of line
    """

    for line in contents:
        # re.search will search through the entire string for the pattern.
        # re.match will match from the start of the string
        # re.VERBOSE: https://docs.python.org/3/howto/regex.html#using-re-verbose
        # Using match groups: https://docs.python.org/3/library/re.html#re.Match.group
        matched = re.search(pattern, line, re.VERBOSE)
        if matched:
            min_count = int(matched.group('min_count'))
            max_count = int(matched.group('max_count'))
            character = matched.group('character')
            password = matched.group('password')
            yield min_count, max_count, character, password


def validate_password_part_1(min_count, max_count, character, password):
    """
    Return whether password is valid

    Returns
    -------
    bool
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

