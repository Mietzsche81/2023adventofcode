import itertools


def main(galaxies, empty_row, empty_col, empty_size=1):
    distance = 0
    expand = empty_size - 1
    for x, y in itertools.combinations(galaxies, 2):
        # Add basic distance
        distance += abs(y - x).sum()
        # Added expanded distance
        if expand:
            lower, upper = sorted([x, y], key=lambda g: g[0])
            left, right = sorted([x, y], key=lambda g: g[1])
            distance += expand * ((left[1] < empty_col) & (empty_col < right[1])).sum()
            distance += expand * ((lower[0] < empty_row) & (empty_row < upper[0])).sum()

    return distance
