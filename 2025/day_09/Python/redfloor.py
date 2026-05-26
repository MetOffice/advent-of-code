import numpy as np


def read_file():
    with open("../input.txt", "r") as file:
        lines = file.readlines()
    return np.array([[int(a) for a in line.strip().split(",")] for line in lines])


def calc_area(point1, point2):
    # 3d points
    width = abs(point1[0] - point2[0]) + 1
    height = abs(point1[1] - point2[1]) + 1
    return width * height

def calc_pairs(array):
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            result.append((calc_area(array[i], array[j]), i, j))
    return result

def main():
    red_tiles = read_file()
    pairs = calc_pairs(red_tiles)
    pairs_sorted = sorted(pairs, key=lambda tup: tup[0], reverse=True)
    biggest = pairs_sorted[0]
    print(red_tiles[biggest[1]])
    print(red_tiles[biggest[2]])
    print(biggest)



if __name__ == "__main__":
    main()
