"""
Solution to day 5 of Advent of Code
link: https://adventofcode.com/2021/day/5
"""


from __future__ import annotations
from typing import List
from math import sqrt


def sign(v: int) -> int:
    if v < 0:
        return -1
    elif v > 0:
        return 1
    return 0


class Point:
    def __init__(self, value: str) -> None:
        self.x, self.y = map(int, value.split(","))

    def __str__(self) -> str:
        return "(%d,%d)" % (self.x, self.y)

    def __eq__(self, __o: Point) -> bool:
        return self.x == __o.x and self.y == __o.y

    def sq_dst(self, x: int, y: int) -> float:
        return sqrt((self.x-x) ** 2 + (self.y-y) ** 2)


class Line:
    def __init__(self, value: str) -> None:
        a_str, b_str = value.split(" -> ")
        self.a = Point(a_str)
        self.b = Point(b_str)
        self.sq_size = self.a.sq_dst(self.b.x, self.b.y)

    def __str__(self) -> str:
        return "%s -> %s" % (str(self.a), str(self.b))

    def contains(self, x: int, y: int) -> bool:
        ac = self.a.sq_dst(x, y)
        cb = self.b.sq_dst(x, y)
        return abs(ac+cb - self.sq_size) < .00001

    def count_collision(self, other: Line, exclude: list) -> int:
        count = 0
        step = (sign(other.b.x - other.a.x), sign(other.b.y - other.a.y))
        current = [other.a.x, other.a.y]
        target = (other.b.x + step[0], other.b.y + step[1])

        while current[0] != target[0] or current[1] != target[1]:
            if self.contains(current[0], current[1]):
                point = (current[0], current[1])
                if not point in exclude:
                    count += 1
                    exclude.append(point)
            current[0] += step[0]
            current[1] += step[1]

        return count


def part_1(lines: List[Line]) -> None:
    count = 0
    exclude = []

    for i in range(len(lines) - 1):
        if lines[i].a.x == lines[i].b.x or lines[i].a.y == lines[i].b.y:
            for j in range(i+1, len(lines)):
                if lines[j].a.x == lines[j].b.x or lines[j].a.y == lines[j].b.y:
                    count += lines[i].count_collision(lines[j], exclude)

    print("Part 1 solution: %d" % count)


def part_2(lines: List[Line]) -> None:
    count = 0
    exclude = []

    for i in range(len(lines) - 1):
        for j in range(i+1, len(lines)):
            count += lines[i].count_collision(lines[j], exclude)

    print("Part 2 solution: %d" % count)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        lines = []
        for l in f.readlines():
            lines.append(Line(l))
        part_1(lines)
        part_2(lines)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
