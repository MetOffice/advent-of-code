#!/usr/bin/env python

from common_functions import bananas_transported, calc_bananas_transported

def ceil_div(a, b):
    ''' Ceiling division - rounds up to the next whole integer'''
    return -(-a // b)

def calc_next_stop(bananas_to_shift, camels_carry_limit,
                          distance_left_to_travel):
    ''' Works out distance until the number of bananas remaining is one less
    load than is currently available. Which is where the 'cost' of onward travel
    drops'''
    bananas_avail = bananas_to_eat(bananas_to_shift, camels_carry_limit)
    distance = how_far_on_a_banana(bananas_to_shift, camels_carry_limit,
                                   bananas_avail, distance_left_to_travel)
    return distance

def bananas_to_eat(bananas_to_shift, camels_carry_limit):
    ''' Works out the numbr of bananas that can be consumed before the number of
    loads that can be carried drops.'''
    n_loads_at_next_store = (bananas_to_shift -1) // camels_carry_limit
    return bananas_to_shift - (n_loads_at_next_store * camels_carry_limit)

def how_far_on_a_banana(bananas_to_shift, camels_carry_limit, bananas_avail,
                        distance_left_to_travel):
    '''Given an arbitrary number of bananas to 'consume' and the number of loads
    to shift onwards - calculates the maximum distance that can be travelled'''
    no_of_loads = ceil_div(bananas_to_shift, camels_carry_limit)
    no_of_trips = (no_of_loads * 2) - 1
    distance = min(bananas_avail // no_of_trips, distance_left_to_travel)
    if distance == 0 and bananas_to_shift > camels_carry_limit:
        print("Using emergency banana munch protocol...")
        no_of_trips -= 2
        bananas_avail = camels_carry_limit
        distance = min(bananas_avail // no_of_trips, distance_left_to_travel)
    return distance

def calc_max_bananas_transported(initial_banana_count, camels_carry_limit,
                                 distance_to_transport):
    '''Given a total distance to cover, and an intial number of bananas along
    with a load limit for the camel - calculates the maximum number of bananas
    that can be delivered to the destination.'''
    distance_left_to_go = distance_to_transport
    bananas_left = initial_banana_count
    while distance_left_to_go > 0:
        best_leg = calc_next_stop(bananas_left,
                                    camels_carry_limit, distance_left_to_go)
        bananas_left = calc_bananas_transported(bananas_left, best_leg,
                                                  camels_carry_limit)
        distance_left_to_go = distance_left_to_go - best_leg
        print(f"Have travelled {best_leg},  got {bananas_left} bananas left "
               f"and {distance_left_to_go} kilometers to go")
    return bananas_left
