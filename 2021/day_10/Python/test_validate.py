import pytest

from validate import is_corrupted, fix_line, score_corruption, score_correction


@pytest.mark.parametrize(
    ("line", "result"),
    [
        ("()", None),
        ("[]", None),
        ("([])", None),
        ("{()()()}", None),
        ("<([{}])>", None),
        ("[<>({}){}[([])<>]]", None),
        ("(((((((((())))))))))", None),
        ("(]", "]"),
        ("{()()()>", ">"),
        ("(((()))}", "}"),
        ("<([]){()}[{}])", ")"),
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
        ("([)]", ")"),
    ],
)
def test_is_corrupted(line, result):
    assert is_corrupted(line) == result


def test_score_corruption():
    lines = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    expected = 26397
    assert score_corruption(lines) == expected


@pytest.mark.parametrize(
    ("line", "correction"),
    [
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
    ],
)
def test_fix_line(line, correction):
    assert fix_line(line) == correction


@pytest.mark.parametrize(
    ("line", "score"),
    [
        (["[({(<(())[]>[[{[]{<()<>>"], 288957),
        (["[(()[<>])]({[<{<<[]>>("], 5566),
        (["(((({<>}<{<{<>}{[]{[]{}"], 1480781),
        (["{<[[]]>}<{[{[{[]{()[[[]"], 995444),
        (["<{([{{}}[<[[[<>{}]]]>[]]"], 294),
        (
            [
                "[({(<(())[]>[[{[]{<()<>>",
                "[(()[<>])]({[<{<<[]>>(",
                "(((({<>}<{<{<>}{[]{[]{}",
                "{<[[]]>}<{[{[{[]{()[[[]",
                "<{([{{}}[<[[[<>{}]]]>[]]",
            ],
            288957,
        ),
    ],
)
def test_score_correction(line, score):
    assert score_correction(line) == score
