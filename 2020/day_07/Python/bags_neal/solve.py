import numpy as np

def solve_parts1_and_2(bag_matrix):
    """
    See pdf for an actual explanation of this...
    """
    shape = np.shape(bag_matrix)
    matrix_sum = np.array(
        np.round(np.linalg.inv(np.identity(shape[0]) - bag_matrix)) 
        - np.identity(shape[0]), dtype=np.int64)

    # number of non-zero entries in first column of M + M^2 + M^3 + ...
    part1_sol = np.sum(np.array(matrix_sum[:,0], dtype=bool))
    # sum of first row of M + M^2 + M^3 + ...
    part2_sol = np.sum(matrix_sum[0])

    return part1_sol, part2_sol