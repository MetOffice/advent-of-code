import pytest

from polymers import apply_rules


@pytest.mark.parametrize(["start", "expected"], [("NNCB", "NCNBCHB"),
                                               ("NCNBCHB", "NBCCNBBBCBHCB"),
                                               ("NBCCNBBBCBHCB",
                                                "NBBBCNCCNBBNBNBBCHBHHBCHB"),
                                               ("NBBBCNCCNBBNBNBBCHBHHBCHB",
                                                "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")])
def test_apply_rules(start, expected):
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

    result = apply_rules(start, rules)

    assert result == expected
