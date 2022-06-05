"""
Solution to day 11 of Advent of Code
link: https://adventofcode.com/2021/day/11
"""


from copy import deepcopy
from typing import List


def flash(grid: List[List[int]], flashed: List[List[bool]], x: int, y: int) -> None:
    if flashed[y][x]:
        return 0
    flashed[y][x] = True
    counter = 1

    if x - 1 >= 0:
        grid[y][x-1] += 1
        if grid[y][x-1] > 9:
            counter += flash(grid, flashed, x-1, y)
    if x + 1 < len(grid[0]):
        grid[y][x+1] += 1
        if grid[y][x+1] > 9:
            counter += flash(grid, flashed, x+1, y)
    if y - 1 >= 0:
        grid[y-1][x] += 1
        if grid[y-1][x] > 9:
            counter += flash(grid, flashed, x, y-1)
    if y + 1 < len(grid):
        grid[y+1][x] += 1
        if grid[y+1][x] > 9:
            counter += flash(grid, flashed, x, y+1)

    if x - 1 >= 0:
        if y - 1 >= 0:
            grid[y-1][x-1] += 1
            if grid[y-1][x-1] > 9:
                counter += flash(grid, flashed, x-1, y-1)
        if y + 1 < len(grid):
            grid[y+1][x-1] += 1
            if grid[y+1][x-1] > 9:
                counter += flash(grid, flashed, x-1, y+1)
    if x + 1 < len(grid[0]):
        if y - 1 >= 0:
            grid[y-1][x+1] += 1
            if grid[y-1][x+1] > 9:
                counter += flash(grid, flashed, x+1, y-1)
        if y + 1 < len(grid):
            grid[y+1][x+1] += 1
            if grid[y+1][x+1] > 9:
                counter += flash(grid, flashed, x+1, y+1)

    return counter


def part_1(grid: List[List[int]]) -> None:
    flashed = [[False for _ in range(len(grid[y]))] for y in range(len(grid))]
    counter = 0

    for _ in range(100):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                grid[y][x] += 1

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9:
                    counter += flash(grid, flashed, x, y)

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9:
                    grid[y][x] = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                flashed[y][x] = False

    print("Part 1 solution %d" % counter)


def part_2(grid: List[List[int]]) -> None:
    flashed = [[False for _ in range(len(grid[y]))] for y in range(len(grid))]
    step = 1

    while True:
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                grid[y][x] += 1

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9:
                    flash(grid, flashed, x, y)

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9:
                    grid[y][x] = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                flashed[y][x] = False

        has_sync = True
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != grid[0][0]:
                    has_sync = False
                    break
            if not has_sync:
                break
        if has_sync:
            break

        step += 1

    print(grid)
    print("Part 2 solution %d" % step)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        grid = []
        for line in f.readlines():
            grid.append(list(map(int, line.rstrip())))
        part_1(deepcopy(grid))
        part_2(grid)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
