import os


INPUT_TXT: str = os.path.join(os.path.dirname(__file__), '../../input.txt')


def calculate_fuel_1(mass: int) -> int:
    """Calculate fuel once."""
    return mass // 3 - 2


def calculate_fuel_r(mass: int) -> int:
    """Calculate fuel recursively."""
    fuel: int = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel_r(fuel)


def main():
    """Print total fuel requirement with data from "input.txt"."""
    print(sum(calculate_fuel_r(int(line)) for line in open(INPUT_TXT)))


if __name__ == '__main__':
    main()
