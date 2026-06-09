import numpy as np
import tqdm
from shapely import Polygon


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

def get_bounds(red_tiles):
    max_x = max(t[0] for t in red_tiles)
    max_y = max(t[1] for t in red_tiles)
    return max_x, max_y

def part1():
    red_tiles = read_file()
    pairs = calc_pairs(red_tiles)
    pairs_sorted = sorted(pairs, key=lambda tup: tup[0], reverse=True)
    biggest = pairs_sorted[0]
    print(red_tiles[biggest[1]])
    print(red_tiles[biggest[2]])
    print(biggest)

def part2():
    red_tiles = read_file()
    pairs = calc_pairs(red_tiles)
    pairs_sorted = sorted(pairs, key=lambda tup: tup[0], reverse=True)

    tiles = Polygon(red_tiles)

    for pair in tqdm.tqdm(pairs_sorted):
        pt1 = red_tiles[pair[1]]
        pt2 = red_tiles[pair[2]]
        square = Polygon([
            (pt1[0], pt1[1]),
            (pt2[0], pt1[1]),
            (pt2[0], pt2[1]),
            (pt1[0], pt2[1])
        ])
        if tiles.covers(square):
            print(pair)
            return
    print()



if __name__ == "__main__":
    part2()
