from collections import Counter


def main(hands):
    # Enumerate value of cards in order
    tokens = ["J"] + list(str(token) for token in range(2, 10)) + ["T", "Q", "K", "A"]
    card_value = {x: i for i, x in enumerate(tokens)}

    for hand in hands:
        # Count matches
        hand["rank"] = Counter(hand["cards"])
        # If all jokers, leave as is (lowest value 5-kind)
        if hand["cards"] == "J" * len(hand["cards"]):
            pass
        # If joker in hand...
        elif "J" in hand["cards"]:
            # Count number of jokers, remove from hand
            jokers = hand["rank"].pop("J")
            # Find most common card (besides joker)
            most_common_card = hand["rank"].most_common(1)[0][0]
            # Cast jokers as most common card
            hand["rank"][most_common_card] += jokers
        # Arrive at tallies of matches in hand
        hand["rank"] = sorted(hand["rank"].values(), reverse=True)

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
