"""
Solution to day 15 of Advent of Code
link: https://adventofcode.com/2021/day/15
"""


from typing import Any, List, Tuple


def neighbours(x: int, y: int, visited: List[List[bool]]) -> List[Tuple[int, int]]:
    n = []

    if x - 1 >= 0 and not visited[y][x-1]:
        n.append((x-1, y))
    if x + 1 < len(visited[0]) and not visited[y][x+1]:
        n.append((x+1, y))
    if y - 1 >= 0 and not visited[y-1][x]:
        n.append((x, y-1))
    if y + 1 < len(visited) and not visited[y+1][x]:
        n.append((x, y+1))

    return n


def findrisk(cave: List[List[int]]) -> int:
    x, y, g = 0, 0, 0
    visited = [[False for _ in range(len(cave[0]))] for _ in range(len(cave))]
    visiting = []

    while y != len(cave) - 1 or x != len(cave[0]) - 1:
        visited[y][x] = True
        for neighbour in neighbours(x, y, visited):
            gcost = g + cave[neighbour[1]][neighbour[0]]
            visiting.append((gcost, neighbour))
            visited[neighbour[1]][neighbour[0]] = True
        visiting.sort(reverse=True)
        last = visiting.pop()
        g = last[0]
        x, y = last[1]

    return g


def part_1(cave: List[List[int]]) -> None:
    print("Part 1 solution %d" % findrisk(cave))


def part_2(cave: List[List[int]]) -> None:
    xlen, ylen = len(cave[0]), len(cave)

    for i in range(5):
        for y in range(ylen):
            newpart = []
            xlim = xlen*4 if i == 0 else xlen*5
            for x in range(xlim):
                value = cave[y][x % xlen] + \
                    (x // xlen + (1 if i == 0 else 0)) + i
                if value > 9:
                    value = value % 9
                newpart.append(value)
            if i == 0:
                for np in newpart:
                    cave[y].append(np)
            else:
                cave.append(newpart)

    print("Part 2 solution %d" % findrisk(cave))


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        cave: List[List[int]] = []
        for line in f.readlines():
            cave.append(list(map(int, line.rstrip())))
        part_1(cave)
        part_2(cave)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
