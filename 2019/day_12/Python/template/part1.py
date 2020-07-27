from load_input import get_input


def main():
    # temporary input (make parsing function later)
    moons = [Moon({'x': 6, 'y': -2, 'z': -7}),
             Moon({'x': -6, 'y': -7, 'z': -4}),
             Moon({'x': -9, 'y': 11, 'z': 0}),
             Moon({'x': -3, 'y': -4, 'z': 6})]

    number_of_timesteps = 1000
    for _ in range(number_of_timesteps):
        for moon in moons:
            # we can use all moons here, as the effect of a moon's
            # gravity on itself is happily zero
            moon.apply_gravity(moons)

        for moon in moons:
            moon.apply_velocity()

    return calculate_energy(moons)


class Moon:
    def __init__(self, position):
        """
        Input parameters:
          position: dict of the form {'x': int, 'y': int, 'z': int}
        """
        self.position = position
        self.velocity = {'x': 0, 'y': 0, 'z': 0}

    def apply_velocity(self):
        """
        Updates the position of this moon using its velocity
        """

        for axis in self.position:
            self.position[axis] += self.velocity[axis]

    def apply_gravity(self, moons):
        """
        Updates the velocity of this moon based on the position
        of other moons in moons.
        Input parameters:
          moons: list of Moon objects
        """
        for moon in moons:
            for axis in self.position:
                if self.position[axis] > moon.position[axis]:
                    self.velocity[axis] -= 1
                elif self.position[axis] < moon.position[axis]:
                    self.velocity[axis] += 1

def calculate_energy(moons):
    """
    Calculate the energy of a given configuration of moons.
    Input parameters:
      moons: list of Moon objects
    """

    total_energy = 0
    for moon in moons:
        kinetic_energy = 0
        potential_energy = 0
        for axis in moon.position:
            kinetic_energy += abs(moon.velocity[axis])
            potential_energy += abs(moon.position[axis])

        energy = kinetic_energy * potential_energy
        total_energy += energy

    return total_energy


def parse_or_something(input_list):
    """
    Function to get input from the file and make it a dict...
    ...but we didn't get round to it
    """
    pass



if __name__ == "__main__":
    print(main())
