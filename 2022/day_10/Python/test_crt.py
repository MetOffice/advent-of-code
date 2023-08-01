import textwrap
import pytest

import crt

large_program = textwrap.dedent(
    """
        addx 15
        addx -11
        addx 6
        addx -3
        addx 5
        addx -1
        addx -8
        addx 13
        addx 4
        noop
        addx -1
        addx 5
        addx -1
        addx 5
        addx -1
        addx 5
        addx -1
        addx 5
        addx -1
        addx -35
        addx 1
        addx 24
        addx -19
        addx 1
        addx 16
        addx -11
        noop
        noop
        addx 21
        addx -15
        noop
        noop
        addx -3
        addx 9
        addx 1
        addx -3
        addx 8
        addx 1
        addx 5
        noop
        noop
        noop
        noop
        noop
        addx -36
        noop
        addx 1
        addx 7
        noop
        noop
        noop
        addx 2
        addx 6
        noop
        noop
        noop
        noop
        noop
        addx 1
        noop
        noop
        addx 7
        addx 1
        noop
        addx -13
        addx 13
        addx 7
        noop
        addx 1
        addx -33
        noop
        noop
        noop
        addx 2
        noop
        noop
        noop
        addx 8
        noop
        addx -1
        addx 2
        addx 1
        noop
        addx 17
        addx -9
        addx 1
        addx 1
        addx -3
        addx 11
        noop
        noop
        addx 1
        noop
        addx 1
        noop
        noop
        addx -13
        addx -19
        addx 1
        addx 3
        addx 26
        addx -30
        addx 12
        addx -1
        addx 3
        addx 1
        noop
        noop
        noop
        addx -9
        addx 18
        addx 1
        addx 2
        noop
        noop
        addx 9
        noop
        noop
        noop
        addx -1
        addx 2
        addx -37
        addx 1
        addx 3
        noop
        addx 15
        addx -21
        addx 22
        addx -6
        addx 1
        noop
        addx 2
        addx 1
        noop
        addx -10
        noop
        noop
        addx 20
        addx 1
        addx 2
        addx 2
        addx -6
        addx -11
        noop
        noop
        noop
    """).strip()

@pytest.mark.parametrize("cycle_number,x_value", [(0,  1),
                                                  (1,  1),
                                                  (2,  1),
                                                  (3,  4),
                                                  (4,  4),
                                                  (5, -1)])
def test_small_program(cycle_number, x_value):
    small_program = textwrap.dedent(
    """
        noop
        addx 3
        addx -5
    """).strip()

    result = crt.x_at_cycle(small_program, cycle_number)
    assert result == (cycle_number, x_value)

@pytest.mark.parametrize("cycle_number,x_value", [( 20, 21),
                                                  ( 60, 19),
                                                  (100, 18),
                                                  (140, 21),
                                                  (180, 16),
                                                  (220, 18)])
def test_large_program(cycle_number, x_value):
    result = crt.x_at_cycle(large_program, cycle_number)
    assert result == (cycle_number, x_value)

def test_signal_strength():
    cycles = [20,60,100,140,180,220]
    result = crt.signal_strength(large_program, cycles)
    assert result == 13140
