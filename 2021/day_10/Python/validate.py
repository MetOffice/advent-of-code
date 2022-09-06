from typing import List, Optional

BRACKETS = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}


def is_corrupted(line: str) -> Optional[str]:
    """
    If corrupted, return first illegal character.
    Else return None.
    """
    stack = []
    for char in line:
        if char in BRACKETS:
            stack.append(BRACKETS[char])
        else:
            try:
                expected = stack.pop()
                if char != expected:
                    # print(f"Expected {expected}, found {char}")
                    return char
            except:
                # print(f"Found {char} with nothing to close")
                return char
    return None


def fix_line(line: str) -> str:
    """
    Take a complete or incomplete line (not corrupted), return the string to
    complete it.
    """
    stack = []
    for char in line:
        if char in BRACKETS:
            stack.append(BRACKETS[char])
        else:
            expected = stack.pop()
            if char != expected:
                raise ValueError(f"Expected {expected}, found {char}")
    return "".join(reversed(stack))


VALIDATION_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def score_corruption(lines: List[str]) -> int:
    score_line = lambda line: VALIDATION_SCORES.get(is_corrupted(line), 0)
    return sum(map(score_line, lines))


CORRECTION_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def score_correction(lines: List[str]) -> int:
    scores = []
    for line in lines:
        if is_corrupted(line):
            continue
        correction = fix_line(line)
        if correction:
            line_score = 0
            for char in correction:
                line_score *= 5
                line_score += CORRECTION_SCORES[char]
            scores.append(line_score)
    i = len(scores) // 2
    return sorted(scores)[i]


if __name__ == "__main__":
    with open("day_10/input.txt") as f:
        lines = f.read().splitlines()
    result_1 = score_corruption(lines)
    print(f"Day 10 part 1: {result_1}")
    result_2 = score_correction(lines)
    print(f"Day 10 part 2: {result_2}")
