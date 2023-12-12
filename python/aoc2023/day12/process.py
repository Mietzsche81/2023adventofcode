from dataclasses import dataclass


def parse(input_file):
    """Read the input file into separate lines, stripping whitespace"""
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    return [stripped for line in lines if (stripped := line.strip())]


class PuzzleSolver:
    """Converts the input `line` into a puzzle grid and list of clues

    Count degrees of freedom in the puzzle via `count_dof` method
    """

    @dataclass(frozen=True)
    class Cursor:
        """
        A hashable, cachable state for scanning the puzzle
        """

        # puzzle index
        position: int = 0
        # clue index
        clue_index: int = 0
        # Running size of block under cursor (i.e. block containing `position`)
        current_block_size: int = 0

        def ignore_under_cursor(self):
            """When encountering ordinary ., move on"""
            return PuzzleSolver.Cursor(self.position + 1, self.clue_index, 0)

        def end_block(self):
            """When encountering . after #, iterate on clue index"""
            return PuzzleSolver.Cursor(self.position + 1, self.clue_index + 1, 0)

        def add_cursor_to_block(self):
            """When encountering # after #, iterate block size"""
            return PuzzleSolver.Cursor(
                self.position + 1, self.clue_index, self.current_block_size + 1
            )

    def __init__(self, line, repeats=1):
        self.grid, self.clue = (
            "?".join([(section := line.split())[0].strip()] * repeats),
            [int(clue) for clue in section[1].strip().split(",")] * repeats,
        )
        # Remove trailing, leading nulls. Reduce repeating nulls (equivalent puzzle)
        self.grid = ".".join([block for block in self.grid.split(".") if block])

    def count_dof(self) -> int:
        """Count all possible configurations that could solve the puzzle"""
        # Cache results for performance
        self._cache = {}
        # Iterate
        return self._count_dof(PuzzleSolver.Cursor())

    def _count_dof(
        self,
        state: Cursor,
    ) -> int:
        # If previously reached this fork when traversing state, use cached result.
        if state in self._cache:
            return self._cache[state]
        # If reached end of grid and...
        if state.position == len(self.grid):
            # ... completed all clues, and no further blocks found
            if state.clue_index == len(self.clue) and state.current_block_size == 0:
                # Valid
                return 1
            # ... just completed last clue
            elif (
                state.clue_index == (len(self.clue) - 1)
                and self.clue[state.clue_index] == state.current_block_size
            ):
                return 1
            # ... incomplete clue or extraneous block found
            else:
                return 0
        # Initialize search for downstream possibilities
        possible = 0
        if self.grid[state.position] == "?":
            if state.current_block_size == 0:
                # Treat ? as . between blocks, skip
                possible += self._count_dof(state.ignore_under_cursor())
            elif (
                state.clue_index < len(self.clue)
                and self.clue[state.clue_index] == state.current_block_size
            ):
                # Treat ? as . ending of current block
                possible += self._count_dof(state.end_block())
            # Treat ? as #
            possible += self._count_dof(state.add_cursor_to_block())
        elif self.grid[state.position] == ".":
            if state.current_block_size == 0:
                # . between blocks, skip
                possible += self._count_dof(state.ignore_under_cursor())
            elif (
                state.clue_index < len(self.clue)
                and self.clue[state.clue_index] == state.current_block_size
            ):
                # . ending of current block
                possible += self._count_dof(state.end_block())
        elif self.grid[state.position] == "#":
            # Add # to current block
            possible += self._count_dof(state.add_cursor_to_block())
        else:
            raise ValueError(f"Invalid Symbol'{self.grid[state.position]}'")
        self._cache[state] = possible
        return possible
