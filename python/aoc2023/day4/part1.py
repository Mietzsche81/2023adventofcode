from typing import Dict, Set


def main(data: Dict[int, Dict[str, Set[int]]]):
    points = 0
    for card in data.values():
        points += int(2 ** (len(card["winner"] & card["card"]) - 1))

    return points
