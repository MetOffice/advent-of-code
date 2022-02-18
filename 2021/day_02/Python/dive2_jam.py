from dive_jam import Sub

class AimedSub(Sub):
    """
    Sub with aimed movement
    """
    def __init__(self):
        super().__init__()
        # Current gradient
        self.aim = 0

    def down(self, x):
        """
        Increases aim by x
        Deeper is positive
        """
        self.aim += x

    def up(self, x):
        """
        Decreases aim by x
        Shallower is negative
        """
        self.aim -= x
    
    def forward(self, x):
        """
        Changes horizontal position by x
        Changes depth by x * aim
        """
        self.h_pos += x
        self.v_pos += x * self.aim

sub = AimedSub()
sub.follow("./input.txt")
out = sub.h_pos * sub.v_pos
print(out)
