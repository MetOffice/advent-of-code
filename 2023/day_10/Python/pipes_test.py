from pipes import next_move, Coordinate, Direction

def test_next_move():
    result = next_move([
        ['.','.','.'],
        ['L','S','J'],
        ['.','.','.'],
    ], Coordinate(1, 2, 0), Direction.EAST)
    assert result == Direction.NORTH
