"""
Solution to day 14 of Advent of Code
link: https://adventofcode.com/2021/day/14
"""


from typing import Dict


def part_1(initial: str, rules: Dict[str, str]) -> None:
    polymer = initial

    for _ in range(40):
        next_polymer = ""
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            if pair in rules:
                next_polymer += polymer[i] + rules[pair]
            else:
                next_polymer += polymer[i]
        polymer = next_polymer + polymer[-1]

    pmin = len(polymer)
    pmax = 0
    for i in range(ord("A"), ord("Z")+1):
        counter = polymer.count(chr(i))
        if counter > pmax:
            pmax = counter
        elif counter > 0 and counter < pmin:
            pmin = counter

    print("Part 1 solution is %d" % (pmax - pmin))


def part_2(initial: str, rules: Dict[str, str]) -> None:
    pass


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        lines = f.readlines()
        initial = lines[0].rstrip()
        rules = {}
        for i in range(2, len(lines)):
            line = lines[i].split(" -> ")
            rules[line[0]] = line[1].rstrip()
        part_1(initial, rules)
        part_2(initial, rules)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
