import itertools as it
import math
import re
from typing import List, Tuple

import numpy as np


def main(lines: List[str]):
    """
    Find the sum
        of the products (gear ratio)
            of each pair of exactly two numbers (gears)
                that border a gear (*)
    """
    # Find the coordinates of symbols in the grid
    gear_pattern = re.compile(r"(\*)")
    gear_grid: List[Tuple[int, int]] = [
        (i, match.start())
        for (i, line) in enumerate(lines)
        for match in re.finditer(gear_pattern, line)
    ]

    # Initialize delta pattern to find coordinates of neighboring cells
    neighbor_pattern = [delta for delta in it.product((-1, 0, 1), (-1, 0, 1))]
    # Initialize pattern to find numbers
    number_pattern = re.compile(r"(\d+)")

    # Check each gear for neighbors
    number_sum = 0
    for gear in gear_grid:
        # Initialize matching net
        values = []
        neighbors = np.array(
            [
                lines[row][col].isdigit() if (row, col) != gear else False
                for row, col in it.starmap(
                    lambda dx, dy: (gear[0] + dx, gear[1] + dy), neighbor_pattern
                )
            ]
        ).reshape(3, 3)

        # left
        if neighbors[1][0]:
            values.append(
                int(
                    re.findall(
                        number_pattern,
                        lines[gear[0]][: gear[1]],
                    )[-1]
                )
            )

        # right
        if neighbors[1][2]:
            values.append(
                int(
                    re.findall(
                        number_pattern,
                        lines[gear[0]][gear[1] + 1 :],
                    )[0]
                )
            )

        # top
        if np.array_equal(neighbors[0], [True, False, True]):
            values.append(
                int(
                    re.findall(
                        number_pattern,
                        lines[gear[0] - 1][: gear[1]],
                    )[-1]
                )
            )
            values.append(
                int(
                    re.findall(
                        number_pattern,
                        lines[gear[0] - 1][gear[1] + 1 :],
                    )[0]
                )
            )
        elif neighbors[0].any():
            span = {x for x in range(gear[1] - 1, gear[1] + 2)}
            for number in re.finditer(number_pattern, lines[gear[0] - 1]):
                if span.intersection({x for x in range(*number.span())}):
                    values.append(int(number.group(0)))
                    break

        # bottom
        if np.array_equal(neighbors[2], [True, False, True]):
            values.append(
                int(
                    re.findall(
                        number_pattern,
                        lines[gear[0] + 1][: gear[1]],
                    )[-1]
                )
            )
            values.append(
                int(
                    re.findall(
                        number_pattern,
                        lines[gear[0] + 1][gear[1] + 1 :],
                    )[0]
                )
            )
        elif neighbors[2].any():
            span = {x for x in range(gear[1] - 1, gear[1] + 2)}
            for number in re.finditer(number_pattern, lines[gear[0] + 1]):
                if span.intersection({x for x in range(*number.span())}):
                    values.append(int(number.group(0)))
                    break

        # Sum
        if len(values) == 2:
            print(
                f"Gear at {gear} bordering {values} for a value of {math.prod(values)}"
            )
            number_sum += math.prod(values)

    return number_sum
