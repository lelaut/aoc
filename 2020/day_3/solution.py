"""
Solution to day 3 of Advent of Code
link: https://adventofcode.com/2020/day/3
"""


from typing import List


def traverse(world: List[str], right: int, down: int) -> int:
    counter = 0
    r = right

    for i in range(down, len(world), down):
        if world[i][r] == "#":
            counter += 1
        r = (r + right) % (len(world[0])-1)

    return counter


def part_1(world: List[str]) -> None:
    print("Part 1 solution %d" % traverse(world, 3, 1))


def part_2(world: List[str]) -> None:
    configs = [traverse(world, 1, 1), traverse(world, 3, 1),
               traverse(world, 5, 1), traverse(world, 7, 1),
               traverse(world, 1, 2)]
    print(configs)
    result = 1
    for config in configs:
        result *= config
    print("Part 2 solution %d" % result)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        world = [l for l in f.readlines()]
        part_1(world)
        part_2(world)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
