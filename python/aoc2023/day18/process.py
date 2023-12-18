import itertools

import numpy as np


def shoelace_2d(sequence):
    """Shoelace area formula"""
    # Turn into linked list for iterating
    if sequence[0] != sequence[-1]:
        raise ValueError("Instructions do not form a closed loop!")
    area = 0
    for (ax, ay), (bx, by) in itertools.pairwise(sequence):
        area += (ax * by) - (ay * bx)
    # Last point
    area += (sequence[-1][0] * sequence[0][1]) - (sequence[0][0] * sequence[-1][1])
    return abs(area) // 2


def orthogonal_perimeter(sequence):
    """Manhattan perimeter"""
    if sequence[0] != sequence[-1]:
        raise ValueError("Instructions do not form a closed loop!")
    perimeter = []
    for (ax, ay), (bx, by) in itertools.pairwise(sequence):
        perimeter += [(bx - ax), (by - ay)]
    return np.abs(perimeter, dtype=int).sum()
