import numpy as np

# all directions that border on hex grid
neighbours = np.array([
    [1,0],
    [-1,0],
    [0,1],
    [-1,1],
    [1,-1],
    [0,-1]
])

# coordinates for hexagonal array
cardinal_to_coord = {
    "e":neighbours[0],
    "w":neighbours[1],
    "ne":neighbours[2],
    "nw":neighbours[3],
    "se":neighbours[4],
    "sw":neighbours[5]
}

def read_input():
    with open("./2020/day_24/input.txt", "r") as file:
        lines = file.readlines()
    return lines

def count_black():
    """
    Determine all tile flips then return the number that are black
    """
    black_tiles = initial_black_tiles()
    return len(black_tiles)

def count_black_after_100():
    """
    Flip initial tiles then follow the flip pattern for 100 days, then determine the number of black tiles
    """
    black_tiles = initial_black_tiles()
    # 100 days
    for i in range(100):
        # run process
        black_tiles = pass_day(black_tiles)
        # long process so send reports
        print(f"Day {i+1}")
    return len(black_tiles)

def initial_black_tiles():
    """
    Return coordinates of black tiles in inital state
    """
    input = read_input()
    # turn list of strings to list of lists of instructions
    instructions = [read_string(string) for string in input]
    # turn list of instructions to coordinates
    flips = [follow_instructions(instruction) for instruction in instructions]
    # determine which tiles are flipped
    return determine_flipped(flips)

def read_string(string):
    """
    Turn string of non-delimited cardinals into list of individual cardinals
    """
    out = []
    # was last char a north or south
    ns = ""
    for char in string:
        # north and south modify next char
        if char in "ns":
            ns = char
        # east and west add to instructions, possibly modified
        if char in "ew":
            out.append(ns+char)
            # no modifier for next char
            ns = ""
    return out

def follow_instructions(instruction):
    """
    Starting at 0,0, follow instructions and return final coords
    """
    pos = np.array((0,0))
    for cardinal in instruction:
        pos += cardinal_to_coord[cardinal]
    return pos

def determine_flipped(coordinates):
    """
    Return a list of each coordinate that appears an odd number of times in the list
    """
    # find unique coordinate pairs
    uniques, freqs = np.unique(coordinates, return_counts=True, axis=0)
    # return all values where freqs is odd
    return uniques[(freqs % 2 == 1)]

def pass_day(black_tiles):
    """
    Determine black tiles after passing one day
    """
    new_black_tiles = []
    # find all grid points on or adjacent to a black tile and the number of neighbouring black tiles
    neighbourhood, black_neighbours = compute_neighbourhood(black_tiles, True)
    for tile, neighbours in zip(neighbourhood, black_neighbours):
        # determine whether current tile is black
        is_black = tile_in_list(tile, black_tiles)
        # work out if tile becomes or remains black
        if becomes_black(is_black, neighbours):
            new_black_tiles.append(tile)
    # make array for fast goodness
    return np.array(new_black_tiles)

def compute_neighbourhood(tiles:np.ndarray, multiplicity=False):
    """
    Get list of all tiles adjacent to the given tile/s. This includes the tiles themselves.
    If multiplicity is True then also return the number of black tiles each neighbourhood tile borders.
    """
    # ensure tile index varies in i, adjacency in j, coord xy in k
    tiles = tiles.reshape(-1,1,2)
    adjacency = neighbours.reshape(1,-1,2)
    # sum gets all possible neighbours
    all_possible = tiles + adjacency
    # flatten
    all_possible = all_possible.reshape(-1,2)
    # return only unique
    return np.unique(all_possible, axis=0, return_counts=multiplicity)

def count_black_neighbours(tile, black_tiles):
    """
    Count the number of neighbours of the tile that appear in black_tiles
    """
    count = 0
    # get all neighbours
    neighbourhood = compute_neighbourhood(tile)
    for neighbour in neighbourhood:
        # count if neighbour is black and not itself
        if tile_in_list(neighbour, black_tiles) and not np.all(neighbour == tile):
            count += 1
    return count

def becomes_black(is_black, black_neighbours):
    """
    Determine whether a tile will be black on the next day
    """
    # black tiles remain black if 1 or 2 black neighbours 
    if is_black:
        return black_neighbours in (1,2)
    # white tiles become black if exactly 2 black neighbours
    else:
        return black_neighbours == 2

def tile_in_list(tile, list):
    """
    Determine whether a tile is in the given list
    """
    return np.any(np.all(list == tile, axis=1))


print(count_black_after_100())

a = np.array((1,0))
b = np.array(((1,0),(0,0)))

#print(pass_day(pass_day(b)))