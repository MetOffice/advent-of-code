#!/usr/bin/env python
from common.loaders import load_string
import copy

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

def find_oxygen_rating(report):
    """From binary report, find the oxygen generation rating value as a decimal."""
    report_copy = copy.deepcopy(report)
    number_of_columns = len(report[0])

    # run through columns, remove any lines that don't match the most common bit
    # of that column
    for column in range(number_of_columns):
        # find_most_common_bit throws a ValueError if there is no most common bit
        # (i.e. the number of 1s and 0s in the columns is the same!)
        try:
            bit = find_most_common_bit(report_copy, column)
        except ValueError:
            bit = 1 # for oxygen, if 0 and 1 are equally common, pick 1 as most common
        report_copy = [line for line in report_copy if int(line[column]) == bit]
        if len(report_copy) == 1:
            break

    # now, len(report_copy) == 1 (in principle!)
    binary_oxygen_rating = report_copy[0]
    decimal_oxygen_rating = int(''.join(binary_oxygen_rating), 2)
    
    return decimal_oxygen_rating

def find_co2_rating(report):
    """From binary report, find the CO2 generation rating value as a decimal."""
    report_copy = copy.deepcopy(report)
    number_of_columns = len(report[0])

    # run through columns, remove any lines that don't match the least common bit
    # of that column
    for column in range(number_of_columns):
        # find_least_common_bit throws a ValueError if there is no least common bit
        # (i.e. the number of 1s and 0s in the columns is the same!)
        try:
            bit = find_least_common_bit(report_copy, column)
        except ValueError:
            bit = 0 # for CO2, if 0 and 1 are equally common, pick 0 as least common
        report_copy = [line for line in report_copy if int(line[column]) == bit]
        if len(report_copy) == 1:
            break

    # now, len(report_copy) == 1 (in principle!)
    binary_co2_rating = report_copy[0]
    decimal_co2_rating = int(''.join(binary_co2_rating), 2)
    
    return decimal_co2_rating
    

def main():
    report = load_string()
    epsilon = get_epsilon_rate(report)
    gamma = get_gamma_rate(report)
    power_consumption = epsilon * gamma
    print(f"Part 1 result: {power_consumption}")

    oxygen_rating = find_oxygen_rating(report)
    co2_rating = find_co2_rating(report)
    life_support_rating = oxygen_rating * co2_rating
    print(f"Part 2 result: {life_support_rating}")

if __name__ == '__main__':
    main()
