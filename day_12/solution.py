"""
Solution to day 12 of Advent of Code
link: https://adventofcode.com/2021/day/12
"""


from typing import Dict, List


def count_paths(path: List[str], cave: Dict[str, List[str]], exclude) -> int:
    counter = 0

    for neighbour in cave[path[-1]]:
        if neighbour == "end":
            counter += 1
        elif not exclude(neighbour, path):
            counter += count_paths(path + [neighbour], cave, exclude)

    return counter


def part_1(cave: Dict[str, List[str]]) -> None:
    def isexclude(position: str, path: List[str]):
        return position.islower() and position in path

    solution = count_paths(["start"], cave, isexclude)
    print("Part 1 solution %d" % solution)


def part_2(cave: Dict[str, List[str]]) -> None:
    def isexclude(position: str, path: List[str]):
        if position == "start":
            return True
        if position.islower() and position in path:
            for position in path:
                if position.islower() and path.count(position) == 2:
                    return True
            return False
        return False

    solution = count_paths(["start"], cave, isexclude)
    print("Part 2 solution %d" % solution)


def connect(cave: Dict[str, List[str]], a: str, b: str) -> None:
    if a in cave:
        cave[a].append(b)
    else:
        cave[a] = [b]
    if b in cave:
        cave[b].append(a)
    else:
        cave[b] = [a]


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        cave: Dict[str, List[str]] = {}
        for line in f.readlines():
            a, b = line.split("-")
            connect(cave, a, b.rstrip())
        part_1(cave)
        part_2(cave)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
