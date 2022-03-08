#!/usr/bin/env python
from common.loaders import load_string


def find_most_common_bit(report, column):
    """Return most common bit in the column of the report."""
    column_data = [int(line[column]) for line in report]
    threshold = len(column_data)/2.
    column_sum = sum(column_data)
    if column_sum > threshold:
        result = 1
    elif column_sum < threshold:
        result = 0
    else:
        raise ValueError("Question makes no sense")

    return result


def find_least_common_bit(report, column):
    """Return least common bit in the column of the report."""
    most_common_bit = find_most_common_bit(report, column)
    return 1 - most_common_bit


def get_gamma_rate(report):
    """Return decimal gamma rate from binary report."""
    number_of_columns = len(report[0])
    binary_gamma_rate = []
    for column in range(number_of_columns):
        binary_gamma_rate.append(str(find_most_common_bit(report, column)))
    decimal_gamma_rate = int(''.join(binary_gamma_rate), 2)
    return decimal_gamma_rate


def get_epsilon_rate(report):
    """Return decimal gamma rate from binary report."""
    number_of_columns = len(report[0])
    # Max possible value minus gamma rate is equivalent to binary inverse of the gamma rate.
    # Max number of values is 2**number of columns, but counting from 0 means we're going from 0 to max number of values - 1.
    return ((2**number_of_columns) - 1) - get_gamma_rate(report)


def main():
    report = load_string()
    epsilon = get_epsilon_rate(report)
    gamma = get_gamma_rate(report)
    power_consumption = epsilon * gamma
    print(f"Part 1 result: {power_consumption}")


if __name__ == '__main__':
    main()
