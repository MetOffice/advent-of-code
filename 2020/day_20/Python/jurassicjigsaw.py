from typing import Dict
import numpy as np

cardinals = ["n","e","s","w"]

def load_string():
    with open("./2020/day_20/input.txt", "r") as file:
        out = file.readlines()
    return out

class Tile():
    """
    Stores id and content of a tile
    """
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self._edges = None

    @staticmethod
    def from_string_def(string_def):
        """
        Create tile from a string definition
        """
        # split block into title and body
        title = string_def[0]
        body = string_def[1:]
        # Format "Tile xxxx:"
        id = int(title[5:9])
        # convert list of strings to list of lists then 2d array
        content = [list(row.strip()) for row in body]
        content = np.array(content)
        # hash for true
        content = content == "#"
        # Create tile object
        return Tile(id, content)

    def north(self):
        """
        Get north edge
        """
        return tuple(self.content[0])

    def south(self):
        """
        Get south edge
        """
        return tuple(self.content[-1])
    
    def west(self):
        """
        Get west edge
        """
        return tuple(self.content[:,0])
    
    def east(self):
        """
        Get east edge
        """
        return tuple(self.content[:,-1])

    def transform(self, trans):
        """
        Return a copy of this tile following the transformation
        """
        return Tile(self.id, transform(self.content, trans))

    def image(self):
        """
        Returns only image data, that is all non-border elements of the content
        """
        # ignore first and last row and column
        return self.content[1:-1,1:-1]

def corner_product():
    """
    Solve the jigsaw and return the product of the ids of the four corner tiles
    """
    strings = load_string()
    # create list of Tile objects
    tiles = interpret_tiles(strings)
    # solution is a numpy array of tile objects
    solution = solve(tiles)
    # return product of four corners
    return solution[0][0].id * solution[0][-1].id * solution[-1][0].id * solution[-1][-1].id

def interpret_tiles(strings):
    """
    Takes string list from file and creates a dictionary of tiles
    """
    tiles = []
    # store recently observed lines
    recent = []
    for line in strings:
        # if not a blank line, store it
        if line.strip():
            recent.append(line)
        # else interpret the last block and reset recently seen
        else:
            tiles.append(Tile.from_string_def(recent))
            recent = []
    # add last tile
    tiles.append(Tile.from_string_def(recent))
    return tiles

def solve(tiles):
    """
    Find the location of each tile where edges match. Tiles can be reflected or rotated.
    Outer edges are guaranteed not to match any other edge.
    Inner edges match at least one edge. Not specified to be unique in question, but true in input.
    """
    solution = {}
    # pick start
    solution = {
        (0,0): tiles[0]
    }
    # remove as candidate
    tiles.remove(tiles[0])
    # recursively and greedily place tiles
    solution = flood_fill((0,0), solution, tiles)
    # return array of ids
    return soln_dict_to_array(solution)

def flood_fill(index:tuple, solution:Dict, tiles):
    """
    Recursively solve puzzle by greedy algorithm. Assumes each pair of edges is unique
    """
    # store for the tile and transform that matches
    matchTile = None
    matchTransform = None
    # check each direction
    for cardinal, neighbour in zip(cardinals, neighbours(index)):
        # if unfilled
        if neighbour not in solution.keys():
            # test all tiles
            for tile in tiles:
                # test all transformations
                for trans in range(8):
                    candidate = tile.transform(trans)
                    # if it matches, record it
                    if match_direction(cardinal, solution[index], candidate):
                        matchTransform = trans
                        break
                # if a transform was found, record this tile
                if matchTransform is not None:
                    matchTile = tile
                    break
            # if we found a match, store
            if matchTile is not None:
                # remove from candidate list
                tiles.remove(matchTile)
                # place in grid
                solution[neighbour] = matchTile.transform(matchTransform)
                # reset store
                matchTile = None
                matchTransform = None
                # fill recursively
                solution = flood_fill(neighbour, solution, tiles)
    return solution

def soln_dict_to_array(solution):
    """
    Takes a solution dictionary and places the ids in an array. Dictionary keys may be negative
    """
    # extract bounds
    keys = solution.keys()
    imin = min([key[0] for key in keys])
    imax = max([key[0] for key in keys])
    jmin = min([key[1] for key in keys])
    jmax = max([key[1] for key in keys])
    # init array
    soln_array = np.empty((imax - imin + 1, jmax - jmin + 1), dtype=object)
    # write ids into array
    for key in keys:
        soln_array[key[0] - imin, key[1] - jmin] = solution[key]
    # Check complete grid
    assert np.all(soln_array), "Some values missing"
    return soln_array

def neighbours(index):
    """
    Returns a list of neighbours of an integer coordinate in order n,e,s,w
    """
    return [
        (index[0]-1,index[1]),
        (index[0],index[1]+1),
        (index[0]+1,index[1]),
        (index[0],index[1]-1),
    ]

def match_direction(cardinal, back:Tile, forward:Tile):
    """
    Test whether the leading edge of back matches the trailing edge of forward
    """
    assert cardinal in cardinals, "must supply valid cardinal"
    if cardinal == "n":
        return back.north() == forward.south()
    if cardinal == "s":
        return back.south() == forward.north()
    if cardinal == "e":
        return back.east() == forward.west()
    if cardinal == "w":
        return back.west() == forward.east()

def transform(array, trans):
    """
    Apply one of the 8 different reflections/rotations to the array. trans is the name of the transformation, an int 0-7 inc.
    Integers 8+ are equivalent to their modulo 8
    """
    # if 1,3,5,7 reflect vertical
    if trans % 2 > 0:
        array = array[::-1,:]
    # if 2,3,6,7 reflect horizontal
    if trans % 4 > 1:
        array = array[:,::-1]
    # if 4,5,6,7 reflect diagonal
    if trans % 8 > 3:
        array = array.T
    return array


if __name__ == "__main__":
    print(corner_product())