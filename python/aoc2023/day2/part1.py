from typing import Dict, List


def main(data: Dict[int, List[Dict[str, int]]]):
    max_visible: Dict[str, int] = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    sum = 0
    for id, sets in data.items():
        print(id, sets)
        max_seen = {
            color: max([draw.get(color, 0) for draw in sets]) for color in max_visible
        }
        if all([max_seen[color] <= max_visible[color] for color in max_visible]):
            sum += id
    return sum
