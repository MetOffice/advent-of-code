FILENAME = '../../input.txt'


def read_input(filename):
    with open(filename, 'r') as file_handle:
        lines = file_handle.readlines()
    return lines


def main():
    lines = read_input(FILENAME)
    fuel_total = 0
    for line in lines:
        fuel_total += calculate_fuel(int(line))
    return fuel_total


def main2():
    lines = read_input(FILENAME)
    return sum([calculate_fuel(int(line)) for line in lines])


def calculate_fuel(mass):
    """
    Return fuel given mass.

    Note: works only for masses > 9.
    """
    if mass <= 8:
        raise RuntimeError('Cannot calculate fuel for mass <= 8')
    return (mass // 3) - 2


if __name__ == '__main__':
    print(main())
    print(main2())
    
