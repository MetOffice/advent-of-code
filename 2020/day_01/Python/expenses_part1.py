from typing import Any, Union


def read_input(filepath):

    with open(filepath) as f:
        return list(map(int, f.readlines()))

def sum_to_2020(transactions):

    transactions = set(transactions)
    # also makes a set    {1,2,3}, but {} is an empty dictionary
    for bill in transactions:
        # sorry dave!
        if (2020 - bill) in transactions:
            return tuple(sorted((bill, (2020 - bill))))
            # defining a tuple



def main():

    transactions = read_input('../input.txt')
    # print(transactions)

    num1, num2 = sum_to_2020(transactions)

    answer = num1 * num2

    print(answer)

if __name__ == '__main__':
    main()

