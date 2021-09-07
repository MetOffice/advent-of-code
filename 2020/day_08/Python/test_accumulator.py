import pytest

from accumulator import InfiniteLoopException, run, fix_program


def test_run_infinite_loop():
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
    with pytest.raises(InfiniteLoopException) as exc:
        output = run(program)
    assert exc.value.accumulator == expected


def test_run_terminates():
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
    output = run(program)
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
