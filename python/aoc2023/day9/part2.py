import numpy as np


def main(histories: list[list[int]]):
    first = []
    for history in histories:
        d = [np.array(history)]
        while d[-1].any():
            d.append(np.diff(d[-1]))
        d = d[::-1]
        if len(d) > 2:
            for i in range(1, len(d)):
                d[i] = np.append(
                    d[i][0] - d[i - 1][0],
                    d[i],
                )
        first.append(d[-1][0])

    return sum(first)
