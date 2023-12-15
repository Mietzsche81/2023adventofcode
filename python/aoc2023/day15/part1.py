from parse import hash


def main(data: list[str]):
    sum = 0
    for step in data:
        sum += hash(step)

    return sum
