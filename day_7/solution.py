"""
Solution to day 7 of Advent of Code
link: https://adventofcode.com/2021/day/7
"""


from typing import List


def basic_fuel_cost(positions: List[int], target: int) -> int:
    cost = 0
    for position in positions:
        cost += abs(position - target)
    return cost


def complex_fuel_cost(positions: List[int], target: int) -> int:
    cost = 0
    for position in positions:
        d = abs(position - target)
        cost += (d + 1) * d // 2
    return cost


def binary_search(values: List[int], fcost):
    a = min(values)
    b = max(values)

    while a != b:
        m = (b-a) // 2 + a
        mfuel = fcost(values, m)
        amfuel = fcost(values, m-1)
        bmfuel = fcost(values, m+1)

        if amfuel < mfuel:
            b = m
        elif bmfuel < mfuel:
            a = m
        else:
            break

    return mfuel


def part_1(values: List[int]) -> None:
    fuel_cost = binary_search(values, basic_fuel_cost)
    print("Part 1 solution: %d fuel cost" % fuel_cost)


def part_2(values: List[int]) -> None:
    fuel_cost = binary_search(values, complex_fuel_cost)
    print("Part 2 solution: %d fuel cost" % fuel_cost)


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
