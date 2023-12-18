import sys
import itertools

import numpy as np

from parse import parse

direction, distance = parse(sys.argv[1], hex=True)

encode = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}

# Apply instructions sequentially
location = (0, 0)
sequence = [location]
for u, d in zip(direction, distance):
    u = encode[u]
    location = (location[0] + d * u[0], location[1] + d * u[1])
    sequence.append(location)

# Shift to Q1
x, y = list(zip(*sequence))
x0, xf = min(x), max(x)
y0, yf = min(y), max(y)
X, Y = (xf - x0) + 1, (yf - y0) + 1

# Turn into linked list
n = len(sequence)
loop = [
    (
        sequence[(i - 1) % n],  # Previous
        sequence[i],  # Current
        sequence[(i + 1) % n],  # Next
    )
    for i in range(n)
]


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


internal = shoelace_2d(sequence)
perimeter = orthogonal_perimeter(sequence)
enclosed = internal + (perimeter // 2) + 1

print(internal, perimeter, enclosed)
