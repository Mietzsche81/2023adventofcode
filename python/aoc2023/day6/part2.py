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


def calc_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


def degrees_of_freedom(time, distance):
    dof = 0
    for t in range(1, time):
        if calc_distance(t, time) > distance:
            dof += 1
    return dof


def main(time, distance):
    # lower, upper, tol = 1, time - 1, 0.5
    # f = lambda t: t * (time - t) - distance
    a = time / 2
    b = np.sqrt(time * time - 4 * distance) / 2
    x, y = math.ceil(a - b), math.floor(a + b)
    return y - x + 1
