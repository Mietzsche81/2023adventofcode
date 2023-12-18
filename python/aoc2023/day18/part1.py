import sys
import itertools


raw = open(sys.argv[1]).read().strip()

lines = [stripped for line in raw.split("\n") if (stripped := line.strip())]

direction = [line.split()[0].strip() for line in lines]
distance = [int(line.split()[1]) for line in lines]
color = [line.split()[2].strip()[2:-1] for line in lines]


delta = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}

location = (0, 0)
grid = {location: color[0]}
for heading, d, c in zip(direction, distance, color):
    u = delta[heading]
    for i in range(d):
        location = (location[0] + u[0], location[1] + u[1])
        grid[location] = c


# Shift & sort grid
x, y = list(zip(*grid))
x0, xf = min(x), max(x)
y0, yf = min(y), max(y)
grid = dict(sorted({(x - x0, y - y0): value for (x, y), value in grid.items()}.items()))
x, y = list(zip(*grid))
X, Y = max(x) + 1, max(y) + 1


def find_enclosed(grid):
    # TODO: upper corner logic, detect below.
    rows = [[y for y in range(Y) if (x, y) in grid] for x in range(X)]
    # First and last row
    inside = len(rows[0]) + len(rows[-1])
    for x in range(1, X - 1):
        row = rows[x]
        internal = False
        for a, b in itertools.pairwise(row):
            # Flip on passing wall
            if (x + 1, a) in grid:
                internal = not internal
            if internal:
                inside += b - a - 1
        inside += len(row)

    return inside


def encode(grid):
    return [
        "".join(["#" if (x, y) in grid else "." for y in range(Y)]) for x in range(X)
    ]


print(find_enclosed(grid))
