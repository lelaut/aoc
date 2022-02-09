"""
Solution to day 14 of Advent of Code
link: https://adventofcode.com/2021/day/14
"""


from typing import Dict


def simulate(initial: str, rules: Dict[str, str], steps: int) -> int:
    graph = {node: [] for node in rules.keys()}

    # Build graph for movements each step
    for node in rules.keys():
        anode = node[0] + rules[node]
        bnode = rules[node] + node[1]

        graph[node].append(anode)
        graph[node].append(bnode)

    letters = set()
    for pattern, node in rules.items():
        letters.add(pattern[0])
        letters.add(pattern[1])
        letters.add(node)

    counter: Dict[str, int] = {}
    for letter in letters:
        counter[letter] = initial.count(letter)

    positions: Dict[str, int] = {}
    for node in rules.keys():
        positions[node] = 0
    for i in range(len(initial)-1):
        positions[initial[i:i+2]] += 1

    newpositions: Dict[str, int] = {}
    for node in rules.keys():
        newpositions[node] = 0
    for _ in range(steps):

        # Make a movement
        for node, amount in positions.items():
            counter[rules[node]] += amount
            for branch in graph[node]:
                newpositions[branch] += amount

        # Update positions
        for node in positions.keys():
            positions[node] = newpositions[node]
            newpositions[node] = 0

    values = list(counter.values())
    values.sort()

    return values[-1] - values[0]


def part_1(initial: str, rules: Dict[str, str]) -> None:
    print("Part 1 solution %d" % simulate(initial, rules, 10))


def part_2(initial: str, rules: Dict[str, str]) -> None:
    print("Part 2 solution %d" % simulate(initial, rules, 40))


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        lines = f.readlines()
        initial = lines[0].rstrip()
        rules = {}
        for i in range(2, len(lines)):
            line = lines[i].split(" -> ")
            rules[line[0]] = line[1].rstrip()
        part_1(initial, rules)
        part_2(initial, rules)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
