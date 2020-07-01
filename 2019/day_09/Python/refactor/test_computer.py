"""
Test ``computer.py``.
To run (from this directory):
  % module load scitools  # or pip or conda install pytest
  % python -m pytest .
Or, if using Cloud9 on AWS:
  % python3 -m pytest .
"""
import pytest

from load_input import get_input
from computer import Computer


@pytest.mark.parametrize(
    'test_program, expected', [
        # Day 2 opcode 1 case 1 (one instruction):
        #
        # 1a. add value (1) at index given by value of index 1 (0)
        # 1b. with value (1) at index given by value of index 2 (0)
        # 1c. and put the result (1 + 1 = 2) at index given by value of index 3
        #     (0)
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        # Day 2 opcode 2 case 1 (one instruction):
        #
        # 1a. multiply value (3) at index given by value of index 1 (3)
        # 1b. with value (2) at index given by value of index 2 (0)
        # 1c. and put the result (3 * 2 = 6) at index given by value of index 3
        #     (3)
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        # Day 2 opcode 2 case 2 (one instruction):
        #
        # 1a. multiply value (99) at index given by value of index 1 (4)
        # 1b. with value (99) at index given by value of index 2 (4)
        # 1c. and put the result (99 * 99 = 9801) at the index given by value
        #     of index 3 (5)
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        # Day 2 opcode 1 & 2 case 2 (two instructions):
        #
        # 1a. add value (1) at index given by value of index 1 (1)
        # 1b. with value (1) at index given by value of index 2 (1)
        # 1c. and put the result (1 + 1 = 2) at index given by value of index 3
        #     (4)
        # 2a. then multiple value (5) at index given by value of index 5 (5)
        # 2b. with value (6) at index given by value of index 6 (6)
        # 2c. and put the result (5 * 6 = 30) at index given by value of index
        #     7 (0)
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        # Day 5 opcode 2 position(C=0)-immediate(B=1)-position(A=0) case 1
        # (one instruction):
        #
        # 1a. multiple value (33) at index given by value of index 1 (4)
        # 1b. with value of index 2 (3)
        # 1c. and put the result (33 * 3 = 99) at index given by value of index
        #     3 (4)
        ([1002, 4, 3, 4, 33],  [1002, 4, 3, 4, 99]),
        # Day 5 opcode 1 immediate(C=1)-immediate(B=1)-position(A=0) case 1
        # (one instruction):
        #
        # 1a. add value of index 1 (100)
        # 1b. with value of index 2 (-1)
        # 1c. and put the result (100 + -1 = 99) at index given by value of
        #     index 3 (4)
        ([1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),
    ]
)
def test_computer(test_program, expected):
    comp = Computer(test_program)
    comp.run()
    assert comp.program == expected


@pytest.mark.parametrize(
    'test_program, test_input, expected', [
        # Day 5 opcode 3 & 4 case 1 (two instructions):
        #
        # 1a. put input (1) at index given by value of index 1 (0)
        # 2a. output value (1) at index given by value of index 3 (0)
        # TODO: where is the "output" stored? Should be asserting output, not
        # program.
        ([3, 0, 4, 0, 99], [1], [1, 0, 4, 0, 99])
    ]
)
def test_computer_with_input(test_program, test_input, expected):
    comp = Computer(test_program, test_input)
    comp.run()
    assert comp.program == expected


def test_get_input_type():
    program = get_input()
    for item in program:
        assert isinstance(item, int)


# @pytest.mark.parametrize(
#     "program, phases, expected",
#     [
#         (
#             [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
#             [9,8,7,6,5],
#             139629729,
#         ),
#         (
#             [
#                 3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
#             ],
#             [9,7,8,5,6],
#             18216,
#         ),
#     ],
# )
# def test_feedback_loop(program, phases, expected):
#     assert part1.run_feedback_loop(program, phases) == expected
