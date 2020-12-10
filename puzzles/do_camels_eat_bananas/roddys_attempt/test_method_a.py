import pytest
from method_a import calc_furthest_limit, calc_next_stop, calc_max_bananas_transported

GLOBAL_BANANA_COUNT = 3000
MAX_BANANA_CARRY = 1200
TOTAL_DISTANCE_TO_TRAVEL = 1000

TEST_LEG_DISTANCE = 200

def test_calc_furthest_limit_sub_full_load():
    '''If the number of bananas you've got is less than a full load, you don't
    need to come back for a second load and the furtest you could go is 1km for
    every banana you have.'''
    bananas_to_shift = max(MAX_BANANA_CARRY-100, 1)
    max_theoretical_distance = bananas_to_shift
    furthest_limit = calc_furthest_limit(bananas_to_shift, MAX_BANANA_CARRY,
                                         max_theoretical_distance)
    assert furthest_limit == max_theoretical_distance

def test_calc_furthest_limit_exceed_full_load():
    '''If the number of bananas you have is greater than a full load, you need
    to come back for the others and the furthest you can go is 1k for every 2
    babnanas you can carry.
    : I realise this is actually wrong - there is a case where it is more
    efficient to abandon some bananas and not come back. Initially the 'cost
    function' was supposed to highlight that distance and this was just the
    furthest theoretical - it's still wrong because that approach is flawed :
    Discuss.....'''
    bananas_to_shift = MAX_BANANA_CARRY+100
    furthest_limit = calc_furthest_limit(bananas_to_shift, MAX_BANANA_CARRY,
                                         TOTAL_DISTANCE_TO_TRAVEL)
    assert furthest_limit == MAX_BANANA_CARRY // 2

def test_calc_furthest_limit_last_leg():
    '''If you've got more bananas than the distance to the final goal, but less
    than a full load so no return trip will be required, the furthest you need
    to go is the remaining distance.'''
    bananas_to_shift = max(MAX_BANANA_CARRY-1, 1)
    distance_remaining = max(bananas_to_shift-1 , 1)
    furthest_limit = calc_furthest_limit(bananas_to_shift, MAX_BANANA_CARRY,
                                         distance_remaining)
    assert furthest_limit == distance_remaining

def test_calc_next_stop_first_leg():
    '''This is where writing tests post writing code is interesting:
    A : I didn't know before writing the code what the answer to this function
    would be - so how do I write a test?.
    B : After writing the code, and ruuning it I spotted that this function will
    give the wrong answer and I'm not sure it can be fixed as the methodology is
    flawed.
    This test just fails if the answer changes from the first time it was run.'''
    distance, bananas_left = calc_next_stop(GLOBAL_BANANA_COUNT,
                                            MAX_BANANA_CARRY,
                                            TOTAL_DISTANCE_TO_TRAVEL)
    assert distance == 300
    assert bananas_left == 1500

def test_calc_next_stop_last_leg():
    '''This is where writing tests post writing code is interesting:
    See previous test for reasons.
    This test just fails if the answer changes from the first time it was run.'''
    last_leg = max(MAX_BANANA_CARRY // 2, 1)
    distance, bananas_left = calc_next_stop(MAX_BANANA_CARRY,
                                            MAX_BANANA_CARRY,
                                            last_leg)
    assert distance == last_leg
    assert bananas_left == MAX_BANANA_CARRY - last_leg

calc_max_bananas_transported
def test_calc_max_bananas_transported():
    '''Another test where I didn't know the answer before running the code.
    So Again, this just tests if the answer has changed from the previous run
    where a human decidied the answer would do.'''
    bananas_left = calc_max_bananas_transported(GLOBAL_BANANA_COUNT,
                                                MAX_BANANA_CARRY,
                                                TOTAL_DISTANCE_TO_TRAVEL)
    assert bananas_left == 500

