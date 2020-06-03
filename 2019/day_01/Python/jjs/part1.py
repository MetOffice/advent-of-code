FILENAME = '../../input.txt'


def read_input(filename):
    with open(filename, 'r') as file_handle:
        lines = file_handle.readlines()
    return lines


def initial_calculation():
    lines = read_input(FILENAME)
    fuel_total = 0
    for line in lines:
        fuel_total += calculate_fuel(int(line))
    return fuel_total


def secondary_calculation(initial_fuel):
    fuel_total = initial_fuel
    extra_fuel = calculate_fuel(initial_fuel)
    while extra_fuel > 0:
        fuel_total += extra_fuel
        extra_fuel = calculate_fuel(extra_fuel)
    return fuel_total


def main():
    lines = read_input(FILENAME)
    initial_fuel = initial_calculation()
    return secondary_calculation(initial_fuel)


def main2():
    lines = read_input(FILENAME)
    return sum([calculate_fuel(int(line)) for line in lines])


def calculate_fuel(mass):
    """
    Return fuel given mass.
    """
    fuel = (mass // 3) - 2
    if fuel <= 0:
        fuel = 0
    return fuel


if __name__ == '__main__':
    print(main())
    print(main2())
    
