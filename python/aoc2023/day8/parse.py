import re


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()

    steps: list[int] = [0 if x == "L" else 1 for x in lines[0].strip()]

    pattern = re.compile(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)")
    paths: dict[str, tuple(str, str)] = {
        a: (l, r)
        for (a, l, r) in (
            re.search(pattern, line.strip()).groups()
            for line in lines[1:]
            if line.strip()
        )
    }

    return steps, paths
