import collections

State = tuple[tuple[int], tuple[int]]


def main(grid: list[str], starts):
    X, Y = len(grid), len(grid[0])
    energy: dict[State, int] = {start: 0 for start in starts}
    for start in energy:
        xv = collections.deque([start])
        cache: set[State] = set()
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
            vf = [v0]  # default case
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

    # Return maximum energy found from all starts
    return max(energy.values())
