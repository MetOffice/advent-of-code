from typing import List
import math
import sys
sys.path.append("./2020/common")
from loaders import load_string

def manhattan_distance(directions):
    """
    Takes a list of single character direction and numeric distance commands, outputting the manhattan distance from origin.
    Rotation is measured in degrees clockwise from x axis.
    Valid commands are:
        N - Move +y
        E - Move +x
        S - Move -y
        W - Move -x
        L - Change rotation +
        R - Change rotation -
        F - Move in direction of current rotation

    Input:
        directions - List of string commands

    Output:
        manhattan distance from origin
    """

    #start at origin
    x = 0
    y = 0
    # rotation facing east
    r = 0

    for command in directions:
        # first character is direction
        dir = command[0]
        # Remaining characters are distance, always integer
        dist = int(command[1:])
        # find change in r, x, y by command
        delx, dely, delr = run_command[dir](dist, r)
        # update position
        x += delx
        y += dely
        r += delr
    
    # return manhattan distance
    return abs(x) + abs(y)

# Set of functions that return the x, y and r deltas based on params and identified by command character
run_command = {
    "E": lambda dist, r: (dist, 0, 0),
    "W": lambda dist, r: (-dist, 0, 0),
    "N": lambda dist, r: (0, dist, 0),
    "S": lambda dist, r: (0, -dist, 0),
    "L": lambda dist, r: (0, 0, dist),
    "R": lambda dist, r: (0, 0, -dist),
    "F": lambda dist, r: (dist * math.cos(math.radians(r)), dist * math.sin(math.radians(r)), 0)
}



if __name__ == "__main__":
    directions = load_string()
    d = manhattan_distance(directions)
    print(d)