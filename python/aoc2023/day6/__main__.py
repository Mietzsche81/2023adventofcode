from argparse import ArgumentParser

from part1 import main as part1, parse as parse1
from part2 import main as part2, parse as parse2

arg_parser = ArgumentParser()
arg_parser.add_argument("part", type=str)
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()


if str(args.part).lower() in ("1", "a"):
    times, distances = parse1(args.input)
    result = part1(times, distances)
elif str(args.part).lower() in ("2", "b"):
    time, distance = parse2(args.input)
    result = part2(time, distance)
else:
    raise ValueError(f"Unknown part {args.part}")

print(result)
