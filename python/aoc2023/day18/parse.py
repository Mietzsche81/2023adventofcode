def parse(input_file: str, *, hex: bool) -> tuple[list[tuple[int, int]], list[int]]:
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    lines = [stripped for line in lines if (stripped := line.strip())]
    # Part 2
    if hex:
        color = [line.split()[2].strip()[2:-1] for line in lines]
        decode = {
            "0": "R",
            "1": "D",
            "2": "L",
            "3": "U",
        }
        direction = [decode[c[-1]] for c in color]
        distance = [int(c[:-1], 16) for c in color]
    # Part 1
    else:
        direction = [line.split()[0].strip() for line in lines]
        distance = [int(line.split()[1]) for line in lines]

    return direction, distance


def instructions_to_sequence(direction, distance):
    encode = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }

    # Apply instructions sequentially
    location = (0, 0)
    sequence = [location]
    for u, d in zip(direction, distance):
        u = encode[u]
        location = (location[0] + d * u[0], location[1] + d * u[1])
        sequence.append(location)

    return sequence
