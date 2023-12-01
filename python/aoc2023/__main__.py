"""Call daily modules programmatically"""

from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
import re


arg_parser = ArgumentParser()
arg_parser.add_argument("module", type=str)
arg_parser.add_argument("input", type=str)


def parse_module(module):
    """Validate and construct output for module path argument"""
    match: re.Match = re.match(r"(\d+)([aAbB])", module)
    if match is None:
        raise ArgumentTypeError(f"Could not parse module for day '{module}'")
    day: str = match.group(1)
    part: str = match.group(2).lower()
    p: Path = Path(__file__).parent / f"day{day}"
    if not p.is_dir():
        raise ArgumentTypeError(f"No day{day} module found at {p.resolve}")
    if part not in ("a", "b"):
        raise ArgumentTypeError(f"Choose part a or part b: unrecognized part '{part}'")
    return p, part


def parse_input(module, input):
    """Validate and construct output for input file argument"""
    for stem in [Path(__file__).parent, Path(module), Path(".")]:
        p: Path = stem / input
        if p.is_file():
            return p
    raise ArgumentTypeError(f"No input file found at '{p.resolve()}'")


args = arg_parser.parse_args()
module, part = parse_module(args.module)
input = parse_input(module, args.input)
