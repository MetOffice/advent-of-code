import numpy as np
from display import display

RAND = np.random.default_rng()

TARGET = np.array([
    [1,1,1,0,1,1,1],
    [0,0,1,0,0,1,0],
    [1,0,1,1,1,0,1],
    [1,0,1,1,0,1,1],
    [0,1,1,1,0,1,0],
    [1,1,0,1,0,1,1],
    [1,1,0,1,1,1,1],
    [1,0,1,0,0,1,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]
])

def random_clue():
    clue = TARGET.copy()

    RAND.shuffle(clue)
    RAND.shuffle(clue.T)

    return clue

def match_axis_sum(clue:np.ndarray, axis):
    target_sum = np.sum(TARGET, axis=1-axis)
    clue_sum = np.sum(clue, axis=1-axis)

    target_order = np.argsort(np.argsort(target_sum))
    clue_order = np.argsort(clue_sum)

    order = clue_order[target_order]

    # Same as indexing along the specified axis
    return clue.take(order, axis=axis)

clue = random_clue()

clue = match_axis_sum(clue, 0)
clue = match_axis_sum(clue, 1)

print(np.equal(clue, TARGET))

#display(clue)