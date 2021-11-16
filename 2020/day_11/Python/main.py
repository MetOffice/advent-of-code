from common import loaders


def part1(puzzle_input: str):
    pass

def part2(puzzle_input: str):
    pass

def main(input=None):
    if input is None:
        input = loaders.load_string()
    print(f"Part 1 solution: {part1(input)}")
    print(f"Part 2 solution: {part2(input)}")

if __name__ == "__main__":
    main()