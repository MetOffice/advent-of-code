from accumulator import calculate_accumulator_value

def test_accumulator_value():
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
    output = calculate_accumulator_value(program)
    assert output == expected
