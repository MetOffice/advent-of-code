import pytest
from common_functions import bananas_transported, calc_bananas_transported

GLOBAL_BANANA_COUNT = 3000
MAX_BANANA_CARRY = 1000
TOTAL_DISTANCE_TO_TRAVEL = 1000

TEST_LEG_DISTANCE = 200

def test_bananas_transported_return_trip():
    return_trip = True
    no_bananas_transported = bananas_transported(MAX_BANANA_CARRY,
                                                 TEST_LEG_DISTANCE,
                                                 return_trip)
    assert no_bananas_transported == MAX_BANANA_CARRY - ( 2 * TEST_LEG_DISTANCE)

def test_bananas_transported_one_way_trip():
    return_trip = False
    no_bananas_transported = bananas_transported(MAX_BANANA_CARRY,
                                                 TEST_LEG_DISTANCE,
                                                 return_trip)
    assert no_bananas_transported == MAX_BANANA_CARRY - TEST_LEG_DISTANCE

def test_bananas_transported_too_far():
    intial_load = TEST_LEG_DISTANCE // 2
    return_trip = False
    with pytest.raises(ValueError):
        no_bananas_transported = bananas_transported(intial_load,
                                                     TEST_LEG_DISTANCE,
                                                     return_trip)

def test_calc_bananas_transported_3000_200km():
    no_bananas_transported = calc_bananas_transported(GLOBAL_BANANA_COUNT,
                                                      TEST_LEG_DISTANCE,
                                                      MAX_BANANA_CARRY)
    assert no_bananas_transported == 2000

def test_calc_bananas_transported_2600_200km():
    no_bananas_transported = calc_bananas_transported(2600,
                                                      TEST_LEG_DISTANCE,
                                                      MAX_BANANA_CARRY)
    assert no_bananas_transported == 1600

def test_calc_bananas_transported_too_far():
    with pytest.raises(ValueError):
        no_bananas_transported = calc_bananas_transported(2600,
                                                          600,
                                                          MAX_BANANA_CARRY)
