from concurrent.futures import ThreadPoolExecutor

from process import PuzzleSolver


def main(lines: list[str]):
    with ThreadPoolExecutor(max_workers=16) as executor:
        dofs = executor.map(
            lambda line: PuzzleSolver(line).count_dof(),
            lines,
        )

    return sum(dofs)
