"""
Solution to day 13 of Advent of Code
link: https://adventofcode.com/2021/day/13
"""


from typing import List, Tuple


def part_1(points: List[List[int]], instructions: List[Tuple[str, int]]) -> None:
    flipped = 0

    if instructions[0][0] == "x":
        for point in points:
            flip = (point[0] - instructions[0][1]) * 2
            if flip > 0:
                flipped += 1
                newpoint = [point[0] - flip, point[1]]
                if newpoint[0] >= 0 and not newpoint in points:
                    points.append(newpoint)
    else:
        for point in points:
            flip = (point[1] - instructions[0][1]) * 2
            if flip > 0:
                flipped += 1
                newpoint = [point[0], point[1] - flip]
                if newpoint[1] >= 0 and not newpoint in points:
                    points.append(newpoint)

    print("Part 1 solution %d" % (len(points) - flipped))


def part_2(points: List[List[int]], instructions: List[Tuple[str, int]]) -> None:
    remove = []
    for instruction in instructions:
        if instruction[0] == "x":
            for point in points:
                flip = (point[0] - instruction[1]) * 2
                if flip > 0:
                    remove.append(point)
                    newpoint = [point[0] - flip, point[1]]
                    if newpoint[0] >= 0 and not newpoint in points:
                        points.append(newpoint)
        else:
            for point in points:
                flip = (point[1] - instruction[1]) * 2
                if flip > 0:
                    remove.append(point)
                    newpoint = [point[0], point[1] - flip]
                    if newpoint[1] >= 0 and not newpoint in points:
                        points.append(newpoint)

        for point in remove:
            points.remove(point)
        remove.clear()

    xmax = 0
    ymax = 0
    for point in points:
        xmax = max(xmax, point[0])
        ymax = max(ymax, point[1])

    print("Part 2 solution:")
    for y in range(ymax+1):
        for x in range(xmax+1):
            print("#" if [x, y] in points else ".", end="")
        print()


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        points = []
        instructions = []
        for line in f.readlines():
            if line.strip() != "":
                if line.startswith("fold"):
                    instruction = line[len("fold along "):].rstrip()
                    instruction = instruction.split("=")
                    instruction = (instruction[0], int(instruction[1]))
                    instructions.append(instruction)
                else:
                    points.append(list(map(int, line.rstrip().split(","))))
        part_1(points, instructions)
        part_2(points, instructions)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
