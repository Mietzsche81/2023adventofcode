import numpy as np


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    lines = [stripped for line in lines if (stripped := line.strip())]

    grid = np.array([list(line) for line in lines])
    grid = np.zeros((len(lines), len(lines[0].strip())), dtype=np.int32)
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            if char == "O":
                grid[i, j] = 1
            elif char == "#":
                grid[i, j] = -1

    return grid
