from rainrisk_bilal import rainrisk_part_1, rainrisk_part_2


def test_rainrisk_part_1():
    testinput = ['F10', 'N3', 'F7', 'R90', 'F11']
    expected = 25
    actual = rainrisk_part_1(testinput)
    assert expected == actual

def test_rainrisk_part_2():
    testinput = ['F10', 'N3', 'F7', 'R90', 'F11']
    expected = 286
    actual = rainrisk_part_2(testinput)
    assert expected == actual