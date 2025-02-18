import itertools

import numpy


def load_file():
    with open("../input", "r") as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


def create_possible_xmas_pt1():
    horizontal = numpy.array(list("XMAS"))[numpy.newaxis]
    vertical = numpy.transpose(horizontal)
    diag = numpy.diag(numpy.array(list("XMAS")))

    return [
        horizontal,
        numpy.flip(horizontal),
        vertical,
        numpy.flip(vertical),
        diag,
        numpy.flipud(diag),
        numpy.fliplr(diag),
        numpy.flip(diag)
    ]


def create_possible_xmas_pt2():
    start1 = numpy.array([list("M S"),
                          list(" A "),
                          list("M S")])
    start2 = numpy.array([list("M M"),
                          list(" A "),
                          list("S S")])
    start3 = numpy.array([list("S S"),
                          list(" A "),
                          list("M M")])
    start4 = numpy.array([list("S M"),
                          list(" A "),
                          list("S M")])
    return [
        start1,
        start2,
        start3,
        start4
    ]


def count_occurences(array, xmas_array):
    count = 0
    for (y, x) in itertools.product(
            range(array.shape[0] - xmas_array.shape[0] + 1),
            range(array.shape[1] - xmas_array.shape[1] + 1)
    ):
        sub_array = array[y:y + xmas_array.shape[0], x:x + xmas_array.shape[1]]
        if arrays_match(sub_array, xmas_array):
            count += 1
    return count


def arrays_match(sub_array, xmas_array):
    for (y, x) in itertools.product(
            range(sub_array.shape[0]),
            range(sub_array.shape[1])
    ):
        if xmas_array[y,x] != " " and sub_array[y,x] != xmas_array[y,x]:
            return False
    return True



def main():
    xmases = create_possible_xmas_pt2()
    array = numpy.array(load_file())
    result = sum(count_occurences(array,xmas) for xmas in xmases)
    print(result)


if __name__ == "__main__":
    main()
