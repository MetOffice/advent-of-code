from functools import cache

def blink(stone: str) -> list[str]:
    match stone:
        case "0":
            return ["1"]
        case stone if ((n := len(stone)) % 2) == 0:
            return [stone[: n // 2], str(int(stone[n // 2 :]))]
        case stone:
            return [str(int(stone) * 2024)]

@cache
def number_of_stones_after_n_blinks(stone: str, blinks: int):
    if blinks == 0:
        return 1
    stones = blink(stone)
    return sum(number_of_stones_after_n_blinks(stone,blinks-1) for stone in stones)