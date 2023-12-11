import itertools

import numpy as np


def main(galaxies, empty_row, empty_col, empty_size=1):
    distance = 0
    for x, y in itertools.combinations(range(len(galaxies)), 2):
        lower, upper = sorted([galaxies[x], galaxies[y]], key=lambda g: g[0])
        left, right = sorted([galaxies[x], galaxies[y]], key=lambda g: g[1])
        vertical = (range(lower[0] + 1, upper[0] + 1) == empty_row).any(axis=0)
        horizontal = (range(left[1] + 1, right[1] + 1) == empty_col).any(axis=0)

        distance += vertical.sum() * empty_size + (~vertical).sum()
        distance += horizontal.sum() * empty_size + (~horizontal).sum()

    return distance
