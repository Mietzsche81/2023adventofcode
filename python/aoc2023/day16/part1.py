from argparse import ArgumentParser
import re
import numpy as np
import itertools
import math
import collections
from pprint import pprint

arg_parser = ArgumentParser()
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()
input_file = args.input

with open(input_file, "r") as fin:
    lines = fin.readlines()

grid = [list(stripped) for line in lines if (stripped := line.strip())]
for line in grid:
    print("".join(line))
print("\n" * 2)

xv = {((0, -1), (0, 1))}

energy = []
while True:
    old_xv = xv.copy()
    for x0, v0 in old_xv:
        xf = tuple(a + b for a, b in zip(x0, v0))
        vf = [v0]
        if not (0 <= xf[0] < len(grid)) or not (0 <= xf[1] < len(grid[0])):
            continue
        match grid[xf[0]][xf[1]]:
            case "|":
                if v0[1]:
                    vf = [(-1, 0), (1, 0)]
            case "-":
                if v0[0]:
                    vf = [(0, -1), (0, 1)]
            case "/":
                match v0:
                    case (1, 0):
                        vf = [(0, -1)]
                    case (-1, 0):
                        vf = [(0, 1)]
                    case (0, 1):
                        vf = [(-1, 0)]
                    case (0, -1):
                        vf = [(1, 0)]
            case "\\":
                match v0:
                    case (1, 0):
                        vf = [(0, 1)]
                    case (-1, 0):
                        vf = [(0, -1)]
                    case (0, 1):
                        vf = [(1, 0)]
                    case (0, -1):
                        vf = [(-1, 0)]
        xv |= {(xf, v) for v in vf}
    if len(xv) == len(old_xv):
        break


xf = {x for x, _ in xv}
encoded = [
    "".join(
        ["#" if (i, j) in xf else "." for j in range(len(grid[0]))],
    )
    for i in range(len(grid))
]
for line in encoded:
    print(line)
print("\n" * 2)

for x in xf:
    print(x)
print(len(xf) - 1)
