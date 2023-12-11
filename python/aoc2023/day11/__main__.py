from argparse import ArgumentParser

from parse import parse
from main import main

arg_parser = ArgumentParser()
arg_parser.add_argument("part", type=str)
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

galaxies, empty_row, empty_col = parse(args.input)

if str(args.part).lower() in ("1", "a"):
    result = main(galaxies, empty_row, empty_col, empty_size=2)
elif str(args.part).lower() in ("2", "b"):
    result = main(galaxies, empty_row, empty_col, empty_size=1e6)
else:
    raise ValueError(f"Unknown part {args.part}")

print(result)
