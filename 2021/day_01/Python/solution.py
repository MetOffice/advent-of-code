from collections import deque
from typing import List

from toolz import sliding_window

from common import loaders, timers


@timers.print_duration
def count_depth_increases(depths: List[int]) -> int:
    """
    Take a list of depths and count the number of times it increases between
    elements. Depth is positive.
    """
    count = 0
    last = depths[0]
    for next_ in depths[1:]:
        if next_ > last:
            count += 1
        last = next_
    return count


@timers.print_duration
def count_depth_increases_zip(depths: List[int]) -> int:
    """
    Take a list of depths and count the number of times it increases between
    elements. Depth is positive.
    """
    pairs = zip(depths, depths[1:])
    return sum((1 if b > a else 0 for a, b in pairs))


def smooth_depths(depths: List[int]) -> List[int]:
    smoothed_depths = []
    window = deque(depths[:2], maxlen=3)
    for depth in depths[2:]:
        window.append(depth)
        smoothed_depths.append(sum(window))
    return smoothed_depths


def smooth_depths_toolz(depths: List[int]) -> List[int]:
    return list(map(sum, sliding_window(3, depths)))


def count_depth_increases_smoothed(depths: List[int]) -> int:
    smoothed_depths = smooth_depths(depths)
    return count_depth_increases(smoothed_depths)


if __name__ == "__main__":
    depths = loaders.load_ints()
    answer1 = count_depth_increases(depths)
    answer1b = count_depth_increases_zip(depths)
    print(f"Part 1 answer: {answer1}")

    answer2 = count_depth_increases_smoothed(depths)
    print(f"Part 2 answer: {answer2}")
