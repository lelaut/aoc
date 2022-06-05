"""
Solution to day 10 of Advent of Code
link: https://adventofcode.com/2021/day/10
"""


from typing import List


def part_1(lines: List[str]) -> None:
    opener = ["(", "[", "{", "<"]
    closer = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    path = []
    score = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in opener:
                path.append(lines[i][j])
            else:
                if lines[i][j] in closer:
                    if closer[lines[i][j]] != path[-1]:
                        score += points[lines[i][j]]
                    path.pop()
        path.clear()

    print("Part 1 solution %d" % score)


def part_2(lines: List[str]) -> None:
    opener = ["(", "[", "{", "<"]
    closer = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    toClose = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    path = []
    score = []

    # {([(<{}[<>[]}>{[]{[(<()>
    for i in range(len(lines)):
        corrupted = False
        for j in range(len(lines[i])):
            if lines[i][j] in opener:
                path.append(lines[i][j])
            else:
                if lines[i][j] in closer:
                    if closer[lines[i][j]] != path[-1]:
                        corrupted = True
                        break
                    path.pop()
        if corrupted:
            path.clear()
            continue

        path = list(map(lambda c: toClose[c], path))
        path.reverse()
        total = 0
        for c in path:
            total = total * 5 + points[c]
        score.append(total)

        path.clear()

    score.sort()
    print("Part 2 solution %d" % score[len(score) // 2])


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        lines = f.readlines()
        part_1(lines)
        part_2(lines)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
