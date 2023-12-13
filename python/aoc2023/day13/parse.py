def parse(input_file):
    with open(input_file, "r") as fin:
        data = fin.read()
    patterns = [stripped for p in data.split("\n\n") if (stripped := p.strip())]
    return patterns
