from common.loaders import load_string
import numpy as np


def calculate_fuel_consumption_pt1(crab_positions, final_position):
    """

    Parameters
    ----------
    crab_positions: np.array of crab starting positions
    final_position: int

    Returns
    -------
    The fuel consumption. int.

    """
    return int(np.sum(np.abs(crab_positions - final_position)))


def calculate_triangle_number(num):
    """
    Calculates the sum of num and integers less than num until 1.
    i.e. calculate_traingle_number(5) = 1 + 2 + 3 + 4 + 5 = 15

    Parameters
    ----------
    num: an integer

    Returns
    -------
    integer

    """

    return (num ** 2 + num)//2


def calculate_fuel_consumption_pt2(crab_positions, final_position):
    """

    Parameters
    ----------
    crab_positions: np.array of crab starting positions
    final_position:  int

    Returns
    -------

    """
    return int(np.sum(calculate_triangle_number(np.abs(crab_positions - final_position))))



if __name__ == "__main__":
    crab_positions = np.loadtxt("../input.txt", delimiter=",", dtype=int)

    # For part one the median gives the optimal position as its the
    # point where there are equal numbers of crabs above and below it.

    final_position1 = int(np.median(crab_positions))
    final_position_high = np.ceil(np.mean(crab_positions))
    final_position_low = np.floor(np.mean(crab_positions))

    fuel_consumption = calculate_fuel_consumption_pt1(crab_positions, final_position1)
    fuel_consumption_high = calculate_fuel_consumption_pt2(crab_positions, final_position_high)
    fuel_consumption_low = calculate_fuel_consumption_pt2(crab_positions, final_position_low)

    print(f"fuel consumption is {fuel_consumption}")
    print(f"fuel consumption part 2 is {min(fuel_consumption_low, fuel_consumption_high)}")




