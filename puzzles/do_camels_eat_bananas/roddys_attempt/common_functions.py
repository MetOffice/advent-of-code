#!/usr/bin/env python

def bananas_transported(initial_banana_load, distance, make_return_trip=True):
    '''Calculated the number of bananas transprted onwards allowing for both
    single and return trip costs'''
    bananas_transported = initial_banana_load - distance
    if make_return_trip:
        bananas_transported -= distance
    if bananas_transported < 0 :
        raise ValueError('Distance too far, the camel has died....')
    return bananas_transported

def calc_bananas_transported(initial_banana_count, distance, camels_carry_limit):
    '''Calculates the total number of bananas moved along one leg of the total
    journey'''
    bananas_left = initial_banana_count
    transported_bananas = 0
    # Iterate over return trips to shift bananas while it's worth doing so :
    #  i.e. there are more bananas left than it takes to make a final trip
    #       after a 'full load' has been transported
    while (bananas_left >  camels_carry_limit + distance):
        carried_bananas = min(bananas_left, camels_carry_limit)
        transported_bananas += bananas_transported(carried_bananas, distance,
                                                   True)
        bananas_left -= carried_bananas
    # Make the final one-way trip to next banana_store carrying as many bananas
    # as possible.
    carried_bananas = min(bananas_left, camels_carry_limit)
    transported_bananas += bananas_transported(carried_bananas, distance,
                                               False)
    return transported_bananas

