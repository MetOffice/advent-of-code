#import pytest
#import tickettranslation as tt

def test_read_policy():
    line = "departure location: 26-715 or 727-972"
    out = tt.read_policy(line)
    assert out == ("departure location", 26, 715, 727, 972)
