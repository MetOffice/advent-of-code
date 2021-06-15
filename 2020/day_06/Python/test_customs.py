import pytest
from customs import count_group_answers, get_group_answers

@pytest.mark.parametrize(
    "answers, expected",
    [(["abc"], 3), (["a", "b", "c"], 3), (["ab", "ac"], 3), (["a", "a", "a", "a"], 1), (["b"], 1)]
)
def test_count_group_answers(answers, expected):
    assert count_group_answers(answers) == expected

def test_get_group_answers():
    input_data = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b", ""]
    output = list(get_group_answers(input_data))
    expected = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
    assert output == expected

