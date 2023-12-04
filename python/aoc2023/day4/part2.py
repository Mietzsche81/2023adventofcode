from typing import Dict, Set


def main(data: Dict[int, Dict[str, Set[int]]]):
    copies = {i: 1 for i in data}
    for i, card in data.items():
        won = len(card["winner"] & card["card"])
        for j in range(1, won + 1):
            copies[i + j] += copies[i]
    total = sum(copies.values())
    return total
