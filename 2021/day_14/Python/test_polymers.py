import pytest

from polymers import apply_rules, apply_rules_better

rules = {"CH": "B",
         "HH": "N",
         "CB": "H",
         "NH": "C",
         "HB": "C",
         "HC": "B",
         "HN": "C",
         "NN": "C",
         "BH": "H",
         "NC": "B",
         "NB": "B",
         "BN": "B",
         "BB": "N",
         "BC": "B",
         "CC": "N",
         "CN": "C"}

@pytest.mark.parametrize(["start", "expected"], [("NNCB", "NCNBCHB"),
                                               ("NCNBCHB", "NBCCNBBBCBHCB"),
                                               ("NBCCNBBBCBHCB",
                                                "NBBBCNCCNBBNBNBBCHBHHBCHB"),
                                               ("NBBBCNCCNBBNBNBBCHBHHBCHB",
                                                "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")])
def test_apply_rules(start, expected):
    result = apply_rules(start, rules)

    assert result == expected


@pytest.mark.parametrize(["start", "expected"],
                         [("NNCB", {"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1}),
                          ("CH", {"CB": 1, "BH": 1})])
def test_apply_rules_better(start, expected):
    result = apply_rules_better(start, rules, 1)
    assert expected == result




