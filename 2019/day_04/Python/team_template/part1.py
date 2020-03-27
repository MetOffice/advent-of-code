from load_input import get_input


def is_valid_password(password: str) -> bool:
    # Note - the tests use this function name - update them if you rename this
    return True


def count_possible_passwords(min_: int, max_: int) -> int:
    return 0


if __name__ == "__main__":
    input_ = get_input()
    print(input_)
    result = count_possible_passwords(int(input_.min), int(input_.max))
    print(result)
