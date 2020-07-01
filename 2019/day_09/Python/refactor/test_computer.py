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
    'test_input, expected', [
        # opcode 1 case 1
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        # opcode 2 case 1
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        # opcode 2 case 2
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        # opcode 1 case 2
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ]
)
def test_day_2(test_input, expected):
    comp = Computer(test_input)
    comp.run()
    output = comp.program
    assert output == expected


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
