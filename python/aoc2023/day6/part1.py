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


def calc_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


def degrees_of_freedom(time, distance):
    dof = 0
    for t in range(1, time):
        if calc_distance(t, time) > distance:
            dof += 1
    return dof


def main(times, distances):
    dof = []
    for t, d in zip(times, distances):
        dof.append(degrees_of_freedom(t, d))
    return np.product(dof)
