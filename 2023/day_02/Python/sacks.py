from typing import Dict, Tuple
import math

max_balls: Dict[str,int] = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def single_game(input_string: str) -> Tuple[int,int]:
    [game, pulls] = input_string.split(':')
    pulls = pulls.split(';')

    result = int(game.split()[1])

    n_balls = { colour: 0 for colour in max_balls }

    for pull in pulls:
        ball_sets = pull.split(',')
        for balls in ball_sets:
            [n, colour] = balls.strip().split()
            n = int(n)
            n_balls[colour] = max(n, n_balls[colour])
            if n > max_balls[colour]:
                result = 0

    return result, math.prod(n_balls.values())

if __name__ == "__main__":
    with open("input.txt",'r') as f:
        n = 0
        powers = 0
        for line in f.readlines():
            game_number_or_0, power = single_game(line)
            n += game_number_or_0
            powers += power
        print(n)
        print(powers)
