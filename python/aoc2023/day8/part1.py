import itertools as it


def main(steps, paths):
    start, stop = "AAA", "ZZZ"
    current = start
    for i, step in enumerate(it.cycle(steps)):
        if current == stop:
            break
        else:
            current = paths[current][step]

    return i
