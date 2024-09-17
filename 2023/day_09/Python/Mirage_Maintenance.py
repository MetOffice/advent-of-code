def read_file(file: str) -> list[list[int]]:
    with open(file, 'r') as f:
        return [[int(i) for i in line.split(" ")] for line in f]


def extrapolate_right(single_input: list[int]) -> int:
    differences = list(map(lambda a, b: a - b, single_input[1:], single_input[:-1]))
    difference = differences[0] if len(set(differences)) == 1 else extrapolate_right(differences)
    return single_input[-1] + difference


def extrapolate_left(single_input: list[int]) -> int:
    differences = list(map(lambda a, b: a - b, single_input[1:], single_input[:-1]))
    difference = differences[0] if len(set(differences)) == 1 else extrapolate_left(differences)
    return single_input[0] - difference


def run():
    data = read_file("../input")
    results_pt1 = [extrapolate_right(single_input) for single_input in data]
    print("Part 1: "+str(sum(results_pt1)))
    results_pt2 = [extrapolate_left(single_input) for single_input in data]
    print("Part 2: "+str(sum(results_pt2)))


if __name__ == "__main__":
    run()
