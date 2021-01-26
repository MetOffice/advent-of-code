from expenses_part1 import sum_to_2020

def test_sum_to_2020():
    testnumbers=[1721,979,
    366,
    299,
    675,
    1456]

    expected = (299, 1721)

    actual = sum_to_2020(testnumbers)
    assert expected == actual
