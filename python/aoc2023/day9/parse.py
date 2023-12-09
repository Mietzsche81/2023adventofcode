def parse(input_file) -> list[list[int]]:
    with open(input_file, "r") as fin:
        lines = fin.readlines()
    histories = [[int(x) for x in line.strip().split()] for line in lines]
    return histories
