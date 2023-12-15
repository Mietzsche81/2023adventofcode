from parse import hash, parse_entry


def main(data: list[str]):
    box = [[] for _ in range(256)]
    for step in data:
        label, operation, focal = parse_entry(step)
        box_number = hash(label)
        if operation == "-":
            if label in [x[0] for x in box[box_number]]:
                box[box_number] = [x for x in box[box_number] if x[0] != label]
        elif operation == "=":
            i = next(
                (i for i, x in enumerate(box[box_number]) if x[0] == label),
                None,
            )
            if i is not None:
                box[box_number][i] = (label, int(focal))
            else:
                box[box_number].append((label, int(focal)))
        else:
            raise ValueError(f"Unknown operation {operation} in {step}")

    score = 0
    for box_number in range(len(box)):
        for i, lens in enumerate(box[box_number]):
            score += (box_number + 1) * (i + 1) * lens[1]

    return score
