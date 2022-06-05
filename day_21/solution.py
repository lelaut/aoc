"""
Solution to day 21 of Advent of Code
link: https://adventofcode.com/2021/day/21
"""


def part_1(p1: int, p2: int) -> None:
    s1 = 0
    s2 = 0
    roll = 1
    isp1 = True
    move = 6

    while s1 < 1000 and s2 < 1000:
        print("Move " + str(move))

        if isp1:
            print("Player 1: " + str(p1))
            p1 += move
            if p1 > 10:
                p1 %= 10
            s1 += p1
        else:
            print("Player 2: " + str(p2))
            p2 += move
            if p2 > 10:
                p2 %= 10
            s2 += p2

        move = (move+9) % 101
        move = 1 if move == 0 else move
        roll += 3
        isp1 = not isp1

        print((p1, s1) if not isp1 else (p2, s2))
        input()

    print(s1 if s1 < 1000 else s2, roll)


def part_2(p1: int, p2: int) -> None:
    pass


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        line = f.readline()
        p1 = int(line[len(line) - line[::-1].index(" "):])
        line = f.readline()
        p2 = int(line[len(line) - line[::-1].index(" "):])
        part_1(p1, p2)
        part_2(p1, p2)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    # print("With large input data")
    # solve("large.txt")


if __name__ == "__main__":
    main()
