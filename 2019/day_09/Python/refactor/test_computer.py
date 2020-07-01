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
        # 0: Day 2 opcode 1 case 1 (one instruction):
        #
        # 1a. add value (1) at index given by value of index 1 (0)
        # 1b. with value (1) at index given by value of index 2 (0)
        # 1c. and put the result (1 + 1 = 2) at index given by value of index 3
        #     (0)
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        # 1: Day 2 opcode 2 case 1 (one instruction):
        #
        # 1a. multiply value (3) at index given by value of index 1 (3)
        # 1b. with value (2) at index given by value of index 2 (0)
        # 1c. and put the result (3 * 2 = 6) at index given by value of index 3
        #     (3)
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        # 2: Day 2 opcode 2 case 2 (one instruction):
        #
        # 1a. multiply value (99) at index given by value of index 1 (4)
        # 1b. with value (99) at index given by value of index 2 (4)
        # 1c. and put the result (99 * 99 = 9801) at the index given by value
        #     of index 3 (5)
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        # 3: Day 2 opcode 1, 2 case 2 (two instructions):
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
        # 4: Day 5 opcode 2 position(C=0)-immediate(B=1)-position(A=0) case 1
        # (one instruction):
        #
        # 1a. multiple value (33) at index given by value of index 1 (4)
        # 1b. with value of index 2 (3)
        # 1c. and put the result (33 * 3 = 99) at index given by value of index
        #     3 (4)
        ([1002, 4, 3, 4, 33],  [1002, 4, 3, 4, 99]),
        # 5: Day 5 opcode 1 immediate(C=1)-immediate(B=1)-position(A=0) case 1
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
    'test_program, test_input, expected_program, expected_output', [
        # 0: Day 5 opcode 3, 4 case 1 (two instructions):
        #
        # 1a. put input (1) at index given by value of index 1 (0)
        # 2a. output value (1) at index given by value of index 3 (0)
        ([3, 0, 4, 0, 99], [1], [1, 0, 4, 0, 99], 1),
        # 1: Day 5 opcode 3, 8, 4 input > 8 case 1 (three instructions):
        #
        # 1a. put input (9) at index given by value of index 1 (9)
        # 2a. since value of index 3 (9) != value of index 4 (10)
        # 2b. put 0 at index given by value of index 5 (9)
        # 3a. output value (0) at index given by value of index 7 (9)
        ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [9],
         [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8], 0),
        # 2
        ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [9],
         [3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8], 0),
        # 3
        ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [9],
         [3, 3, 1108, 0, 8, 3, 4, 3, 99], 0),
        # 4
        ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [9],
         [3, 3, 1107, 0, 8, 3, 4, 3, 99], 0),
        # 5: Day 5 opcode 3, ... input = 8
        ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8],
         [3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8], 1),
        # 6
        ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8],
         [3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8], 0),
        # 7
        ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [8],
         [3, 3, 1108, 1, 8, 3, 4, 3, 99], 1),
        # 8
        ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [8],
         [3, 3, 1107, 0, 8, 3, 4, 3, 99], 0),
        # 9: Day 5 opcode 3, ... input < 8
        ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [7],
         [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8], 0),
        # 10
        ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7],
         [3, 9, 7, 9, 10, 9, 4, 9, 99, 1, 8], 1),
        # 11
        ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [7],
         [3, 3, 1108, 0, 8, 3, 4, 3, 99], 0),
        # 12
        ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [7],
         [3, 3, 1107, 1, 8, 3, 4, 3, 99], 1),
        # 13: Day 5 opcode 3, ... input = 0 output = 0
        ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0],
         [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 0, 0, 1, 9], 0),
        # 14: Day 5 opcode 3, ... input = 99 output = 1
        ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [99],
         [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 99, 1, 1, 9], 1),
        # 15: Day 5 opcode 3, ... input < 8 output = 999
        ([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
          1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
          999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
         [7],
         [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
          1106, 0, 36, 98, 0, 7, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
          999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
          999),
        # 16: Day 5 opcode 3, ... input = 8 output = 1000
        ([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
          1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
          999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
         [8],
         [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
          1106, 0, 36, 98, 1000, 8, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
          999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
         1000),
        # 17: Day 5 opcode 3, ... input > 8 output = 1001
        ([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
          1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
          999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
         [9],
         [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
          1106, 0, 36, 98, 1001, 9, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
          999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
         1001),
    ]
)
def test_computer_with_input(test_program, test_input, expected_program,
                             expected_output):
    comp = Computer(test_program, test_input)
    comp.run()
    assert comp.program == expected_program
    assert comp.last_output == expected_output


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
