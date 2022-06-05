"""
Solution to day 6 of Advent of Code
link: https://adventofcode.com/2021/day/6
"""


from typing import List


def simulate_lanternfishes(initial_state: List[int], days: int) -> List[int]:
    fish_groups = [0 for _ in range(9)]
    for value in initial_state:
        fish_groups[value] += 1

    for _ in range(days):
        new_born = 0
        new_cycle = 0
        if fish_groups[0] > 0:
            new_born = fish_groups[0]
            new_cycle = fish_groups[0]
        for i in range(8):
            fish_groups[i] = fish_groups[i+1]
        fish_groups[6] += new_cycle
        fish_groups[8] = new_born

    return fish_groups


def part_1(values: List[int]) -> None:
    total = sum(simulate_lanternfishes(values, 80))
    print("Part 1 solution: %d" % total)


def part_2(values: List[int]) -> None:
    total = sum(simulate_lanternfishes(values, 256))
    print("Part 2 solution: %d" % total)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        values = list(map(int, f.readline().split(",")))
        part_1(values)
        part_2(values)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
