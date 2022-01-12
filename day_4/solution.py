"""
Solution to day 4 of Advent of Code
link: https://adventofcode.com/2021/day/4
"""

from typing import List


class Board:
    VALUE = 0
    MARKED = 1

    def __init__(self, lines: List[str]) -> None:
        self.state = [[[int(value), False] for value in line.split()]
                      for line in lines]

    def __str__(self) -> str:
        ret = ""
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                ret += str((self.state[i][j][Board.VALUE],
                            self.state[i][j][Board.MARKED])) + " "
            ret += "\n"
        return ret + "\n"

    def _check(self, ipos: int, jpos: int) -> bool:
        won = True
        for i in range(len(self.state)):
            if not self.state[i][jpos][Board.MARKED]:
                won = False
                break
        if won:
            return True

        won = True
        for j in range(len(self.state[ipos])):
            if not self.state[ipos][j][Board.MARKED]:
                won = False
                break
        if won:
            return True

    def draw(self, number: int) -> bool:
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j][Board.VALUE] == number:
                    self.state[i][j][Board.MARKED] = True
                    return self._check(i, j)

    def sum_unmarked(self) -> int:
        value = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if not self.state[i][j][Board.MARKED]:
                    value += self.state[i][j][Board.VALUE]
        return value


def part_1(numbers_draw: List[int], boards: List[Board]) -> None:
    solution = (-1, -1)

    for number in numbers_draw:
        for board in boards:
            if board.draw(number):
                solution = (board.sum_unmarked(), number)
                break
        if solution[0] != -1:
            break

    print("Part 1 solution: %d * %d = %d" %
          (solution + (solution[0]*solution[1],)))


def part_2(numbers_draw: List[int], boards: List[Board]) -> None:
    solution = (-1, -1)
    winner: List[Board] = []

    for number in numbers_draw:
        for board in boards:
            if board.draw(number):
                winner.append(board)
        for board in winner:
            boards.remove(board)
            if len(boards) == 0:
                solution = (board.sum_unmarked(), number)
                break
        winner.clear()

    print("Part 2 solution: %d * %d = %d" %
          (solution + (solution[0]*solution[1],)))


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        lines = f.readlines()
        numbers_draw = [int(value) for value in lines[0].split(',')]
        begin = 2
        boards = []
        for i in range(2, len(lines)):
            if lines[i] == '\n':
                boards.append(Board(lines[begin:i]))
                begin = i+1
        boards.append(Board(lines[begin:len(lines)]))

        part_1(numbers_draw, boards)
        part_2(numbers_draw, boards)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
