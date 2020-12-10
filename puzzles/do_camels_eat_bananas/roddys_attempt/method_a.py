#!/usr/bin/env python

from common_functions import bananas_transported, calc_bananas_transported

def calc_furthest_limit(bananas_to_shift, camels_carry_limit,
                        distance_left_to_travel, return_trip=True):
    '''Theoretically, How far can a camel go at 1 banana/km...
    Assuming that if there are more bananas than the camel can carry, it needs
    to make a return trip and can olny go half as far as the number of bananas
    it can carry. If no return trip, range is limited by the number of banans.'''
    limit_by_banana = min(bananas_to_shift, camels_carry_limit)
    # Check if a return trip needs to be made.
    # I appreciate this is /wrong/ in the case of abandoning bananas not worth
    # returning for - but that should be handled elsewhere.
    if (bananas_to_shift > camels_carry_limit):
        limit_by_banana = limit_by_banana // 2
    furthest_possible = min(distance_left_to_travel, limit_by_banana)
    return furthest_possible
    
def calc_next_stop(bananas_to_shift, camels_carry_limit,
                          distance_left_to_travel):
    '''The cost function : asumes that the highest score of number of bananas
    transported * distance travelled is the optimum distance to go before making
    a 'banana store'
    This turns out to be the wrong approach.
    2nd attempt was to try and find the minimum cost in terms of bananas eaten
    per km travelled - it failed also.'''
    max_banana_miles = 0
    best_distance = -100
    best_bananas_transported = -100
    min_banana_cost = bananas_to_shift
    best_distance_2 = -100
    best_bananas_transported_2 = -100
    furthest_limit = calc_furthest_limit(bananas_to_shift,
                                         camels_carry_limit,
                                         distance_left_to_travel)
    for propsed_distance in range(1,furthest_limit + 1):
        bananas_transported = calc_bananas_transported(bananas_to_shift,
                              propsed_distance, camels_carry_limit)
        banana_miles =  bananas_transported * propsed_distance
        if banana_miles > max_banana_miles:
            max_banana_miles = banana_miles
            best_distance = propsed_distance
            best_bananas_transported = bananas_transported
            #print("New high score of {0} moving {1:5d} {2:5d} kilometers".format(
            #      max_banana_miles, bananas_transported, propsed_distance))
        #elif banana_miles == max_banana_miles:
        #    print("Curious_point = got a double identical score of "
        #          "{0:5d} at {1:5d} and {2:5d}".format(max_banana_miles,
        #           best_distance, propsed_distance))
# Second attempt at cost function - even worse than the the first....
# Then I realised why - you need the cost of the next leg, not the current one
# to decide where to place the banana store.... I'd be very curious if there was
# a cost function which would iterate from 1 to n km and calculate a
# trasportation cost that gave the cutoff for the first leg at the same place as
# one which works out when the cost of the next leg changes and then calculates
# how far you can go until that happens...
#        milage_cost = (bananas_to_shift - bananas_transported) / propsed_distance
#        bananana_cost = bananas_transported / milage_cost
#        if bananana_cost < min_banana_cost:
#            min_banana_cost = bananana_cost
#            best_distance = propsed_distance
#            best_bananas_transported = bananas_transported
#            #print("New best cost of {0} moving {1:5d} {2:5d} kilometers".format(
#            #      min_banana_cost, bananas_transported, propsed_distance))
#        #elif milage_cost == min_banana_cost:
#        #    print("Curious_point = got a double identical cost of "
#        #          "{0} at {1:5d} and {2:5d}".format(min_banana_cost,
#        #           best_distance, propsed_distance))
    return best_distance, best_bananas_transported

    
def calc_max_bananas_transported(initial_banana_count, camels_carry_limit,
                                 distance_to_transport):
    '''Given a total distance to cover, and an intial number of bananas along
    with a load limit for the camel - calculates the maximum number of bananas
    that can be delivered to the destination.'''
    distance_left_to_go = distance_to_transport
    bananas_left = initial_banana_count
    while distance_left_to_go > 0:
        (best_leg, bananas_left) = calc_next_stop(bananas_left,
                                   camels_carry_limit, distance_left_to_go)
        distance_left_to_go = distance_left_to_go - best_leg
        print(f"Have travelled {best_leg},  got {bananas_left} bananas left "
               f"and {distance_left_to_go} kilometers to go")
    return bananas_left
