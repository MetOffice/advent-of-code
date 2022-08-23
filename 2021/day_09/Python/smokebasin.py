import numpy as np

def load_input(input_file="../input.txt"):
    """
    Read file as a grid of numbers with column width 1 (individual digits)
    and return as np array
    """
    # column width delimiter is only available in genfromtxt(), not in loadtxt()
    return np.genfromtxt(input_file, dtype=int, delimiter=1)

def find_low_points(input):
    low_points = np.ones(input.shape, dtype=bool)

    low_points[1:,:] &= input[1:,:] < input[:-1,:]
    low_points[:-1,:] &= input[:-1,:] < input[1:,:]
    low_points[:,1:] &= input[:,1:] < input[:,:-1]
    low_points[:,:-1] &= input[:,:-1] < input[:,1:]

    return low_points

def compute_risk(input, low_points):
    return np.sum(input[low_points]) + np.sum(low_points)


def flood_fill(coords:tuple, fill:int, input:np.ndarray, canvas:np.ndarray):
    h, w = input.shape
    conditions = (
        0 <= coords[0] < h
        and 0 <= coords[1] < w
        and input[coords] < 9
        and canvas[coords] == 0
    )

    if not conditions:
        return

    canvas[coords] = fill
    flood_fill((coords[0]+1,coords[1]), fill, input, canvas)
    flood_fill((coords[0]-1,coords[1]), fill, input, canvas)
    flood_fill((coords[0],coords[1]+1), fill, input, canvas)
    flood_fill((coords[0],coords[1]-1), fill, input, canvas)

def find_low_coords(low_points):
    low_coords = np.nonzero(low_points)
    return np.array(low_coords).T

def find_basins(input, low_coords):
    basin_map = np.zeros(input.shape, dtype=int)

    for colour, coords in enumerate(low_coords):
        flood_fill(tuple(coords), colour + 1, input, basin_map)

    return basin_map

def calc_basin_risk(basin_map):
    _, counts = np.unique(basin_map, return_counts=True)
    return np.product(np.sort(counts)[-4:-1])

# Question Parts

def part1(input):
    low_points = find_low_points(input)

    return compute_risk(input, low_points)

def part2(input):
    low_points = find_low_points(input)
    low_coords = find_low_coords(low_points)
    basin_map = find_basins(input, low_coords)

    return calc_basin_risk(basin_map)


if __name__ == "__main__":
    input = load_input()
    
    print(part1(input), part2(input))