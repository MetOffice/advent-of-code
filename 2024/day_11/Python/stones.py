def blink(stones: list[str]) -> list[str]:
    new_stones = []
    for stone in stones:
        match stone:
            case "0":
                new_stones.append("1")
            case stone if ((n := len(stone)) % 2) == 0:
                new_stones.extend([stone[: n // 2], str(int(stone[n // 2 :]))])
            case stone:
                new_stones.append(str(int(stone) * 2024))
    return new_stones
