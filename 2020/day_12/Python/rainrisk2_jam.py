import math
import sys
sys.path.append("./2020/common")
from loaders import load_string

def manhattan_distance(directions):
    """
    Takes a list of single character direction and numeric distance commands, outputting the manhattan distance from origin.
    Rotation is measured in degrees clockwise from x axis.
    Waypoint is functionally a speed vector of the boat.
    Valid commands are:
        N - Move waypoint +y
        E - Move waypoint +x
        S - Move waypoint -y
        W - Move waypoint -x
        L - Rotate waypoint +
        R - Rotate waypoint -
        F - Change position by multiple of waypoint vector

    Input:
        directions - List of string commands

    Output:
        manhattan distance from origin
    """

    # initialise boat
    boat = Boat(0,0,10,1)

    for command in directions:
        boat.command(command)

    # return manhattan distance
    return boat.manhattan_distance()
    
class Boat:
    """
    Class for managing boat's current waypoint and position
    """
    def __init__(self, bx, by, wx, wy):
        """
        bx, by: Boat's initial x and y positions
        wx, wy: Waypoint's initial x and y positions
        _command: Dictionary of  functions, used to translate command strings into methods with correct args
        """
        self.bx = bx
        self.by = by
        self.wx = wx
        self.wy = wy

        self._command = {
            "E": lambda x: self.translate_waypoint(x, 0),
            "W": lambda x: self.translate_waypoint(-x, 0),
            "N": lambda x: self.translate_waypoint(0, x),
            "S": lambda x: self.translate_waypoint(0, -x),
            "L": lambda x: self.rotate_waypoint(x),
            "R": lambda x: self.rotate_waypoint(-x),
            "F": self.move
        }

    def command(self, command_string):
        """
        Interpret a command string and call the correct command
        """
        comm = command_string[0]
        x = int(command_string[1:])
        self._command[comm](x)

    def translate_waypoint(self, dx, dy):
        """
        Move waypoint by given x and y deltas
        """
        self.wx += dx
        self.wy += dy

    def rotate_waypoint(self, r, intgrid=True):
        """
        Rotate waypoint by r degrees clockwise
        intgrid is a toggle for integer answers. The problem does not specify that the boat must remain on integer grid spaces, though it tends to.
        """
        rr = math.radians(r)
        wx = self.wx * math.cos(rr) - self.wy * math.sin(rr)
        wy = self.wx * math.sin(rr) + self.wy * math.cos(rr)
        if intgrid:
            wx = int(round(wx))
            wy = int(round(wy))
        self.wx = wx
        self.wy = wy

    def move(self, dist):
        """
        Move in direction of waypoint dist times
        """
        self.bx += dist * self.wx
        self.by += dist * self.wy

    def manhattan_distance(self):
        """
        Return current manhattan distance from the origin
        """
        return abs(self.bx) + abs(self.by)

if __name__ == "__main__":
    directions = load_string()
    d = manhattan_distance(directions)
    print(d)