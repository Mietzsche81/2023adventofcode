import numpy as np
import numpy.typing as nptype


class Grid:
    """Parses the ASCII map into a grid of pipes"""

    # Encode ASCII characters as ints for speed
    encoder = {c: i for i, c in enumerate(".|-LJ7FS")}
    decoder = {i: c for c, i in encoder.items()}

    # Relative cardinal directions
    dir = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
    }

    @classmethod
    def dirs(cls, s):
        return [cls.dir[x] for x in s.strip()]

    def __init__(self, input_file: str):
        """Parse input_file and instantiate `Grid` variables"""
        # Map coordinate delta's from shape
        self._delta_from_current = {
            "|": self.dirs("NS"),
            "-": self.dirs("EW"),
            "L": self.dirs("EN"),
            "J": self.dirs("NW"),
            "7": self.dirs("SW"),
            "F": self.dirs("ES"),
            "S": self.dirs("ENSW"),
        }
        # Map shape from attached neighboring pipes
        self._shape_from_path = {
            "NS": "|",
            "EW": "-",
            "EN": "L",
            "NW": "J",
            "SW": "7",
            "ES": "F",
            "ENSW": "S",
        }
        # Map neighboring pipes shapes that are valid for attaching
        self._valid_attach = {
            self.dir["N"]: "S|7F",
            self.dir["S"]: "S|JL",
            self.dir["W"]: "S-FL",
            self.dir["E"]: "S-J7",
        }

        # Parse input
        with open(input_file, "r") as fin:
            lines = fin.readlines()

        # Convert raw ascii grid
        self.grid: nptype.NDArray[np.int32] = np.array(self.encode(lines))
        # Initialize empty loop
        self.loop = None

    def shape(self):
        return self.grid.shape

    def encode(self, unencoded):
        """Convert ASCII shape to numeric encoding"""
        if isinstance(unencoded, str) and len(unencoded.strip()) == 1:
            return self.encoder[unencoded]
        if isinstance(unencoded, str):
            return [self.encoder[x] for x in unencoded.strip()]
        else:
            return [self.encode(row) for row in unencoded]

    def decode(self, encoded):
        """Convert numeric encoding to ASCII shape"""
        if isinstance(encoded[0], (int, np.int32, np.int64)):
            return "".join(self.decoder[x] for x in encoded)
        else:
            return [self.decode(row) for row in encoded]

    def find_valid_attach(self, cell):
        """Find neighboring cells with valid attachments"""
        return [
            abs
            for rel in self._delta_from_current[self.decoder[self.grid[*cell]]]
            if self.decoder[self.grid[*(abs := cell + rel)]] in self._valid_attach[rel]
        ]

    def advance(self, previous, current):
        """Return the coordinates of the next cell attached to the `current`

        Calculates next cell from current using previous to imply direction
        """
        delta = current - previous
        match self.decoder[self.grid[*current]]:
            case "|":
                if delta[0] > 0:
                    return current + [1, 0]
                else:
                    return current - [1, 0]
            case "-":
                if delta[1] > 0:
                    return current + [0, 1]
                else:
                    return current - [0, 1]
            case "L":
                if delta[0] > 0:
                    return current + [0, 1]
                else:
                    return current - [1, 0]
            case "J":
                if delta[0] > 0:
                    return current - [0, 1]
                else:
                    return current - [1, 0]
            case "7":
                if delta[1] > 0:
                    return current + [1, 0]
                else:
                    return current - [0, 1]
            case "F":
                if delta[1] < 0:
                    return current + [1, 0]
                else:
                    return current + [0, 1]

    def find_loop(self):
        """From the start location denoted by `S`, find the loop of attachments"""
        # start location
        self.start = np.argwhere(self.grid == self.encoder["S"])[0]
        possible_path = [
            [self.start, forward] for forward in self.find_valid_attach(self.start)
        ]

        # Iteratively solve for loop
        self.loop = None
        while not self.loop:
            # For each possible path from start
            for i, path in enumerate(possible_path):
                # Attempt to advance
                forward = self.advance(*path[-2:])
                if (forward == self.find_valid_attach(path[-1])).all(axis=1).any():
                    path.append(forward)
                else:
                    del possible_path[i]
                    continue

                # Full loop?
                if (path[-1] == self.start).all():
                    self.loop = path[:-1]
                    break

        # Replace start type with equivalent shape
        section = [self.loop[1] - self.start, self.loop[-1] - self.start]
        dir_symbols = {d: i for i, d in self.dir.items()}
        shape = self._shape_from_path[
            "".join(sorted(dir_symbols[tuple(d)] for d in section))
        ]
        self.grid[*self.start] = self.encoder[shape]

        return self.loop

    def find_enclosed(self):
        """Find enclosed via 'wall parity'

        The edges of the grid are definitely outside. Therefore, when scanning
        horizontally, each vertical wall will change the 'parity' of the cell
        (e.g., inside vs outside status).

        NOTE: for corners, must exclusively count only lower corners (L|J) or
              only upper corners (F|7), NOT BOTH. This is because a pair of
              vertically like corners will define a contour of a wall, vs a
              pair of vertically unlike corners (i.e. one upper corner, one
              lower corner) only defines an inflection

              E.g.,

              .......F---7.......
              .......|xxx|.......
              .....F-JxxxL-7.....
              .....|xxxxxxx|.....
              .....|xxxxxxx|.....
        """
        if not self.loop:
            self.find_loop()

        self.walls = np.zeros_like(self.grid)
        for loc in self.loop:
            self.walls[*loc] = 1

        self.enclosed = np.zeros_like(self.grid)
        for row in range(self.shape()[0]):
            internal = False
            for col in range(self.shape()[1]):
                if self.walls[row, col]:
                    if self.decoder[self.grid[row, col]] in "|JL":
                        internal = not internal
                else:
                    self.enclosed[row, col] = internal

        return self.enclosed.sum()
