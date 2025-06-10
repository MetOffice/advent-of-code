from trailhead import trailhead_scores


def test_trailhead():
    assert trailhead_scores("input-test.txt") == 36
