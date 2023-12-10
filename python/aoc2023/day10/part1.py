from argparse import ArgumentParser
import numpy as np


arg_parser = ArgumentParser()
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

input_file = args.input
with open(input_file, "r") as fin:
    lines = fin.readlines()

encoding = {c: i for i, c in enumerate(".|-LJ7FS")}
decoding = {i: c for c, i in encoding.items()}

grid = np.array(
    [
        [encoding[char] for char in stripped]
        for line in lines
        if (stripped := line.strip())
    ]
)
size = grid.shape
start = np.argwhere(grid == encoding["S"])[0]


def neighbors(cell):
    valid = {
        (-1, 0): "|7F",
        (1, 0): "|JL",
        (0, -1): "-FL",
        (0, 1): "-J7",
    }
    locs = {
        rel: abs
        for rel in valid
        if ([0, 0] <= (abs := cell + rel)).all() and (abs < size).all()
    }

    return [
        absolute
        for relative, absolute in locs.items()
        if (grid[*absolute] in (encoding[char] for char in valid[relative]))
    ]


def advance(previous, current):
    delta = current - previous
    match decoding[grid[*current]]:
        case "|":
            if delta[0] > 0:
                return current + [1, 0]
            else:
                return current - [1, 0]
        case "-":
            if delta[1] > 0:
                return current + [0, 1]
            else:
                return current - [0, 1]
        case "L":
            if delta[0] > 0:
                return current + [0, 1]
            else:
                return current - [1, 0]
        case "J":
            if delta[0] > 0:
                return current - [0, 1]
            else:
                return current - [1, 0]
        case "7":
            if delta[1] > 0:
                return current + [1, 0]
            else:
                return current - [0, 1]
        case "F":
            if delta[1] < 0:
                return current + [1, 0]
            else:
                return current + [0, 1]


loop = [start, neighbors(start)[0]]
while not (loop[-1] == start).all():
    loop.append(advance(*loop[-2:]))

print(np.ceil(len(loop) // 2))

"""

def get(cell):
    return grid[cell[0]][cell[1]]

def start_type(start):
    others = neighbors(start)
    path = [others[1], start, others[1]]
    symbols = {get(other) for other in others}
    match symbols:
        case {"|"}:
            return "|"
    delta = (others[1][0] - others[0][0], others[1][1] - others[0][1])
    match delta:
        case (2, 0) | (-2, 0):
            return "|"
        case (0, 2) | (0, -2):
            return "-"
        case (1, 1) | (-1, -1):
            d2 = (start[0] - )
            if None:
                return "L"
            else:
                return "7"
        case (-1, 1) | (1, -1):
            if None:
                return "J"
            else:
                return "F"

loop = [start, neighbors(start)[0]]
while loop[-1] != start:
    loop.append(advance(*loop[-2:]))
"""
