def parse(input_file: str) -> list[dict[str, list[str] | int]]:
    with open(input_file, "r") as fin:
        lines = fin.readlines()

    hands: list[dict[str, list[str] | int]] = [
        {"cards": cards, "bid": int(bid)}
        for cards, bid in (line.strip().split() for line in lines)
    ]
    return hands
