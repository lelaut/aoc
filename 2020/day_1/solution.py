"""
Solution to day 1 of Advent of Code
link: https://adventofcode.com/2020/day/1
"""


from typing import List


def part_1(report: List[int]) -> None:
    for i in range(len(report)):
        for j in range(i+1, len(report)):
            if report[i]+report[j] == 2020:
                print("Part 1 solution %d" % (report[i]*report[j]))
                return


def part_2(report: List[int]) -> None:
    for i in range(len(report)):
        for j in range(i+1, len(report)):
            for k in range(j+1, len(report)):
                if report[i]+report[j]+report[k] == 2020:
                    print("Part 2 solution %d" %
                          (report[i]*report[j]*report[k]))
                    return


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        report = list(map(int, [l.rstrip() for l in f.readlines()]))
        part_1(report)
        part_2(report)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
