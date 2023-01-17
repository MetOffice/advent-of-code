# Read the file
# add the calories from each elf
# find the biggest

from common.loaders import load_ints


def read_calories():
    calories = load_ints()

    return calories


def get_elf_calories(calories):
    all_elves = [0]
    for value in calories:
        if value is None:
            all_elves.append(0)
        else:
            all_elves[-1] += value

    return all_elves


if __name__ == "__main__":
    calories = read_calories()
    elf_calories = get_elf_calories(calories)
    elf_calories.sort()

    print(f"max calories = {max(elf_calories)}")
    print(f"top three calories = {sum(elf_calories[-3:])}")