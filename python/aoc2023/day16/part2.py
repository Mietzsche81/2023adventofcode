from argparse import ArgumentParser
import collections

arg_parser = ArgumentParser()
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()
input_file = args.input

with open(input_file, "r") as fin:
    lines = fin.readlines()

grid = [list(stripped) for line in lines if (stripped := line.strip())]

X, Y = len(grid), len(grid[0])

energy = (
    {((x, -1), (0, 1)): 0 for x in range(X)}
    | {((x, Y), (0, -1)): 0 for x in range(X)}
    | {((-1, y), (1, 0)): 0 for y in range(Y)}
    | {((X, y), (-1, 0)): 0 for y in range(Y)}
)
for start in energy:
    xv = collections.deque([start])
    cache = set()
    while xv:
        x0, v0 = xv.pop()
        xf = x0[0] + v0[0], x0[1] + v0[1]
        # Repeated state, do not reevaluate
        if (xf, v0) in cache:
            continue
        # Left the grid, do not project forward
        elif not ((0 <= xf[0] < X) and (0 <= xf[1] < Y)):
            continue
        else:
            cache.add((xf, v0))

        # Iterate forward
        vf = [v0]
        match grid[xf[0]][xf[1]]:
            case "|":
                if v0[1]:
                    vf = [(-1, 0), (1, 0)]
            case "-":
                if v0[0]:
                    vf = [(0, -1), (0, 1)]
            case "/":
                vf = [(-v0[1], -v0[0])]
            case "\\":
                vf = [(v0[1], v0[0])]

        # Append forward states to queue
        for v in vf:
            xv.append((xf, v))
    energy[start] = len({x for x, _ in cache})

print(max(energy.values()))
