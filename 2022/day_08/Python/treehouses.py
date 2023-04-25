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

tree_map = np.genfromtxt("../input.txt", dtype=int, delimiter=1)
tree_map = ma.array(tree_map)

mask = mask_hidden(tree_map)

print(tree_map)
masked_trees = mask_hidden(tree_map)
print(masked_trees)
print(masked_trees.count())