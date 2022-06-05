"""
Solution to day 2 of Advent of Code
link: https://adventofcode.com/2020/day/2
"""


def part_1(records: list) -> None:
    counter = 0

    for record in records:
        limit, letter, password = record
        c = password.count(letter)
        if c >= limit[0] and c <= limit[1]:
            counter += 1

    print("Part 1 solution %d" % counter)


def part_2(records: list) -> None:
    counter = 0

    for record in records:
        positions, letter, password = record
        c = password.count(letter)
        if (password[positions[0]-1] == letter) ^ (password[positions[1]-1] == letter):
            counter += 1

    print("Part 2 solution %d" % counter)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        records = []
        for line in f.readlines():
            policy, password = line.split(": ")
            values, letter = policy.split()
            records.append((list(map(int, values.split("-"))),
                            letter, password.rstrip()))
        part_1(records)
        part_2(records)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
