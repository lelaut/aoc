"""
Solution to day 18 of Advent of Code
link: https://adventofcode.com/2021/day/18
"""


from __future__ import annotations
from typing import List

import math


class Node:
    def __init__(self, number: str = "", nodes: List[Node] = None, parent: Node = None, lit: int = None) -> None:
        self.parent = parent

        if nodes != None:
            self.type = "pair"
            self.data = nodes
            self.data[0].parent = self
            self.data[1].parent = self
            return
        if lit != None:
            self.type = "literal"
            self.data = lit
            return

        if number.startswith("["):
            self.type = "pair"
            n = 0
            for i in range(len(number)):
                if number[i] == "[":
                    n += 1
                elif number[i] == ",":
                    n -= 1
                    if n == 0:
                        self.data = [
                            Node(number[1:i], parent=self),
                            Node(number[i+1:-1], parent=self)]
                        break
        else:
            self.type = "literal"
            self.data = int(number)

    def __str__(self) -> str:
        if self.type == "pair":
            return "[%s,%s]" % (str(self.data[0]), str(self.data[1]))
        return str(self.data)

    def _left(self, ignore: Node) -> Node:
        if self.data[0] != ignore:
            return self.data[0]
        if self.parent == None:
            return None
        return self.parent._left(self)

    def _right(self, ignore: Node) -> Node:
        if self.data[1] != ignore:
            return self.data[1]
        if self.parent == None:
            return None
        return self.parent._right(self)

    def _llit(self) -> Node:
        if self.type == "literal":
            return self
        if self.data[0].type == "literal":
            return self.data[0]
        return self.data[0]._llit()

    def _rlit(self) -> Node:
        if self.type == "literal":
            return self
        if self.data[1].type == "literal":
            return self.data[1]
        return self.data[1]._rlit()

    def _check_explosion(self, depth: int) -> bool:
        if self.type == "pair":

            if depth == 4:
                lr = self.parent._left(self)
                if lr != None:
                    rlit = lr if lr.type == "literal" else lr.data[1]._rlit(
                    )
                    rlit.data += self.data[0].data
                rr = self.parent._right(self)
                if rr != None:
                    llit = rr if rr.type == "literal" else rr.data[0]._llit(
                    )
                    llit.data += self.data[1].data

                if self == self.parent.data[0]:
                    self.parent.data = [
                        Node(lit=0, parent=self.parent), self.parent.data[1]]
                else:
                    self.parent.data = [self.parent.data[0],
                                        Node(lit=0, parent=self.parent)]

                return True

            lr = self.data[0]._check_explosion(depth+1)
            rr = self.data[1]._check_explosion(depth+1)
            return lr or rr

        return False

    def _check_splits(self):
        if self.data[0].type == "literal":
            n = self.data[0].data
            if n > 9:
                self.data[0] = Node(
                    nodes=[
                        Node(lit=math.floor(n / 2)),
                        Node(lit=math.ceil(n / 2))],
                    parent=self)

                return True
        else:
            if self.data[0]._check_splits():
                return True
        if self.data[1].type == "literal":
            n = self.data[1].data
            if n > 9:
                self.data[1] = Node(
                    nodes=[
                        Node(lit=math.floor(n / 2)),
                        Node(lit=math.ceil(n / 2))],
                    parent=self)

                return True
        else:
            return self.data[1]._check_splits()
        return False

    def root(self) -> Node:
        r = self
        while r.parent != None:
            r = r.parent
        return r

    def add(self, other: Node) -> Node:
        node = Node(nodes=[self, other])
        done = False

        while True:
            while node.root()._check_explosion(0):
                pass
            if not node.root()._check_splits():
                break

        return node

    def magnitude(self) -> int:
        l = self.data[0].data * 3 \
            if self.data[0].type == "literal" else 3 * self.data[0].magnitude()
        r = self.data[1].data * 2 \
            if self.data[1].type == "literal" else 2 * self.data[1].magnitude()
        return l+r


def part_1(homework: List[str]) -> None:
    state = Node(homework[0])
    for i in range(1, len(homework)):
        node = Node(homework[i])
        state = state.add(node)

    print("Part 1 solution is %d" % state.root().magnitude())


def part_2(homework: List[str]) -> None:
    maxm = 0
    for i in range(len(homework)):
        for j in range(len(homework)):
            if i != j:
                a = Node(homework[i])
                b = Node(homework[j])
                m = a.add(b).root().magnitude()
                if m > maxm:
                    maxm = m

    print("Part 2 solution is %d" % maxm)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        homework = [l.strip() for l in f.readlines()]
        part_1(homework)
        part_2(homework)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
