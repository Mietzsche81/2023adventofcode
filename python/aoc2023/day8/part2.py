import itertools as it
import math


def main(steps, paths):
    start = [x for x in paths if x.endswith("A")]
    ends = []
    for s in start:
        current = s
        for i, step in enumerate(it.cycle(steps)):
            if current.endswith("Z"):
                ends.append(i)
                break
            else:
                current = paths[current][step]

    return math.lcm(*ends)
