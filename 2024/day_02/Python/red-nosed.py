import copy
from collections import Counter
from math import copysign
from typing import List, LiteralString, Literal


def read_file() -> List[List[int]]:
    with open("../input", "r") as file:
        lines = file.readlines()
        return [[int(i) for i in line.split(" ")] for line in lines]

def check_report(report: List[int], depth=0) -> Literal["SAFE", "UNSAFE"]:
    if depth > 1:
        return "UNSAFE"
    sign = copysign(1,report[0] - report[1])
    for i in range(len(report) - 1):
        diff = report[i] - report[i+1]
        if not (3 >= abs(diff) >= 1 and sign == copysign(1,diff)) :

            check_report(report[::i]+report[i+1::], depth+1)
            check_report(report[::i+1]+report[i+2::], depth+1)

            return check_report(report[::i]+report[i+1::], depth+1)

    return "SAFE"

[3,5,9,6,8]

def main():
    reports = read_file()
    result = Counter([check_report(report) for report in reports])
    print(result)



if __name__=="__main__":
    main()