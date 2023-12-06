import math

import numpy as np


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    for line in lines:
        line = line.strip().split()
        if line[0].strip() == "Time:":
            times = [int(t) for t in line[1:]]
        elif line[0].strip() == "Distance:":
            distances = [int(d) for d in line[1:]]

    return times, distances


def degrees_of_freedom(time, distance):
    # Quadratic formula for -1 * t**2 + time * t - distance > 0
    center = time / 2
    discriminant = np.sqrt(time * time - 4 * distance) / 2
    x, y = math.ceil(center - discriminant), math.floor(center + discriminant)
    # Return length of range between roots
    return y - x + 1


def main(times, distances):
    dof = 1
    for t, d in zip(times, distances):
        dof *= degrees_of_freedom(t, d)
    return dof
