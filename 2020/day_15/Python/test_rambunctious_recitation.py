from rambunctious_recitation import reciter


def test_reciter():
    input = [0,3,6]
    expected = 436
    actual = reciter(input,2020)
    assert expected == actual

