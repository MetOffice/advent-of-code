
from math import floor
from statistics import mean, median

def get_positions():
    with open("./2021/day_07/input.txt", "r") as file:
        input = file.read()
    return [int(pos) for pos in input.split(",")]

def triangle(n):
    return n * (n + 1) // 2

def fuel_use_1(positions, target):
    fuel = [abs(pos - target) for pos in positions]
    return sum(fuel)

def fuel_use_2(positions, target):
    distances = [abs(pos - target) for pos in positions]
    fuel = [triangle(d) for d in distances]
    return sum(fuel)


positions = get_positions()

centre = median(positions)
target = round(centre)

fuel = fuel_use_1(positions, target)

print(fuel)

centre = mean(positions)
target = floor(centre)

fuel_low = fuel_use_2(positions, target)
fuel_high = fuel_use_2(positions, target + 1)

print(min(fuel_low, fuel_high))