import pytest

from accumulator import (
    calculate_accumulator_value_part_1,
    calculate_accumulator_value_part_2,
    fix_program,
)


def test_accumulator_value_part_1():
    program = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    expected = 5
    output = calculate_accumulator_value_part_1(program)
    assert output == expected


def test_accumlator_value_infinite_loop_part_2():
    program = [
        "jmp +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    with pytest.raises(RuntimeError):
        calculate_accumulator_value_part_2(program)


def test_accumlator_value_program_terminates_part_2():
    program = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "nop -4",
        "acc +6",
    ]
    expected = 8
    output = calculate_accumulator_value_part_2(program)
    assert output == expected


def test_fix_program():
    program = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    expected = 8        
    output = fix_program(program)
    assert output == expected
