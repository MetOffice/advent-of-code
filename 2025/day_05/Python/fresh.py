import tqdm


def load_input(file_path) :
    with open(file_path, 'r') as file:
        file = file.read()
    ranges, veg = file.split("\n\n")
    ranges = ranges.split("\n")
    veg = veg.split("\n")

    ranges = [list(map(int, r.split("-"))) for r in ranges]
    veg = [int(v) for v in veg]
    return ranges, veg


def main():
    ranges, veg = load_input('../input.txt')
    result = 0
    for v in tqdm.tqdm(veg):
        for r in ranges:
            if r[0] <= v <= r[1]:
                # print(f"{v} is in range {r}")
                result += 1
                break
    print(result)

if __name__ == "__main__":
    main()