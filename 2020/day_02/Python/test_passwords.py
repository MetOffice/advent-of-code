import passwords


def test_parse_input():

    contents = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    result = list(passwords.parse_input(contents))
    expect = [(1, 3, "a", "abcde"), (1, 3, "b", "cdefg"), (2, 9, "c", "ccccccccc")]
    assert result == expect
