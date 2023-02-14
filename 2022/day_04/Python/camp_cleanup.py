from common import loaders

# read in input
# format it
def parse_input():
    raw = loaders.load_string()

    sections = [(item.split(",")[0], item.split(",")[1]) for item in raw]
    elf0 = [(int(item[0].split("-")[0]), int(item[0].split("-")[1])) for item in sections]
    elf1 = [(int(item[1].split("-")[0]), int(item[1].split("-")[1])) for item in sections]

    return list(zip(elf0, elf1))


# check if bounds of one contain the other
def check_inside(elf0, elf1):
    return elf1[0] <= elf0[0] <= elf0[1] <= elf1[1]


def check_overlap(elf0, elf1):
    return (elf1[0] <= elf0[0] <= elf1[1]) or (elf1[0] <= elf0[1] <= elf1[1])


def check_all_bounds(assigned_sections):
    count = 0
    for elf0, elf1 in assigned_sections:
        if check_inside(elf0, elf1) or check_inside(elf1, elf0):
            count += 1

    return count


def check_all_overlaps(assigned_sections):
    count = 0
    for elf0, elf1 in assigned_sections:
        if check_overlap(elf0, elf1) or check_overlap(elf1, elf0):
            count += 1
    return count


# count
if __name__ == "__main__":
    elfs = parse_input()
    result = check_all_bounds(elfs)
    print(f"part1 = {result}")
    result2 = check_all_overlaps(elfs)
    print(f"part2 = {result2}")
    print("done")