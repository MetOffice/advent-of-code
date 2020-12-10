import pytest
from method_b import ceil_div, calc_next_stop, bananas_to_eat, how_far_on_a_banana, calc_max_bananas_transported

GLOBAL_BANANA_COUNT = 3000
MAX_BANANA_CARRY = 1000
TOTAL_DISTANCE_TO_TRAVEL = 1000

TEST_LEG_DISTANCE = 200

def test_ceil_div_1():
    '''Just a handful of hand cranked examplees of what ceiling dision should
    return'''
    a = 7
    b = 5
    assert ceil_div(a, b)   == 2
    assert ceil_div(b, a)   == 1
    assert ceil_div(a, a)   == 1
    assert ceil_div(2*a, a) == 2
    assert ceil_div(a, 2*a) == 1
    assert ceil_div(0, b)   == 0

def test_bananas_to_eat_more_than_full_load():
    '''Works out how many bananas there are until an integer number of max load
    is attained'''
    bananas = (3 * MAX_BANANA_CARRY) + 50
    assert bananas_to_eat(bananas, MAX_BANANA_CARRY) == 50

def test_bananas_to_eat_less_than_full_load():
    '''If there's less than a full load, you should be able to eat them all.
    is attained'''
    bananas = max(MAX_BANANA_CARRY - 10, 1)
    assert bananas_to_eat(bananas, MAX_BANANA_CARRY) == bananas

def test_how_far_on_a_banana_comfortable_limits():
    '''If there are N times as many bananas as the camel can carry, and further
    to go than 1 single trip, the camel needs to make (2N -1) trips to be one
    stage further on : N-1 return and one single.  To do so, the camel can
    consume 1 whole load's worth of bananas across the trips and thus has
    travelled 1/(2N -1) of a full load'''
    N = 3
    bananas_to_shift = N * MAX_BANANA_CARRY
    bananas_avail = MAX_BANANA_CARRY
    distance_left_to_travel = 2 * MAX_BANANA_CARRY
    how_far = how_far_on_a_banana(bananas_to_shift, MAX_BANANA_CARRY,
                                  bananas_avail, distance_left_to_travel)
    assert how_far == MAX_BANANA_CARRY // (2*N -1)

def test_how_far_on_a_banana_abandoning_bananas():
    '''If there are N(max load) + (2N) bananas available, the ceil division
    would indicate 2N -1 trips and only 2N bananas to make the 2N+1 trips, so
    even travelling 1km would burn more bananas than abandoning the 2N.
    So 2N should be abandoned at the current stop and
    only the transport of N(max load) bananas should be attempted.'''
    N = 3
    bananas_to_shift = (N * MAX_BANANA_CARRY) + (2*N)
    bananas_avail = (2*N)
    distance_left_to_travel = 2 * MAX_BANANA_CARRY
    how_far = how_far_on_a_banana(bananas_to_shift, MAX_BANANA_CARRY,
                                  bananas_avail, distance_left_to_travel)
    assert how_far == MAX_BANANA_CARRY // (2*N -1)

def test_calc_next_stop():
    '''Just strings together 'bananas_to_eat' and 'how_far_on_a_banana' to get
    the distance tot he next stop. Thus returns the same value that 
    'how_far_on_a_banana' would have given after being provided a number of
    banans to eat by 'bananas_to_eat'. '''
    N = 3
    bananas_to_shift = N * MAX_BANANA_CARRY
    bananas_avail = MAX_BANANA_CARRY
    distance_left_to_travel = 2 * MAX_BANANA_CARRY
    distance = calc_next_stop(bananas_to_shift, MAX_BANANA_CARRY,
                              distance_left_to_travel)

def test_calc_max_bananas_transported():
    '''This uses answer provided by the pages setting the problem. So if it
    passes we've calcualated the answer we're supposed to.'''
    # Hardwiring to the numbers from the question
    initial_banana_count = 3000
    camels_carry_limit = 1000
    distance_to_transport = 1000
    bananas = calc_max_bananas_transported(initial_banana_count,
                                           camels_carry_limit,
                                           distance_to_transport)
    assert bananas == 533
