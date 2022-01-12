"""
Solution to day 2 of Advent of Code
link: https://adventofcode.com/2021/day/2
"""


from typing import List

HORIZONTAL = 0
DEPTH = 1
AIM = 2


def part_1(commands: List[str]) -> None:
    state = [0, 0]

    for command in commands:
        x = int(command.split(" ")[1])
        if command.startswith("down"):
            state[DEPTH] += x
        elif command.startswith("up"):
            state[DEPTH] -= x
        else:
            state[HORIZONTAL] += x

    print("Part 1 solution:", state[DEPTH] * state[HORIZONTAL])


def part_2(commands: List[str]) -> None:
    state = [0, 0, 0]

    for command in commands:
        x = int(command.split(" ")[1])
        if command.startswith("down"):
            state[AIM] += x
        elif command.startswith("up"):
            state[AIM] -= x
        else:
            state[HORIZONTAL] += x
            state[DEPTH] += state[AIM] * x

    print("Part 2 solution:", state[DEPTH] * state[HORIZONTAL])


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        commands = f.readlines()
        part_1(commands)
        part_2(commands)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
