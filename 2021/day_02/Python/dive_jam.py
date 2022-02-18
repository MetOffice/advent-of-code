
class Sub():
    """
    Class representing submarine, including movement methods and location tracking
    """
    def __init__(self):
        # horizontal position
        self.h_pos = 0
        # vertical position
        self.v_pos = 0
        # dict of keyword->action
        self._go = {
            "forward": self.forward,
            "down": self.down,
            "up": self.up
        }

    def go(self, direction, distance):
        """
        Change position according to given direction and distance
        """
        assert direction in self._go.keys(), "Invalid direction."
        self._go[direction](distance)

    def forward(self, x):
        """
        Increase horizontal position by x
        """
        self.h_pos += x

    def down(self, x):
        """
        Increase vertical position by x
        Note that v_pos is depth so down is positive
        """
        self.v_pos += x
    
    def up(self, x):
        """
        Decrease vertical position by x
        Note that v_pos is depth so up is negative
        """
        self.v_pos -= x

    def follow(self, path):
        """
        Follow all move commands in the file at the given path
        """
        with open(path, "r") as file:
            for line in file:
                direction, distance = line.split()
                self.go(direction, int(distance))

sub = Sub()
sub.follow("./input.txt")
out = sub.h_pos * sub.v_pos
print(out)