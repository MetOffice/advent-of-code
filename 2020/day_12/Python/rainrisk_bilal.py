import numpy as np


def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()


class Ferry:
    """ class to handle ferry position and direction"""



    def __init__(self, coords, dir):
        self.coords = coords
        self.dir = dir
        self.cardinals_to_coords = {
            'N': np.array([0, 1]),
            'W': np.array([-1, 0]),
            'S': np.array([0, -1]),
            'E': np.array([1, 0]),
            90: np.array([0, 1]),
            180: np.array([-1, 0]),
            270: np.array([0, -1]),
            0: np.array([1, 0])
        }

    def update_ferry(self, data):
        action = data[0]
        value = int(data[1:])
        if action == 'L':
            self.dir = (self.dir + value) % 360
        elif action == 'R':
            self.dir = (self.dir - value) % 360
        else:
            if action == 'F':
                moving_dir = self.dir
            else:
                moving_dir = action
            self.coords += value * self.cardinals_to_coords[moving_dir]


class WaypointedFerry:
    """ Class to handle ferry and waypoint positions"""

    def __init__(self, coords, wcoords):
        self.coords = coords
        self.wcoords = wcoords
        self.cardinals_to_coords = {
            'N': np.array([0, 1]),
            'W': np.array([-1, 0]),
            'S': np.array([0, -1]),
            'E': np.array([1, 0])
        }

    def update_ferry(self, data):
        action = data[0]
        value = int(data[1:])
        if action == 'L' or action == 'R':
            if action == 'R':
                value = (360 - value) % 360  # turn into acw rotation
            if value == 90:
                self.wcoords = np.array([-self.wcoords[1], self.wcoords[0]])
            elif value == 180:
                self.wcoords = np.array([-self.wcoords[0], -self.wcoords[1]])
            elif value == 270:
                self.wcoords = np.array([self.wcoords[1], -self.wcoords[0]])
        elif action == 'F':
            self.coords += value * self.wcoords
        else:
            self.wcoords += value * self.cardinals_to_coords[action]


def rainrisk_part_1(sequence):
    ferry = Ferry(np.array([0, 0]), 0)

    for instruction in sequence:
        ferry.update_ferry(instruction)

    distance = abs(ferry.coords[0]) + abs(ferry.coords[1])
    return distance


def rainrisk_part_2(sequence):
    ferry = WaypointedFerry(np.array([0, 0]), np.array([10, 1]))

    for instruction in sequence:
        ferry.update_ferry(instruction)

    distance = abs(ferry.coords[0]) + abs(ferry.coords[1])
    return(distance)


def main():
    sequence = read_input("../input.txt")
    rainrisk_part_1(sequence)
    rainrisk_part_2(sequence)


if __name__ == "__main__":
    main()
