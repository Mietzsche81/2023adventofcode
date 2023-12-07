from argparse import ArgumentParser
from collections import Counter

arg_parser = ArgumentParser()
arg_parser.add_argument("input", type=str)

args = arg_parser.parse_args()
input_file = args.input

with open(input_file, "r") as fin:
    lines = fin.readlines()

card_value = list(str(x) for x in range(2, 10)) + ["T", "J", "Q", "K", "A"]
card_value = {x: i + 2 for i, x in enumerate(card_value)}

hands = [{"cards": [card_value[x] for x in l.split()[0]]} for l in lines]
bids = [int(l.split()[1]) for l in lines]

for i, hand in enumerate(hands):
    freq = Counter(hand["cards"])
    hands[i]["rank"] = sorted(freq.values(), reverse=True)
    hands[i]["bid"] = bids[i]

hands = sorted(hands, key=lambda d: (d["rank"], d["cards"]))

winnings = 0
for i, hand in enumerate(hands):
    winnings += (i + 1) * hand["bid"]

print(winnings)
