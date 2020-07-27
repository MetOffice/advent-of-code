from part1 import Moon, calculate_energy

def test_apply_velocity():
    moon1 = Moon({'x': -1, 'y': 0, 'z': 2})
    moon2 = Moon({'x': 2, 'y': -10, 'z': -7})
    moon3 = Moon({'x': 4, 'y': -8, 'z': 8})
    moon4 = Moon({'x': 3, 'y': 5, 'z': -1})

    moon1.apply_gravity([moon2, moon3, moon4])
    moon1.apply_velocity()
    assert moon1.position == {'x': 2, 'y': -1, 'z': 1}


def test_apply_gravity():
    moon1 = Moon({'x': -1, 'y': 0, 'z': 2})
    moon2 = Moon({'x': 2, 'y': -10, 'z': -7})
    moon3 = Moon({'x': 4, 'y': -8, 'z': 8})
    moon4 = Moon({'x': 3, 'y': 5, 'z': -1})

    moon1.apply_gravity([moon2, moon3, moon4])
    moon2.apply_gravity([moon1, moon3, moon4])
    moon3.apply_gravity([moon1, moon2, moon4])
    moon4.apply_gravity([moon1, moon2, moon3])
    assert moon1.velocity == {'x': 3, 'y': -1, 'z': -1}
    assert moon2.velocity == {'x': 1, 'y': 3, 'z': 3}
    assert moon3.velocity == {'x': -3, 'y': 1, 'z': -3}
    assert moon4.velocity == {'x': -1, 'y': -3, 'z': 1}


def test_calculate_energy():
    moon1 = Moon({'x': 2, 'y': 1, 'z': -3})
    moon2 = Moon({'x': 1, 'y': -8, 'z': 0})
    moon3 = Moon({'x': 3, 'y': -6, 'z': 1})
    moon4 = Moon({'x': 2, 'y': 0, 'z': 4})

    moons = [moon1, moon2, moon3, moon4]

    moon1.velocity = {'x': -3, 'y': -2, 'z' : 1}
    moon2.velocity = {'x': -1, 'y': 1, 'z': 3}
    moon3.velocity = {'x': 3, 'y': 2, 'z': -3}
    moon4.velocity = {'x': 1, 'y': -1, 'z': -1}

    assert calculate_energy(moons) == 179

    