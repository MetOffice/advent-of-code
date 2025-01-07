from collections import Counter
from os.path import split
from typing import List


def read_file() -> List[List[int]]:
    with open("../input", "r") as file:
        lines = file.readlines()
        list_1 = []
        list_2 = []

        for line in lines:
            a,b = line.split()
            list_1.append(int(a))
            list_2.append(int(b))

        list_1.sort()
        list_2.sort()

        return [list_1, list_2]


def main():
    list_1, list_2 = read_file()
    counts = Counter(list_2)
    result = sum([counts[loc] * loc for loc in list_1])
    print(result)


def part1():
    list_1, list_2 = read_file()
    pairs = zip(list_1,list_2)
    result = sum([abs(a-b) for a,b in pairs])
    print(result)


if __name__=="__main__":
    main()
