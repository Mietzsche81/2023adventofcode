from argparse import ArgumentParser

from parse import parse, instructions_to_sequence
from process import shoelace_2d, orthogonal_perimeter

arg_parser = ArgumentParser()
arg_parser.add_argument("part", type=str)
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()

if str(args.part).lower() in ("1", "a"):
    data = parse(args.input, hex=False)
elif str(args.part).lower() in ("2", "b"):
    data = parse(args.input, hex=True)
else:
    raise ValueError(f"Unknown part {args.part}")

"""
Pick's Theorem
    area = internal + perimeter/2 - 1
    area := shoelace
    perimeter := manhattan
    =>
    internal := area - perimeter/2 + 1

Problem asks for number of squares filled, i.e.,
internal + perimeter?
=>
squares = area + perimeter/2 + 1
"""
sequence = instructions_to_sequence(*data)
area = shoelace_2d(sequence)
perimeter = orthogonal_perimeter(sequence)
squares = area + (perimeter // 2) + 1
print(squares)
