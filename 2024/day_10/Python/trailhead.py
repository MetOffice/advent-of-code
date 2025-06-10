def rating(array: list[list[int]], x: int, y: int) -> int:
    height = array[y][x]

    if height == 9:
        return 1

    n = 0
    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        x_ = x + i
        y_ = y + j
        if x_ < 0 or y_ < 0:
            continue
        try:
            if array[y_][x_] == height + 1:
                n += rating(array, x_, y_)
        except IndexError:
            pass

    return n


def reachable_peaks(array: list[list[int]], x: int, y: int) -> set[tuple[int, int]]:
    height = array[y][x]

    if height == 9:
        return {(x, y)}

    peaks: set[tuple[int, int]] = set()
    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        x_ = x + i
        y_ = y + j
        if x_ < 0 or y_ < 0:
            continue
        try:
            if array[y_][x_] == height + 1:
                peaks.update(reachable_peaks(array, x_, y_))
        except IndexError:
            pass

    return peaks


def file_to_array(path: str) -> list[list[int]]:
    array: list[list[int]] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            array.append(list(map(int, line)))
    return array


def trailhead_scores(path: str) -> int:
    array = file_to_array(path)

    x = len(array[0])
    y = len(array)

    score = 0
    for j in range(y):
        for i in range(x):
            if array[j][i] == 0:
                score += len(reachable_peaks(array, i, j))

    return score


def trailhead_ratings(path: str) -> int:
    array = file_to_array(path)

    x = len(array[0])
    y = len(array)

    score = 0
    for j in range(y):
        for i in range(x):
            if array[j][i] == 0:
                score += rating(array, i, j)

    return score
