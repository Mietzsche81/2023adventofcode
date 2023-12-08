from argparse import ArgumentParser

from parse import parse
from part1 import main as part1
from part2 import main as part2

arg_parser = ArgumentParser()
arg_parser.add_argument("part", type=str)
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

steps, paths = parse(args.input)

if str(args.part).lower() in ("1", "a"):
    result = part1(steps, paths)
elif str(args.part).lower() in ("2", "b"):
    result = part2(steps, paths)
else:
    raise ValueError(f"Unknown part {args.part}")

print(result)
