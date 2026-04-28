import numpy as np


def read_file():
    with open("../input.txt", 'r') as file:
        lines = file.readlines()
    return np.array([[int(a) for a in line.strip().split(",")] for line in lines])

def calc_distance(point1, point2):
    #3d points
    np.linalg.norm(point1 - point2)
    return np.sqrt(np.sum((point1 - point2) ** 2))

def calc_pairs(array):
    result = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            result.append((calc_distance(array[i], array[j]), array[i], array[j]))
    return result

def main():
    lines = read_file()
    pairs = calc_pairs(lines)
    print(lines)

if __name__ == "__main__":
    main()