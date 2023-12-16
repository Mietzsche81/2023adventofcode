import numpy as np


def main(grid):
    # While steady state not reached ...
    while True:
        old_grid = grid.copy()
        # ... For each rock ...
        for x, y in np.argwhere(grid > 0):
            # ... if neighbor cell is empty...
            if not grid[max(x - 1, 0), y]:
                # ... Roll into empty cell.
                grid[max(x - 1, 0), y] = 1
                grid[x, y] = 0
        # If no rocks moved, steady state achieved.
        if (old_grid == grid).all():
            break

    score = sum(grid.shape[0] - rock[0] for rock in np.argwhere(grid > 0))
    return score
