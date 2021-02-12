from datetime import datetime
import functools


def do_twice(func):
    """Runs function func twice"""
    @functools.wraps(func)
    def _do_twice(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        return result1, result2

    return _do_twice


def print_duration(func):
    """
    Prints duration for running function func.
    """

    @functools.wraps(func)
    def _print_duration(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(
            f"Duration of {func.__name__} is {(end - start).total_seconds()} seconds."
        )
        return result

    func(0)
    datetime.now()
    return _print_duration


@do_twice  # applied second
@print_duration  # applied first
def prove1(number):
    """
    Prints number given as input, returns 2xnumber.
    """
    print(number)
    return number * 2


def main():
    print("Output from within decorated prove1:\n")
    prove1(5)
    print("\nOutput returned by decorated prove1:\n")
    print(prove1(5))
    print("\nDecorated prove1 docstring:")
    print(prove1.__doc__)


if __name__ == '__main__':
    main()
