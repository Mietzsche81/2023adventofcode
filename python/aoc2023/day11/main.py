import itertools

import numpy as np


def main(galaxies, empty_row, empty_col, empty_size=1):
    distance = 0
    for x, y in itertools.combinations(range(len(galaxies)), 2):
        lower, upper = sorted([galaxies[x], galaxies[y]], key=lambda g: g[0])
        left, right = sorted([galaxies[x], galaxies[y]], key=lambda g: g[1])
        for j in range(left[1] + 1, right[1] + 1):
            if j in empty_col:
                distance += empty_size
            else:
                distance += 1
        for i in range(lower[0] + 1, upper[0] + 1):
            if i in empty_row:
                distance += empty_size
            else:
                distance += 1

    return distance
