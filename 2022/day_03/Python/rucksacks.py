import string

from common.loaders import load_string

def get_common_item(*backpacks) -> str:
    common, *others = backpacks
    common = set(common)
    for other in others:
        common.intersection_update(set(other))
    return common.pop()

def get_priority(s: str) -> int:
    """
    Return 1-26 for a-z, 27-52 for A-Z.
    """
    if s in string.ascii_lowercase:
        return ord(s) - 96
    else:
        return ord(s) - 38

def find_answer(filepath: str = "day_03/input.txt"):
    rucksacks = load_string(filepath)
    acc = 0
    for line in rucksacks:
        length = len(line) // 2
        a, b = line[:length], line[length:]
        common = get_common_item(a, b)
        acc += get_priority(common)
    return acc

def find_answer_2(filepath: str = "day_03/input.txt"):
    rucksacks = iter(load_string(filepath))
    acc = 0
    while True:
        try:
            a, b, c = next(rucksacks), next(rucksacks), next(rucksacks)
        except StopIteration:
            break
        common = get_common_item(a, b, c)
        acc += get_priority(common)
    return acc

if __name__ == "__main__":
    print(f"Day 3 part 1: {find_answer()}")
    print(f"Day 3 part 2: {find_answer_2()}")
