from calculate import Submarine
import pytest


SAMPLE_COMMANDS = [
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2",
]



def test_execute_course():
    expected =150
    sub = Submarine()
    sub.execute_course(SAMPLE_COMMANDS)
    assert sub.depth * sub.horizontal_position == expected

@pytest.mark.parametrize(
    ("command","depth","horizontal_position","expected_depth", "expected_horizontal_position"),
    [(SAMPLE_COMMANDS[0], 0, 0, 0, 5),
     (SAMPLE_COMMANDS[1], 0, 5, 5, 5)]
    )

def test_move(command, depth, horizontal_position, expected_depth, expected_horizontal_position):
    sub = Submarine(depth, horizontal_position)
    sub.move(command)
    assert sub.depth == expected_depth
    assert sub.horizontal_position == expected_horizontal_position