import tqdm
from ranges import Range, RangeSet


def load_input(file_path):
    with open(file_path, 'r') as file:
        file = file.read()
    ranges, veg = file.split("\n\n")
    ranges = ranges.split("\n")
    veg = veg.split("\n")

    ranges = [list(map(int, r.split("-"))) for r in ranges]
    veg = [int(v) for v in veg]
    return ranges, veg


def part1(ranges, veg):
    result = 0
    for v in tqdm.tqdm(veg):
        for r in ranges:
            if r[0] <= v <= r[1]:
                # print(f"{v} is in range {r}")
                result += 1
                break
    print("Pt1:", result)


def part2(ranges):
    rangeset = RangeSet()
    for r in ranges:
        rangeset.add(Range(r[0], r[1], include_end=True))
    count = 0
    for r2 in rangeset.ranges():
        count += r2.end - r2.start + 1
    print("Pt2:", count)


def main():
    ranges, veg = load_input('../input.txt')
    part1(ranges, veg)
    part2(ranges)


if __name__ == "__main__":
    main()
