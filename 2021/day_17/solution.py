"""
Solution to day 17 of Advent of Code
link: https://adventofcode.com/2021/day/17
"""


from operator import contains
from typing import List

test = [23, -10, 25, -9, 27, -5, 29, -6, 22, -6, 21, -7, 9, 0, 27, -7, 24, -5, 25, -7, 26, -6, 25, -5, 6, 8, 11, -2, 20, -5, 29, -10, 6, 3, 28, -7, 8, 0, 30, -6, 29, -8, 20, -10, 6, 7, 6, 4, 6, 1, 14, -4, 21, -6, 26, -10, 7, -1, 7, 7, 8, -1, 21, -9, 6, 2, 20, -7, 30, -10, 14, -3, 20, -8, 13, -2, 7, 3, 28, -8, 29, -9, 15, -3, 22, -5, 26, -8, 25, -8, 25, -6, 15, -4, 9, -2, 15, -2, 12, -2, 28, -9, 12, -3, 24, -6, 23, -7, 25, -10, 7, 8, 11, -3, 26, -7, 7, 1, 23, -9, 6, 0, 22, -10, 27, -6, 8, 1, 22, -8, 13, -4, 7, 6, 28, -6, 11, -4, 12, -4, 26, -9, 7, 4, 24, -10, 23, -8, 30, -8, 7, 0, 9, -1, 10, -1, 26, -5, 22, -9, 6, 5, 7, 5, 23, -6, 28, -10, 10, -2, 11, -1, 20, -9, 14, -2, 29, -7, 13, -3, 23, -5, 24, -8, 27, -9, 30, -7, 28, -5, 21, -10, 7, 9, 6, 6, 21, -5, 27, -10, 7, 2, 30, -9, 21, -8, 22, -7, 24, -9, 20, -6, 6, 9, 29, -5, 8, -2, 27, -8, 30, -5, 24, -7
        ]


def simulate(tx: List[int], ty: List[int], fx: int, fy: int) -> int:
    s = 1
    px = 0
    py = 0

    while fy >= 0 or py >= ty[0]:
        px += fx
        py += fy

        if px >= tx[0] and px <= tx[1] and py >= ty[0] and py <= ty[1]:
            return s

        fy -= 1
        if fx != 0:
            fx = fx - 1 if fx > 0 else fx + 1
        s += 1

    return -1


def part_1(tx: List[int], ty: List[int]) -> None:
    y = abs(ty[0]) - 1
    ymax = (y**2+y)/2
    print("Part 1 solution %d" % ymax)


def part_2(tx: List[int], ty: List[int]) -> None:
    ry = [ty[0], abs(ty[0]) - 1]
    rx = tx[1]
    c = 0

    for y in range(ry[0], ry[1]+1):
        for x in range(1, rx+1):
            if simulate(tx, ty, x, y) >= 0:
                c += 1

    print("Part 2 solution %d" % c)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        line = f.readline()
        xi = line.index("x=")
        yi = line.index("y=")
        tx = list(map(int, line[xi+2:yi-2].split("..")))
        ty = list(map(int, line[yi+2:].split("..")))
        part_1(tx, ty)
        part_2(tx, ty)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
