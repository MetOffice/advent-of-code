import copy
from collections import Counter
from typing import List, LiteralString, Literal


def read_file() -> List[List[int]]:
    with open("../input", "r") as file:
        lines = file.readlines()
        return [[int(i) for i in line.split(" ")] for line in lines]

def check_report(report: List[int]) -> Literal["SAFE", "UNSAFE"]:
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


def main():
    reports = read_file()
    result = Counter([check_report(report) for report in reports])
    print(result)



if __name__=="__main__":
    main()