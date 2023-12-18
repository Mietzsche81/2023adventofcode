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
