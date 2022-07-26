from typing import Dict, List
import math
from collections import Counter

class Point:
    """
    Class containing a point in 2d space
    """
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other:"Delta") -> "Point":
        return Point(self.x + other.dx, self.y + other.dy)

    def __sub__(self, other:"Point") -> "Delta":
        return Delta(self.x - other.x, self.y - other.y)

    @staticmethod
    def newFromString(string:str) -> "Point":
        coords = [int(num) for num in string.strip().split(",")]
        return Point(*coords)

    def vertical(self, other:"Point") -> bool:
        return self.x == other.x

    def horizontal(self, other:"Point") -> bool:
        return self.y == other.y

class Delta:
    """
    Integer difference between points
    """
    def __init__(self, dx:int, dy:int) -> None:
        self.dx = dx
        self.dy = dy

    def __str__(self) -> str:
        return f"{self.dx},{self.dy}"

    def reduce(self):
        """
        Reduce to least integer form
        """
        factor = math.gcd(self.dx, self.dy)
        self.dx //= factor
        self.dy //= factor

class Line:
    """
    Class containing a line in 2d space
    """
    def __init__(self, a:Point, b:Point) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"{str(self.a)} -> {str(self.b)}"
    
    @staticmethod
    def newFromString(string:str) -> "Line":
        points = [Point.newFromString(coords) for coords in string.split("->")]
        return Line(*points)

    def gradient(self):
        """
        Get the gradient as an integer tuple
        """
        gradient = self.b - self.a
        gradient.reduce()
        return gradient

    def vertical(self):
        return self.a.vertical(self.b)

    def horizontal(self):
        return self.a.horizontal(self.b)
    
    def orthogonal(self):
        return self.horizontal() or self.vertical()

    def inner_points(self):
        """
        Iterator yielding each point on the line
        """
        gradient = self.gradient()
        point = self.a
        while point != self.b:
            yield point
            point += gradient
        yield self.b

class LineCollection:
    """
    Manages the storage of lines
    """
    def __init__(self, lines) -> None:
        self.lines = list(lines)

    def __index__(self, *args) -> Line:
        return self.lines.__index__(*args)
    
    def __iter__(self, *args):
        return self.lines.__iter__(*args)

    def __next__(self, *args):
        return self.lines.__next__(*args)

    def diagonal(self):
        """
        Get only diagonal lines
        """
        return LineCollection([line for line in self if not line.orthogonal()])

    def orthogonal(self):
        """
        Get only orthogonal lines
        """
        return LineCollection([line for line in self if line.orthogonal()])

class Map:
    """
    Remembers the locations of vents
    """
    def __init__(self, lines:LineCollection=None) -> None:
        self.map = Counter()
        if lines:
            self.add_lines(lines)

    def add_line(self, line:Line):
        """
        Adds a line to the map
        """
        self.map.update(line.inner_points())

    def add_lines(self, lines:LineCollection):
        """
        Adds all lines from the collection
        """
        for line in lines:
            self.add_line(line)

    def crossings(self):
        """
        Get list of points where multiple lines cross
        """
        return [key for (key,value) in self.map.items() if value > 1]

    def number_of_crossings(self):
        return len(self.crossings())


class FileReader:
    """
    Class retrieving data from an input file
    """
    def __init__(self, path) -> None:
        self.path = path
    
    def getLines(self):
        with open(self.path, "r") as file:
            lines = [Line.newFromString(line) for line in file]
        return LineCollection(lines)


def main():
    reader = FileReader("2021/day_05/input.txt")
    lines = reader.getLines()

    map = Map()

    map.add_lines(lines.orthogonal())
    print(map.number_of_crossings())

    map.add_lines(lines.diagonal())
    print(map.number_of_crossings())

if __name__ == "__main__":
    main()