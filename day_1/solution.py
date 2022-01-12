"""
Solution to day 1 of Advent of Code
link: https://adventofcode.com/2021/day/1
"""

from typing import List


def part_1(values: List[int]):
    counter = 0

    for i in range(len(values) - 1):
        if values[i+1] > values[i]:
            counter += 1

    print("Part 1 solution:", counter)


def part_2(values: List[int]):
    counter = 0

    for i in range(len(values) - 3):
        a_window = values[i]+values[i+1]+values[i+2]
        b_window = values[i+1]+values[i+2]+values[i+3]
        if b_window > a_window:
            counter += 1

    print("Part 2 solution:", counter)


def solve(input_path: str):
    with open(input_path, "r") as f:
        values = [int(l) for l in f.readlines()]
        part_1(values)
        part_2(values)


def main():
    print("With the small input")
    solve("small.txt")

    print("With the large input")
    solve("large.txt")


if __name__ == "__main__":
    main()
