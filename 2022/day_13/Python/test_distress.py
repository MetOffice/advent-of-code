import pytest
from distress import compare, listify, part_1

@pytest.mark.parametrize("left,right,result",
                         
[([1,1,3,1,1], [1,1,5,1,1], -1),
 
([[1],[2,3,4]], [[1],4], -1),

([9], [[8,7,6]], +1),

([[4,4],4,4], [[4,4],4,4,4], -1),

([7,7,7,7], [7,7,7], +1),

([], [3], -1),

([[[]]], [[]], +1),

([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9], +1),

([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,7]]]],8,9], 0)

])
def test_compare(left, right, result):
    test_out = compare(left, right)
    assert result == test_out

@pytest.mark.parametrize("string,result", [("[1,[2,[3,[4,[5,6,7]]]],8,9]", [1,[2,[3,[4,[5,6,7]]]],8,9])])
def test_listify(string, result):
    test_out = listify(string)
    assert test_out == result


def test_part_1():                    
    pairs = [
        ([1,1,3,1,1], [1,1,5,1,1]),
    
        ([[1],[2,3,4]], [[1],4]),

        ([9], [[8,7,6]]),

        ([[4,4],4,4], [[4,4],4,4,4]),

        ([7,7,7,7], [7,7,7]),

        ([], [3]),

        ([[[]]], [[]]),

        ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
    ]

    assert part_1(pairs) == 13
