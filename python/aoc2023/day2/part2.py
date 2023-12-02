from typing import Dict, List

import numpy as np


def main(data: Dict[int, List[Dict[str, int]]]):
    sum = 0
    colors = ["red", "green", "blue"]
    for id, sets in data.items():
        print(id, sets)
        max_seen = {
            color: max([draw.get(color, 0) for draw in sets]) for color in colors
        }
        sum += np.product(list(max_seen.values()))
    return sum
