import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt


def mask_row(row:np.ndarray, direction):
    """
    Create a mask for a single row indicating trees hidden from the
    specified direction. Direction is 0 (left) or 1 (right).
    """
    # If direction is 1 we reverse the input and output
    if direction:
        row = row[::-1]
    mask = np.zeros_like(row)
    for i in range(1, len(row)):
        mask[i] = row[i] <= np.max(row[:i])
    if direction:
        mask = mask[::-1]
    return mask


def mask_one_direction(trees, direction):
    """
    Create a mask indicating trees hidden from the specified direction.
    Direction
    """
    # direction is integer 0 to 3
    axis = direction % 2
    reversal = direction // 2
    return np.apply_along_axis(lambda row: mask_row(row, reversal), axis, trees)


def mask_hidden(trees):
    """
    Return a masked array of trees where hidden trees are masked.
    """
    mask = np.ones_like(trees)

    # a tree is hidden only if its hidden from all sides
    mask = np.logical_and(mask_one_direction(trees, 0), mask)
    mask = np.logical_and(mask_one_direction(trees, 1), mask)
    mask = np.logical_and(mask_one_direction(trees, 2), mask)
    mask = np.logical_and(mask_one_direction(trees, 3), mask)

    return ma.masked_where(mask, trees)


def look_forward(tree_row):
    # find how many trees we can see from position 0
    our_tree_height = tree_row[0]
    rest_of_trees = tree_row[1:]
    for distance, tree in enumerate(rest_of_trees):
        if tree >= our_tree_height:
            return distance+1
    return len(rest_of_trees)


def make_four_slice_directions(trees, our_coords):
    """
    Takes slices from our position
    Parameters
    ----------
    trees: big array of trees
    our_coords: the coordinate of our tree

    Returns
    -------
    four arrays with this tree in the first position

    """
    up = trees[our_coords[0],our_coords[1]::-1]
    down = trees[our_coords[0],our_coords[1]:]
    left = trees[our_coords[0]::-1,our_coords[1]]
    right = trees[our_coords[0]:,our_coords[1]]

    return [up, down, left, right]

def part_1():
    tree_map = np.genfromtxt("../input.txt", dtype=int, delimiter=1)
    tree_map = ma.array(tree_map)

    mask = mask_hidden(tree_map)

    print(tree_map)
    masked_trees = mask_hidden(tree_map)
    print(masked_trees)
    print(masked_trees.count())

def part_2():
    tree_map = np.genfromtxt("../input.txt", dtype=int, delimiter=1)
    tree_map = ma.array(tree_map)
    biggest_score = 0
    for i in range(1, np.shape(tree_map)[1]-1):
        for j in range(1, np.shape(tree_map)[1]-1):
            four_slices = make_four_slice_directions(tree_map, [i, j])
            score = 1
            for view in four_slices:
                score *= look_forward(view)
            biggest_score = max(score, biggest_score)

    print(biggest_score)


if __name__=="__main__":
    part_2()