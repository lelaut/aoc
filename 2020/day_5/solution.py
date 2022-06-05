"""
Solution to day 5 of Advent of Code
link: https://adventofcode.com/2020/day/5
"""


import math
from typing import List


def position(string: str, lowerhalf: str, limit: int) -> int:
    a = 0
    b = limit

    for s in string:
        if s == lowerhalf:
            b = (b-a) // 2 + a
        else:
            a = math.ceil((b-a) / 2 + a)

    return a


def evalsids(seats: List[str]) -> List[int]:
    sids = []

    for seat in seats:
        row = position(seat[:7], "F", 127)
        col = position(seat[7:], "L", 7)
        sids.append(row * 8 + col)

    return sids


def part_1(seats: List[str]) -> None:
    print("Part 1 solution %d" % max(evalsids(seats)))


def part_2(seats: List[str]) -> None:
    # !!ignore small data!!
    if len(seats) < 700:
        return

    sids = evalsids(seats)
    sids.sort()
    for i in range(len(sids)-1):
        if (sids[i+1] - sids[i]) == 2:
            print("Part 2 solution %d" % sids[i]+1)
            return


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        seats = f.readlines()
        part_1(seats)
        part_2(seats)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
