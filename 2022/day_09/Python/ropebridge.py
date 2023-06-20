import numpy as np

class Knot:
    def __init__(self) -> None:
        self.position = np.array((0, 0))
        self.follow_call = None

    def update_position(self, direction_vector):
        self.position += direction_vector
        if self.follow_call:
            self.follow_call()

class Head(Knot):
    direction = {
        "U": np.array((0, 1)),
        "R": np.array((1, 0)),
        "D": np.array((0, -1)),
        "L": np.array((-1, 0)),
    }
    def __init__(self) -> None:
        super().__init__()

    def wiggle_loop(self, instructions):
        for instruction in instructions:
            self.wiggle(instruction)

    def wiggle(self, instruction):
        self.update_position(Head.direction[instruction])
        

class Tail(Knot):
    def __init__(self, head) -> None:
        super().__init__()
        self.head = head
        head.follow_call = self.woggle
        self.trail = set()
        self.trail.add(tuple(self.position))

    def woggle(self):
        head_tail_vector = self.head.position - self.position 
        if np.linalg.norm(head_tail_vector) >=2:
            tail_move = np.clip(head_tail_vector, -1, 1)
            self.update_position(tail_move)
            self.trail.add(tuple(self.position))

    def return_trail(self):
        return len(self.trail)


def read_instructions():
    with open("../input.txt", "r") as input_instructions:
        instructions = ""
        for line in input_instructions:
            direction, distance = line.strip().split()
            instructions += (direction*int(distance))
    return instructions

def make_rope(rope_length):
    head = Head()
    last_tail_which_is_also_now_a_head_i_guess = head
    for i in range(rope_length -1):
        last_tail_which_is_also_now_a_head_i_guess = Tail(last_tail_which_is_also_now_a_head_i_guess)
    return head, last_tail_which_is_also_now_a_head_i_guess

def main():
    instructions = read_instructions()
    head,tail = make_rope(10)
    head.wiggle_loop(instructions)
    print(tail.return_trail())
    



if __name__=="__main__":
    main()