from load_input import get_input


def does_repeat(password: str) -> bool:

    does_repeat = False
    for i, digit in enumerate(password[:-1]):
        if digit == password[i + 1]:
            does_repeat = True
            break

    return does_repeat


def not_decreasing(password: str) -> bool:

    not_decreasing = True
    for i, digit in enumerate(password[:-1]):
        if int(digit) > int(password[i+1]):
            not_decreasing = False
            break

    return not_decreasing


def is_valid_password(password: str) -> bool:
    # Note - the tests use this function name - update them if you rename this
    # two adjacent digits are the same

    return does_repeat(password) and not_decreasing(password)


def count_possible_passwords(min_: str, max_: str) -> int:

    count = 0
    for password in range(int(min_), int(max_)+1):
        if is_valid_password(str(password)):
            print(password)
            count += 1

    return count


if __name__ == "__main__":
    input_ = get_input()
    print(input_)
    result = count_possible_passwords(input_.min, input_.max)
    print(result)
