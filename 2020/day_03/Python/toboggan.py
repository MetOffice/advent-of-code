from common.loaders import load_string


def count_trees(tree_pattern, right, down):
    x_position = 0
    y_position = 0
    trees_found = 0
    line_length = len(tree_pattern[0])

    tree = "#"

    while y_position < len(tree_pattern):
        # check if tree/not_tree
        if tree_pattern[y_position][x_position] == tree:
            trees_found += 1
        # update current position
        y_position += down
        x_position += right
        # check if at rightmost column and wrap back to start of line
        if x_position >= line_length:
            x_position -= line_length
    return trees_found


def multiply_all_the_trees(tree_pattern):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for right, down in slopes:
        result *= count_trees(tree_pattern, right, down)
    return result


def main():
    tree_pattern = load_string()
    print(f"Part 1 result: {count_trees(tree_pattern, right=3, down=1)}")
    print(f"Part 2 result: {multiply_all_the_trees(tree_pattern)}")


if __name__ == "__main__":
    main()
