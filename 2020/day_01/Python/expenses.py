from typing import Any, Union


def read_input(filepath):

    with open(filepath) as f:
        return list(map(int, f.readlines()))


def sum_to_target(transactions, target=2020):

    transactions = set(transactions)
    # also makes a set    {1,2,3}, but {} is an empty dictionary
    for bill in transactions:
        # sorry dave!
        if (target - bill) in transactions:
            return tuple(sorted((bill, (target - bill))))
            # defining a tuple


def find_target(transactions, target=2020):
    for number in transactions:
        new_target = target - number
        other_numbers = sum_to_target(transactions, new_target)
        if other_numbers is not None:
            return tuple(sorted((number, *other_numbers)))
        # * unpacks the tuple output by sum_to_target
        #


def main():

    transactions = read_input("../input.txt")
    # print(transactions)

    num1, num2 = sum_to_target(transactions)

    part1_answer = num1 * num2

    print(part1_answer)

    num1, num2, num3 = find_target(transactions, target=2020)

    part2_answer = num1 * num2 * num3

    print(part2_answer)


if __name__ == "__main__":
    main()
