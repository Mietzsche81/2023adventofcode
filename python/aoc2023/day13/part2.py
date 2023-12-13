from argparse import ArgumentParser
import numpy as np
import re
import math
import itertools

arg_parser = ArgumentParser()
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

input_file = args.input

with open(input_file, "r") as fin:
    data = fin.read()

patterns = [stripped for p in data.split("\n\n") if (stripped := p.strip())]


score = 0
for pattern in patterns:
    pattern_score = 0
    # Horizontal
    grid = [stripped for line in pattern.split() if (stripped := line.strip())]
    for i in range(1, len(grid)):
        before, after = grid[:i][::-1], grid[i:]
        if (
            sum(
                1 for b, a in zip(before, after) for b_i, a_i in zip(b, a) if b_i != a_i
            )
            == 1
        ):
            pattern_score = 100 * i
            score += pattern_score
            break
    if pattern_score:
        continue
    # Vertical
    grid = ["".join(col) for col in list(map(list, zip(*grid)))]
    # print(grid)
    for i in range(1, len(grid)):
        before, after = grid[:i][::-1], grid[i:]
        if (
            sum(
                1 for b, a in zip(before, after) for b_i, a_i in zip(b, a) if b_i != a_i
            )
            == 1
        ):
            pattern_score = i
            score += pattern_score
            break
    if not pattern_score:
        raise ValueError("Did not find reflection")
    # print(pattern_score)
    # input()

print(score)
