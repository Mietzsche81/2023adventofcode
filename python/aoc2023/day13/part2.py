def find_smudge(grid: list[str]):
    for i in range(1, len(grid)):
        gen = zip(grid[:i][::-1], grid[i:])
        if sum(b_i != a_i for b, a in gen for b_i, a_i in zip(b, a)) == 1:
            return i


def main(patterns: list[str]):
    score = 0
    for pattern in patterns:
        # Horizontal
        grid = [stripped for line in pattern.split() if (stripped := line.strip())]
        if index := find_smudge(grid):
            score += 100 * index
            continue
        # Vertical
        grid = ["".join(col) for col in list(map(list, zip(*grid)))]
        if index := find_smudge(grid):
            score += index
            continue
        # Failed to find
        raise ValueError("Did not find reflection")

    return score
