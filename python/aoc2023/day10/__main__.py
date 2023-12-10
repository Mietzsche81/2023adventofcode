from argparse import ArgumentParser

import numpy as np

from grid import Grid

arg_parser = ArgumentParser()
arg_parser.add_argument("part", type=str)
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

grid = Grid(args.input)

if str(args.part).lower() in ("1", "a"):
    grid.find_loop()
    result = np.ceil(len(grid.loop) // 2)
elif str(args.part).lower() in ("2", "b"):
    result = grid.find_enclosed()
else:
    raise ValueError(f"Unknown part {args.part}")

print(result)
