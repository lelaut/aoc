"""
Solution to day 9 of Advent of Code
link: https://adventofcode.com/2021/day/9
"""


from typing import List, Tuple


def find_low_points(heightmap: List[List[int]],) -> List[Tuple[int, int]]:
    low_points = []

    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if x - 1 >= 0 and heightmap[y][x-1] <= heightmap[y][x]:
                continue
            if x + 1 < len(heightmap[y]) and heightmap[y][x+1] <= heightmap[y][x]:
                continue
            if y - 1 >= 0 and heightmap[y-1][x] <= heightmap[y][x]:
                continue
            if y + 1 < len(heightmap) and heightmap[y+1][x] <= heightmap[y][x]:
                continue
            low_points.append((x, y))

    return low_points


def part_1(heightmap: List[List[int]]) -> None:
    low_points = find_low_points(heightmap)
    risk_level = sum([heightmap[p[1]][p[0]]
                      for p in low_points]) + len(low_points)

    print("Part 1 solution: %d" % risk_level)


def fill(x: int, y: int, heightmap: List[List[int]], computed: List[List[bool]], low_point: int = -1):
    if computed[y][x]:
        return 0
    if low_point == -1:
        low_point = heightmap[y][x]
    computed[y][x] = True
    counter = 1

    if x - 1 >= 0 and heightmap[y][x-1] < 9 and heightmap[y][x-1] > low_point:
        counter += fill(x-1, y, heightmap, computed, low_point)
    if x + 1 < len(heightmap[y]) and heightmap[y][x+1] < 9 and heightmap[y][x+1] > low_point:
        counter += fill(x+1, y, heightmap, computed, low_point)
    if y - 1 >= 0 and heightmap[y-1][x] < 9 and heightmap[y-1][x] > low_point:
        counter += fill(x, y-1, heightmap, computed, low_point)
    if y + 1 < len(heightmap) and heightmap[y+1][x] < 9 and heightmap[y+1][x] > low_point:
        counter += fill(x, y+1, heightmap, computed, low_point)

    return counter


def part_2(heightmap: List[List[int]]) -> None:
    low_points = find_low_points(heightmap)
    computed = [[False for _ in range(len(heightmap[y]))]
                for y in range(len(heightmap))]
    basin_sizes = []

    for point in low_points:
        basin_sizes.append(fill(point[0], point[1], heightmap, computed))

    basin_sizes.sort(reverse=True)
    print("Part 2 solution: %d" %
          (basin_sizes[0]*basin_sizes[1]*basin_sizes[2]))


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        heightmap = []
        for line in f.readlines():
            heightmap.append(list(map(int, list(line.strip()))))
        part_1(heightmap)
        part_2(heightmap)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
