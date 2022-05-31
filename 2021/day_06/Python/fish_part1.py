import numpy as np

from common.loaders import load_string


def simulate_fish(initial_state, number_of_days):
    fishes = initial_state
    for _ in range(number_of_days):
        # For each day, subtract 1 from the internal timer of each fish:
        fishes = [fish - 1 for fish in fishes]
        
        # Determine whether any fish have a negative internal timer:
        negative_fish = fishes.count(-1)
        
        if negative_fish:
            # The original fish resets its timer to 6:
            fishes = [fish if fish != -1 else 6 for fish in fishes]
            
            # For every original fish that has its timer reset, a new fish
            # is created with an internal timer of 8:
            fishes.extend([8] * negative_fish)

    return fishes


def calculate_total_fish(initial_state, number_of_days):
    fishes = simulate_fish(initial_state, number_of_days)
    number_of_fish = len(fishes)
    return number_of_fish
    
            
if __name__ == "__main__":
    initial_state = [int(value) for value in load_string()[0].split(",")]
    number_of_days = 80
    number_of_fish = calculate_total_fish(initial_state, number_of_days)
    print(f"Part 1: there are {number_of_fish} after {number_of_days} days")
    
