from stones import blink, number_of_stones_after_n_blinks


def test_stones():
    stones = ["125", "17"]
    result = sum(number_of_stones_after_n_blinks(stone, 25) for stone in stones)
    assert result == 55312
