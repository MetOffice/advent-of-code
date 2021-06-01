from expenses import sum_to_target
from expenses import find_target


def test_sum_to_target():
    testnumbers = [1721, 979, 366, 299, 675, 1456]

    expected = (299, 1721)

    actual = sum_to_target(testnumbers)
    assert expected == actual


def test_find_target():
    testnumbers = [1721, 979, 366, 299, 675, 1456]

    expected = (366, 675, 979)

    actual = find_target(testnumbers)
    assert expected == actual
