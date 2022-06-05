"""
Solution to day 3 of Advent of Code
link: https://adventofcode.com/2021/day/3
"""


from typing import List

ZERO_ORD = ord('0')


def part_1(values: List[str]) -> None:
    counter = [[0, 0] for _ in range(len(values[0]) - 1)]

    for value in values:
        for i in range(len(value) - 1):
            counter[i][ord(value[i]) - ZERO_ORD] += 1

    gamma = 0
    for i in range(len(counter)):
        if counter[i][1] > counter[i][0]:
            gamma += 2 ** (len(counter) - i - 1)
    mask = 2 ** len(counter) - 1
    epsilon = (~gamma) & mask

    print("Part 1 solution: %d * %d = %d" % (gamma, epsilon, gamma*epsilon))


def part_2(values: List[str]) -> None:
    n = len(values[0]) - 1
    oxygen_values = values.copy()
    co2_values = values.copy()
    for i in range(n):
        if len(oxygen_values) > 1:
            counter = [0, 0]
            for value in oxygen_values:
                counter[ord(value[i]) - ZERO_ORD] += 1
            if counter[0] > counter[1]:
                oxygen_values = [oxygen_values[j]
                                 for j in range(len(oxygen_values)) if oxygen_values[j][i] == '0']
            else:
                oxygen_values = [oxygen_values[j]
                                 for j in range(len(oxygen_values)) if oxygen_values[j][i] == '1']

        if len(co2_values) > 1:
            counter = [0, 0]
            for value in co2_values:
                counter[ord(value[i]) - ZERO_ORD] += 1
            if counter[1] < counter[0]:
                co2_values = [co2_values[j]
                              for j in range(len(co2_values)) if co2_values[j][i] == '1']
            else:
                co2_values = [co2_values[j]
                              for j in range(len(co2_values)) if co2_values[j][i] == '0']

    oxygen_rate = int(oxygen_values[0], 2)
    co2_rate = int(co2_values[0], 2)
    print("Part 2 solution: %d * %d = %d" %
          (oxygen_rate, co2_rate, oxygen_rate * co2_rate))


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        values = f.readlines()
        part_1(values)
        part_2(values)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
