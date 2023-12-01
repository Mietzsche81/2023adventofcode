from typing import List


def main(data: List[str]):
    sum = 0
    for line in data:
        for char in line:
            if char.isdigit():
                sum += 10 * int(char)
                break
        for char in line[::-1]:
            if char.isdigit():
                sum += int(char)
                break
    return sum
