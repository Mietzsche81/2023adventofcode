from collections import Counter


def main(hands):
    # Enumerate value of cards in order
    tokens = list(str(token) for token in range(2, 10)) + ["T", "J", "Q", "K", "A"]
    card_value = {x: i for i, x in enumerate(tokens)}

    for hand in hands:
        # Count matches
        hand["rank"] = sorted(
            Counter(hand["cards"]).values(),
            reverse=True,
        )

    # Sort first by matches, tiebreak by value of cards in order
    hands = sorted(
        hands,
        key=lambda d: (
            d["rank"],
            [card_value[x] for x in d["cards"]],
        ),
    )

    # Sum winnings
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand["bid"]

    return winnings
