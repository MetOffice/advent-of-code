from part1 import calc_closest_intersection


def test_case_1():
    wire_a = ["R8","U5","L5","D3"]
    wire_b = ["U7","R6","D4","L4"]
    expected = 6

    assert calc_closest_intersection(wire_a, wire_b) == expected


def test_case_2():
    wire_a = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    wire_b = ["U62","R66","U55","R34","D71","R55","D58","R83"]
    expected = 159

    assert calc_closest_intersection(wire_a, wire_b) == expected


def test_case_3():
    wire_a = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
    wire_b = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
    expected = 135

    assert calc_closest_intersection(wire_a, wire_b) == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    print("All tests passed")