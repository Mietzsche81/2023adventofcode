"""Call daily modules programmatically"""

from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
import re
import subprocess


arg_parser = ArgumentParser()
arg_parser.add_argument("module", type=str)
arg_parser.add_argument("input", type=str)


def parse_module(module):
    """Validate and construct output for module path argument"""
    match: re.Match = re.match(r"(\d+)\.?([aAbB12])", module)
    if match is None:
        raise ArgumentTypeError(f"Could not parse module for day '{module}'")
    day: str = match.group(1)
    p: Path = Path(__file__).parent / f"day{day}"
    if not p.is_dir():
        raise ArgumentTypeError(f"No day{day} module found at {p.resolve}")
    part: str = match.group(2).lower()
    if part in ("a", "1"):
        part = 1
    if part in ("b", "2"):
        part = 2
    else:
        raise ArgumentTypeError(f"Choose part a or part b: unrecognized part '{part}'")
    return p, part


def parse_input(module, input):
    """Validate and construct output for input file argument"""
    for stem in [
        Path("."),
        Path(module),
        Path(__file__).parent,
    ]:
        p: Path = stem / input
        if p.is_file():
            return p
    raise ArgumentTypeError(f"No input file found at '{p.resolve()}'")


args = arg_parser.parse_args()
module, part = parse_module(args.module)
input = parse_input(module, args.input)

print(module)
print(f"python '{module.as_posix()}' {part} {input}")
subprocess.call(
    [
        "python",
        rf'"{module}"',
        part,
        input.resolve(),
    ]
)
# subprocess.call(rf"python '{module.as_posix()}' {part} {input}", shell=True)
