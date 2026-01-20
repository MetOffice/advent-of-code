import pytest

import safe
from safe import Instruction


@pytest.mark.parametrize("start, dir, val, expect_pos, expected_zero_count", [
    [50,"R", 50, 0, 1],
    [50,"R", 49, 99, 0],
    [50,"R", 51, 1, 1],

    [50,"L", 50, 0, 1],
    [50,"L", 49, 1, 0],
    [50,"L", 51, 99, 1],

    [50,'L', 68, 82, 1],
    [82,'L', 30, 52, 0],
    [52,'R', 48, 0, 1],
    [0,'L', 5, 95, 0],
    [95,'R', 60, 55, 1],
    [55,'L', 55, 0, 1],

    [50,'R', 200, 50, 2],
    [0,'R', 200, 0, 2],
    [0,'L', 200, 0, 2],
])
def test_thing(start, dir: str, val: int, expect_pos: int, expected_zero_count: int):
    lock = safe.Lock()
    lock.pos = start
    lock.apply(Instruction(dir, val))
    assert lock.pos == expect_pos
    assert lock.zero_count == expected_zero_count
