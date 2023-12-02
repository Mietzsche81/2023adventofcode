import re


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    games = {
        i: [
            {
                cubes[1]: int(cubes[0])
                for cubes in [
                    color.split(" ") for color in [c.strip() for c in colors.split(",")]
                ]
            }
            for colors in [sets for sets in game.split(":")[1].strip().split(";")]
        ]
        for i, game in enumerate(lines, 1)
    }
    return games
