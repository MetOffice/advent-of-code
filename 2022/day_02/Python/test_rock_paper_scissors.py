import pytest

from rock_paper_scissors import calculate_score, calculate_score_part2


@pytest.mark.parametrize("move, score", [(["A Y"], 8),
                                         (["B X"], 1),
                                         (["C Z"], 6),
                                         (["A Y", "B X", "C Z"], 15)])
def test_calculate_score(move, score):
    result = calculate_score(move)

    assert result == score


@pytest.mark.parametrize("move, score", [(["A Y"], 4),
                                         (["B X"], 1),
                                         (["C Z"], 7),
                                         (["A Y", "B X", "C Z"], 12)])
def test_calculate_score_part2(move, score):
    result = calculate_score_part2(move)

    assert result == score
