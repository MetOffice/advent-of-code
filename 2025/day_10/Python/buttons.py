import itertools
from functools import reduce
from typing import NamedTuple, Self

import numpy as np
from scipy.optimize import milp, LinearConstraint

from tqdm import tqdm

# from sympy.matrices.normalforms import smith_normal_decomp
# from sympy import Matrix, ZZ


def parse_button(b) -> set[int]:
    return {int(i) for i in b[1:-1].split(",")}


def parse_button_bits(b, ind_len):
    t = parse_button(b)
    bit_array = [0] * ind_len
    for i in t:
        bit_array[i] = 1
    return bit_array


class Machine(NamedTuple):
    @classmethod
    def from_line(cls, item) -> Self:
        indicators, *buttons, joltage = item.strip().split(" ")
        ind = {i for i, c in enumerate(indicators[1:-1]) if c == "#"}
        butt = [parse_button(b) for b in buttons]
        butt_mask = [
            parse_button_bits(b, len(indicators) - 2) for b in buttons
        ]
        jolt = [int(i) for i in joltage[1:-1].split(",")]
        return cls(ind, butt, jolt, butt_mask)

    def solve(self):
        for i in range(len(self.buttons)):
            for c in itertools.combinations(self.buttons, i):
                if self.check_combination(c):
                    return i

    def check_combination(self, combination: tuple[set[int]]) -> bool:
        reduced = reduce(set.symmetric_difference, combination, set())
        if reduced == self.indicators:
            return True
        return False

    # Currently works for test input but takes too long / is wrong for full input
    # Interestingly we consistently get numbers like 13000000123124 implying maybe
    # couple results are super broken but the rest okay?
    def solve_pt2(self):
        butt_matrix = np.array(self.butt_mask)
        # button_matrix = np.linalg.pinv(np.array(self.butt_mask).T)
        A = butt_matrix.T
        return int(
            milp(
                np.ones(A.shape[1]),
                integrality=1,
                constraints=LinearConstraint(
                    A, lb=self.joltage, ub=self.joltage
                ),
            ).fun
        )
        # print("A", Matrix(A))
        # joltage_matrix = np.array(self.joltage)
        # C = joltage_matrix
        # B, U, V = smith_normal_decomp(Matrix(A), domain=ZZ)
        # for i in range(np.min(B.shape)):
        #     if B[i, i] == 0:
        #         k = i
        #         break
        # else:
        #     k = np.min(B.shape)
        # # print(B, U, V)
        # # print("U, C", U, C)
        # D = U @ C
        # # print("D", D)
        # H = np.zeros(A.shape[1], dtype=np.int64)
        # min_presses = 1000000000
        # min_presses_X = np.zeros(V.shape[0])
        # min_presses_H = np.zeros(A.shape[1])
        # for i in range(k):
        #     H[i] = D[i] / B[i, i]
        # X = V @ H
        # print("X", X)
        # for i in range(k, len(H)):
        #     H_ = np.zeros(A.shape[1], dtype=np.int64)
        #     H_[i] = 1
        #     print(f"V @ H_{i}", V @ H_)
        # raise NotImplementedError
        # print("X, np.sum(X)", X, np.sum(X))
        # print("A @ X", A @ X)
        # print(min_presses)
        # print("V", V)
        # print("H", min_presses_H, min_presses_H[k:])
        # print("X", min_presses_X)
        # print("min_presses", min_presses)
        # max_joltage = np.max(joltage_matrix)
        # num_presses = max_joltage
        # while True:
        #     print("Searching ", num_presses, " press combinations")
        #     for presses in itertools.combinations_with_replacement(
        #         butt_matrix, num_presses
        #     ):
        #         if np.array_equal(np.sum(presses, axis=0), joltage_matrix):
        #             print(num_presses)
        #             return num_presses

        #     num_presses += 1
        #     if num_presses > max_joltage + 10:
        #         raise Exception("probably broken")
        # result = button_matrix @ joltage_matrix
        # print(result)
        # print("HELP")
        # return min_presses

    indicators: set[int]
    buttons: list[set[int]]
    joltage: list[int]
    butt_mask: list[list[int]]


def read_file():
    with open("../input.txt", "r") as file:
        lines = file.readlines()
        return [Machine.from_line(item) for item in lines]


def main():
    machines: list[Machine] = read_file()
    result = []
    for m in tqdm(machines):
        result.append(m.solve_pt2())
    print(sum(result))


if __name__ == "__main__":
    main()
