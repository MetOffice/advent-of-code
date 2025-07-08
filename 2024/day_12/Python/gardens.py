import operator
from functools import reduce

import numpy as np
from string import ascii_uppercase
from scipy import ndimage

import scipy.ndimage
from scipy import ndimage


# Load in as an image
# Split into 26 images for each letter in image
# For each:
# Use scipy image label for each to find each feature:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html#scipy.ndimage.label
# Extract each feature
# Count area
# Count perimeter https://stackoverflow.com/a/13444457

def load_file(file: str):
    with open(file, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


def load_image(img: list[list[str]]):
    array = np.array(img)
    return array


def filter_for_letter(arr: np.ndarray, letter):
    return arr == letter


def split_letters(arr: np.ndarray):
    return [filter_for_letter(arr, letter) for letter in ascii_uppercase]


def split_features(arr: np.ndarray, number_of_areas):
    return [filter_for_letter(arr, i + 1) for i in range(number_of_areas)]


def detect_features(arr: np.ndarray):
    features = ndimage.label(arr)
    split_features_list = split_features(features[0], features[1])
    return split_features_list


def calculate_feature_perimeter(arr: np.ndarray):
    arr = np.pad(arr, 1, "constant")
    vert = ndimage.convolve1d(arr.astype(int), np.array([1, -1]), 0, None, "constant", 0)
    horz = ndimage.convolve1d(arr.astype(int), np.array([1, -1]), 1, None, "constant", 0)
    combined = np.absolute(vert) + np.absolute(horz)
    res = combined.sum()
    return res


def calculate_feature_corners(arr: np.ndarray):
    arr = np.pad(arr, 1, "constant")
    corners = ndimage.convolve(arr.astype(int), np.array(
        [
            [1, -1],
            [-1, 1]
        ]
    ))
    return np.absolute(corners).sum()


def calculate_feature_area(arr):
    return arr.sum()


def calculate_feature_pt1(arr):
    return calculate_feature_perimeter(arr) * calculate_feature_area(arr)


def calculate_feature_pt2(arr):
    return calculate_feature_corners(arr) * calculate_feature_area(arr)


def main():
    inp = load_file("../gardens.txt")
    arr = load_image(inp)
    many_arrs = split_letters(arr)

    all_individual_features = reduce(operator.concat, (detect_features(arr) for arr in many_arrs), [])

    features_pt1 = [calculate_feature_pt1(f) for f in all_individual_features]
    features_pt2 = [calculate_feature_pt2(f) for f in all_individual_features]
    print(f"Part 1: {sum(features_pt1)}")
    print(f"Part 2: {sum(features_pt2)}")


if __name__ == "__main__":
    main()
