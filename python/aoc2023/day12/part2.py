from concurrent.futures import ThreadPoolExecutor

from process import PuzzleSolver


def main(lines: list[str]):
    with ThreadPoolExecutor() as executor:
        dofs = executor.map(
            lambda line: PuzzleSolver(line, repeats=5).count_dof(),
            lines,
        )

    return sum(dofs)
