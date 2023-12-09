import re
import math
import itertools as it
import numpy as np
from pprint import pprint

from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()
input_file = args.input

with open(input_file, "r") as fin:
    lines = fin.readlines()

histories = [[int(x) for x in line.strip().split()] for line in lines]


history = histories[0]
last = []
for history in histories:
    d = [np.array(history)]
    while d[-1].any():
        d.append(np.diff(d[-1]))
    d = d[::-1]
    if len(d) > 2:
        for i in range(1, len(d)):
            d[i] = np.append(d[i], d[i][-1] + d[i - 1][-1])
    pprint(d)
    print()
    last.append(d[-1][-1])

print(last)
print(sum(last))
