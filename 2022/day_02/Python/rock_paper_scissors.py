# read in the list
# create score matrix
# use a score matrix
import numpy as np

from common import loaders


def read_moves():
    moves = loaders.load_string()
    return moves


def calculate_score(moves):
    # (1 for Rock A X, 2 for Paper B Y, and 3 for Scissors C Z)
    # plus
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).

    #   A, B, C
    # X
    # Y
    # Z

    score_matrix = np.asarray([[4, 8, 3],
                               [1, 5, 9],
                               [7, 2, 6]])

    score = 0
    for move in moves:
        their_move, my_move = move.split(" ")
        score += score_matrix[ord(their_move) - 65][ord(my_move) - 88]

    return score


def calculate_score_part2(moves):
    # (1 for Rock A, 2 for Paper B, and 3 for Scissors C)
    # plus
    # (0 if you lost X, 3 if the round was a draw Y, and 6 if you won Z).

    #   A, B, C
    # X
    # Y
    # Z

    score_matrix = np.asarray([[3, 1, 2], [4, 5, 6], [8, 9, 7]])

    score = 0
    for move in moves:
        their_move, result = move.split(" ")
        score += score_matrix[ord(result) - 88][ord(their_move) - 65]

    return score


if __name__ == "__main__":
    moves = read_moves()
    score = calculate_score(moves)
    score2 = calculate_score_part2(moves)

    print(f"score is {score}")
    print(f"score 2 is {score2}")

