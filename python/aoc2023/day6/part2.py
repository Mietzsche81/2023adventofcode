import math

import numpy as np


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    for line in lines:
        line = line.strip().split()
        if line[0].strip() == "Time:":
            time = int("".join(line[1:]).replace(" ", ""))
        elif line[0].strip() == "Distance:":
            distance = int("".join(line[1:]).replace(" ", ""))

    return time, distance


def main(time, distance):
    # Quadratic formula for -1 * t**2 + time * t - distance > 0
    center = time / 2
    discriminant = np.sqrt(time * time - 4 * distance) / 2
    x, y = math.ceil(center - discriminant), math.floor(center + discriminant)
    # Return length of range between roots
    return y - x + 1
