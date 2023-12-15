import re


def parse(input_file):
    with open(input_file, "r") as fin:
        lines = fin.read()
    data = lines.replace("\n", "").strip().split(",")
    return data


def hash(s: str):
    value = 0
    for i in s:
        value += ord(i)
        value *= 17
        value %= 256

    return value


def parse_entry(entry):
    label, operation, focal = re.match("([a-zA-z]+)(=|-)(\d+)?", entry).groups()
    return label, operation, focal
