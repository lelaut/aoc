"""
Solution to day 20 of Advent of Code
link: https://adventofcode.com/2021/day/20
"""


from typing import List

DefaultPixel = "."


def pixel(x: int, y: int, image: List[str]) -> str:
    if x < 0 or y < 0:
        return DefaultPixel
    if y >= len(image) or x >= len(image[0]):
        return DefaultPixel
    return image[y][x]


def windowToIndex(window: str) -> int:
    index = 0
    for i in range(len(window)):
        index += 0 if window[i] == "." else 1 << (len(window)-i-1)
    return index


def enhance(enhancement: str, image: List[str]) -> List[str]:
    result = []
    mx = len(image[0])
    for i in range(len(image)):
        if mx < len(image[i]):
            mx = len(image[i])
    for y in range(-1, len(image)+1):
        result.append("")
        for x in range(-1, mx+1):
            pi = windowToIndex(pixel(x-1, y-1, image)
                               + pixel(x, y-1, image)
                               + pixel(x+1, y-1, image)
                               + pixel(x-1, y, image)
                               + pixel(x, y, image)
                               + pixel(x+1, y, image)
                               + pixel(x-1, y+1, image)
                               + pixel(x, y+1, image)
                               + pixel(x+1, y+1, image))
            result[-1] += enhancement[pi]
    global DefaultPixel
    DefaultPixel = enhancement[0] if DefaultPixel == "." else enhancement[-1]
    return result


def show(image: List[str]) -> None:
    for i in range(len(image)):
        print(image[i])
    print()


def litcount(image: List[str]) -> int:
    count = 0
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == "#":
                count += 1
    return count


def part_1(enhancement: str, image: List[str]) -> None:
    for _ in range(2):
        image = enhance(enhancement, image)
    print("Part 1 solution: %d" % litcount(image))


def part_2(enhancement: str, image: List[str]) -> None:
    for _ in range(50):
        image = enhance(enhancement, image)
    print("Part 2 solution: %d" % litcount(image))


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        enhancement = f.readline().rstrip()
        f.readline()
        image = list(map(lambda l: l.rstrip(), f.readlines()))
        part_1(enhancement, image)
        part_2(enhancement, image)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
