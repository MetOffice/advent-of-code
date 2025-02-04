import copy
from collections import Counter
from math import copysign
from typing import List, Literal


def read_file() -> List[List[int]]:
    with open("../input", "r") as file:
        lines = file.readlines()
        return [[int(i) for i in line.split(" ")] for line in lines]


def check_report_pt1(report: List[int]) -> Literal["SAFE", "UNSAFE"]:
    temp_list = copy.copy(report)
    temp_list.sort()

    temp_list_2 = copy.copy(report)
    temp_list_2.sort(reverse=True)
    if not (report == temp_list or report == temp_list_2):
        return "UNSAFE"

    ## check second condition
    ## difference between numbers in report

    for i in range(len(report) - 1):
        diff = report[i] - report[i+1]
        if not (3 >= abs(diff) >= 1):
            return "UNSAFE"

    return "SAFE"

def check_report(report: List[int], depth=0) -> Literal["SAFE", "UNSAFE"]:
    if depth > 1:
        return "UNSAFE"
    sign = modal_sign(report)
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (3 >= abs(diff) >= 1 and sign == copysign(1, diff)):
            if (
                    check_report(report[:i] + report[i + 1:], depth + 1) == "SAFE" or
                    check_report(report[:i + 1] + report[i + 2:], depth + 1) == "SAFE"
            ):
                return "SAFE"
            else:
                return "UNSAFE"

    return "SAFE"

def modal_sign(report: List[int]) -> float:
    total = 0
    for i in range(len(report) - 1):
        total += copysign(1, report[i + 1] - report[i])
    return copysign(1, total)

def main():
    reports = read_file()
    result = Counter([check_report(report) for report in reports])
    print(result)



if __name__=="__main__":
    main()