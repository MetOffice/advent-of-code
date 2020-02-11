import pytest

from day1 import calculate_fuel_1, calculate_fuel_r


@pytest.mark.parametrize(
    'mass,fuel',
    [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ],
)
def test_calculate_fuel_1(mass, fuel):
    assert calculate_fuel_1(mass) == fuel


@pytest.mark.parametrize(
    'mass,fuel',
    [
        (12, 2),
        (14, 2),
        (1969, 966),
        (100756, 50346),
    ],
)
def test_calculate_fuel_r(mass, fuel):
    assert calculate_fuel_r(mass) == fuel
