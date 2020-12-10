#!/usr/bin/env python

from method_a import calc_max_bananas_transported as calc_max_bananas_transported_a
from method_b import calc_max_bananas_transported as calc_max_bananas_transported_b

GLOBAL_BANANA_COUNT = 3000
MAX_BANANA_CARRY = 1000
TOTAL_DISTANCE_TO_TRAVEL = 1000

def main():

    print("Calling method A :")
    bananas_left_A = calc_max_bananas_transported_a( GLOBAL_BANANA_COUNT,
                                                     MAX_BANANA_CARRY,
                                                     TOTAL_DISTANCE_TO_TRAVEL)

    print("", "="*30, "\n")
    print("Calling method B :")
    bananas_left_B = calc_max_bananas_transported_b( GLOBAL_BANANA_COUNT,
                                                     MAX_BANANA_CARRY,
                                                     TOTAL_DISTANCE_TO_TRAVEL)
    print("\n", "="*30, "\n")
    print(f"method A reckons I can shift {bananas_left_A}")
    print(f"method B reckons I can shift {bananas_left_B}")
    print("", "="*30, "\n")

if __name__ == '__main__':
    main()
