import numpy as np


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()

    grid = np.array(
        [
            [1 if char == "#" else 0 for char in line.strip()]
            for line in lines
            if line.strip()
        ]
    )
    galaxies = np.argwhere(grid)
    empty_row = np.argwhere(~grid.any(axis=1))
    empty_col = np.argwhere(~grid.any(axis=0))

    return galaxies, empty_row, empty_col
