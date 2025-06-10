from stones import blink


def test_stones():
    stones = ["125", "17"]
    for _ in range(25):
        stones = blink(stones)
    assert len(stones) == 55312
