import re
from typing import List


def main(data: List[str]):
    """Parse each line for the first and last digits represented"""

    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    numbers = list(range(0, 10))

    # Create a map reading digits both numerically and lexically
    forward_map: dict = {
        **dict(zip([str(n) for n in numbers], numbers)),
        **dict(zip(words, numbers)),
    }
    # Also read these map backwards, such that shared letters in words are detected:
    # i.e. regex backwards so that 1eightwo returns "two" as last, not eight, which
    #      would steal the 't' from the two
    backward_map: dict = dict(
        zip([key[::-1] for key in forward_map.keys()], forward_map.values())
    )
    # Precompile for performance
    forward_pattern = re.compile(f"({'|'.join(forward_map.keys())})")
    backward_pattern = re.compile(f"({'|'.join(backward_map.keys())})")

    sum = 0
    for line in data:
        # First digit is the 10s value
        match = re.search(forward_pattern, line).group(0)
        sum += 10 * forward_map[match]
        # Second digit is the 1s value
        match = re.search(backward_pattern, line[::-1]).group(0)
        sum += backward_map[match]

    return sum
