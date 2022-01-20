from crabcombat import *

def test_loopbreak():
    victor, score = resolve_recursive_combat(Deck([43,19]), Deck([2,29,14]))
    assert victor

def test_recursive():
    victor, score = resolve_recursive_combat(
        Deck([9,2,6,3,1]),
        Deck([5,8,4,7,10])
    )
    assert not victor, "Incorrect victor"
    assert score == 291, f"Score was {score} but should be 291."

test_recursive()