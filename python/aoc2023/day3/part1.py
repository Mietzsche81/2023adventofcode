import itertools as it
import re
from typing import List


def main(lines: List[str]):
    """Find the sum of the numbers that border symbols"""
    # Find the coordinates of symbols in the grid
    symbol_pattern = re.compile(r"([^\.a-zA-Z0-9\s])")
    symbol_grid = [
        (i, match.start())
        for (i, line) in enumerate(lines)
        for match in re.finditer(symbol_pattern, line)
    ]

    # Initialize pattern to find numbers
    number_pattern = re.compile(r"(\d+)")
    # Initialize delta pattern to find coordinates of neighboring cells
    neighbor_pattern = [
        delta for delta in it.product((-1, 0, 1), (-1, 0, 1)) if delta != (0, 0)
    ]
    # Search for each number, and look for neighboring symbols
    number_sum = 0
    for i, line in enumerate(lines):
        for number in re.finditer(number_pattern, line):
            found_part = False
            # Coordinates of cells occupied by this number
            occupied = [(i, j) for j in range(*number.span())]
            for cell in occupied:
                # Use delta pattern to find coordinates of neighboring cells
                for neighbor in it.starmap(
                    lambda x, y: (cell[0] + x, cell[1] + y), neighbor_pattern
                ):
                    # If this neighbor contains a symbol, add part to sum and move on
                    if neighbor in symbol_grid:
                        # print(f"{m.group(0)} bordering {neighbor} at {cell}")
                        found_part = True
                        break
                    if found_part:
                        break
            if found_part:
                number_sum += int(number.group(0))

    return number_sum
