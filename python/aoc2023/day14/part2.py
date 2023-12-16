import numpy as np


def tuplize(grid):
    return tuple(map(tuple, np.argwhere(grid > 0)))


def main(grid):
    # Store shape of grid for detecting bounds, scoring rows.
    X, Y = grid.shape

    # Routines for getting index of neighbor from cell index
    north = lambda x, y: (max(x - 1, 0), y)
    west = lambda x, y: (x, max(y - 1, 0))
    south = lambda x, y: (min(x + 1, X - 1), y)
    east = lambda x, y: (x, min(y + 1, Y - 1))

    # Initialize cache of rock (x,y) states and the indexed revolution i at which they appear
    cache = {tuplize(grid): 0}

    # The indexed revolution at which we would like to score the state
    i_target = 1000000000
    # For each revolution
    for i in range(1, i_target):
        # For each set of rock movements corresponding to tipping the platform
        for move in [north, west, south, east]:
            # Simulate rockfalls until reaching steady state
            while True:
                old_grid = grid.copy()
                # For each rock...
                for x, y in np.argwhere(grid > 0):
                    neighbor = move(x, y)
                    # ... if neighbor cell is empty...
                    if not grid[neighbor]:
                        # ... Roll into empty cell.
                        grid[neighbor], grid[x, y] = 1, 0
                # If no rocks moved, steady state achieved.
                if (old_grid == grid).all():
                    break
        # Cache state in (turn into tuple to hash)
        state = tuplize(grid)
        # If already achieved this state
        if state in cache:
            # Found a steady period of repeating states
            i_original = cache[state]
            i_repeat = i
            # Don't need to continue simulating, can extrapolate via phasing
            break
        cache[state] = i

    # Find the equivalent index of the target state
    period = i_repeat - i_original
    phase = round((((i_target - i_original) / period) % 1) * period)
    i_equivalent = i_original + phase
    state = next(state for state, i in cache.items() if i == i_equivalent)

    # Apply weighting and sum to score
    score = sum(X - rock[0] for rock in np.array(state))
    return score
