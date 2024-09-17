from Mirage_Maintenance import extrapolate_right, extrapolate_left

def test_input_test():
    result = extrapolate_right([0, 3, 6, 9, 12, 15])
    assert result == 18


def test_input_test_2():
    result = extrapolate_right([10, 13, 16, 21, 30, 45])
    assert result == 68


def test_input_extrapolate_left():
    result = extrapolate_left([10, 13, 16, 21, 30, 45])
    assert result == 5
