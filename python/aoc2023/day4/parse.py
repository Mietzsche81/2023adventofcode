import re
from typing import Dict, Set


def parse(input_file) -> Dict[int, Dict[str, Set[int]]]:
    with open(input_file, "r") as fin:
        lines = fin.readlines()

    pattern_split = re.compile(r"[:|]")
    pattern_key = re.compile(r"Card\s+(\d+)")

    cards = {
        int(re.match(pattern_key, key).group(1)): {
            "winner": {int(x) for x in winner.split()},
            "card": {int(x) for x in card.split()},
        }
        for key, winner, card in (
            re.split(pattern_split, line) for line in lines if not line.isspace()
        )
    }

    return cards
