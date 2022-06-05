"""
Solution to day 16 of Advent of Code
link: https://adventofcode.com/2021/day/16
"""


from re import M
from typing import Any, Callable, List, Tuple
import functools


def read_header(package: str, pos: int) -> tuple:
    version = int(package[pos:pos+3], 2)
    tid = int(package[pos+3:pos+6], 2)

    if tid != 4:
        return version, tid, package[pos+6]
    return version, tid, None


def read_literal(package: str, pos: int) -> tuple:
    number = ""

    while package[pos] == '1':
        number += package[pos+1:pos+5]
        pos += 5
    number += package[pos+1:pos+5]

    return int(number, 2), pos+5


def read_length_operator(package: str, pos: int, reducer: Callable[[int, int, Any], Any], state: Any) -> tuple:
    length = int(package[pos:pos+15], 2) - 10
    pos += 15
    start_pos = pos

    while pos - start_pos < length:
        state, pos = compute(package, pos, reducer, state)

    return state, pos


def read_amount_operator(package: str, pos: int, reducer: Callable[[int, int, Any], Any], state: Any) -> tuple:
    amount = int(package[pos:pos+11], 2)
    pos += 11

    for i in range(amount):
        state, pos = compute(package, pos, reducer, state)

    return state, pos


def compute(package: str, pos: int, reducer: Callable[[int, int, int, bool, Any], Any], state: Any) -> Tuple[Any, int]:
    v, t, i = read_header(package, pos)

    if t == 4:
        n, pos = read_literal(package, pos+6)
        state = reducer(v, t, n, False, state)
    else:
        state = reducer(v, t, None, False, state)
        if i == '0':
            state, pos = read_length_operator(package, pos+7, reducer, state)
        elif i == '1':
            state, pos = read_amount_operator(package, pos+7, reducer, state)
        else:
            raise Exception("Impossible")
        state = reducer(v, t, None, True, state)

    return state, pos


def part_1(package: str) -> None:
    def step(v: int, t: int, _n: int, _close: bool, state: int) -> int:
        return state + v

    final, _ = compute(package, 0, step, 0)

    print("Part 1 solution: %d" % final)


symbols = {
    0: "+",
    1: "*",
    2: "m",
    3: "M",
    5: ">",
    6: "<",
    7: "=",
}


def operate(op: str, params: List[int]) -> int:
    if op == "+":
        return sum(params)
    if op == "*":
        return functools.reduce(lambda a, b: a*b, params)
    if op == "m":
        return min(params)
    if op == "M":
        return max(params)
    if op == ">":
        return 1 if params[0] > params[1] else 0
    if op == "<":
        return 1 if params[0] < params[1] else 0
    if op == "=":
        return 1 if params[0] == params[1] else 0
    raise NotImplementedError()


def part_2(package: str) -> None:
    def step(_v: int, t: int, n: int, close: bool, state: str) -> str:
        if t == 4:
            return state + str(n) + " "
        if close:
            state = state.rstrip()
            i = state[::-1].index("(")
            op = state[-i-2:-i-1]
            params = list(map(int, state[-i:].split(" ")))
            x = state[:-i-2] + str(operate(op, params)) + " "
            return x
        return state + symbols[t] + "("

    final, _ = compute(package, 0, step, "")

    print("Part 2 solution: %s" % final)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        package = "".join(["{0:b}".format(int(char, 16)).zfill(4)
                           for char in f.readline()])
        part_1(package)
        part_2(package)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
