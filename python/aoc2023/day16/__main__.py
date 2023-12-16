from argparse import ArgumentParser

from parse import parse
from process import main

arg_parser = ArgumentParser()
arg_parser.add_argument("part", type=str)
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

data = parse(args.input)

if str(args.part).lower() in ("1", "a", "one"):
    starts = {((0, -1), (0, 1))}
    result = main(data, starts)
elif str(args.part).lower() in ("2", "b", "two"):
    X, Y = len(data), len(data[0])
    starts = (
        {((x, -1), (0, 1)) for x in range(X)}
        | {((x, Y), (0, -1)) for x in range(X)}
        | {((-1, y), (1, 0)) for y in range(Y)}
        | {((X, y), (-1, 0)) for y in range(Y)}
    )
    result = main(data, starts)
else:
    raise ValueError(f"Unknown part {args.part}")

print(result)
