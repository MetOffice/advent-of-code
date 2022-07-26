import numpy as np

from common.loaders import load_string


def simulate_states(initial_state, number_of_days):
    fishes = initial_state
    internal_timers = [0] * 9
    for index, internal_timer in enumerate(internal_timers):
        internal_timers[index] = fishes.count(index)
        
    for _ in range(number_of_days):
        fish_to_spawn = internal_timers.pop(0)
        internal_timers[6] += fish_to_spawn
        internal_timers.append(fish_to_spawn)
    
    return internal_timers


def calculate_total_fish(initial_state, number_of_days):
    states = simulate_states(initial_state, number_of_days)
    number_of_fish = sum(states)
    return number_of_fish
    

if __name__ == "__main__":
    initial_state = [int(value) for value in load_string()[0].split(",")]
    number_of_days = 256
    number_of_fish = calculate_total_fish(initial_state, number_of_days)
    print(f"Part 2: there are {number_of_fish} after {number_of_days} days")
    
