"""
Solution to day 4 of Advent of Code
link: https://adventofcode.com/2020/day/4
"""


from cgi import test
import re
from typing import Dict, List


PASSPORT_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]
VALID_EYE_COLOR = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def isvalid(passport: Dict[str, str]) -> bool:
    keys = passport.keys()

    if not "byr" in keys or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False

    if not "iyr" in keys or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False

    if not "eyr" in keys or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    if not "hgt" in keys:
        return False
    if passport["hgt"].endswith("cm"):
        if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
            return False
    elif passport["hgt"].endswith("in"):
        if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
            return False
    else:
        return False

    if not "hcl" in keys or re.match(r"^#([0-9]|[a-f]){6}$", passport["hcl"]) == None:
        return False

    if not "ecl" in keys or not passport["ecl"] in VALID_EYE_COLOR:
        return False

    if not "pid" in keys or re.match(r"^[0-9]{9}$", passport["pid"]) == None:
        return False

    return True


def part_1(passports: List[Dict[str, str]]) -> None:
    counter = 0

    for passport in passports:
        keys = passport.keys()
        if len(keys) == len(PASSPORT_FIELDS):
            counter += 1
        elif len(passport.keys()) == len(PASSPORT_FIELDS)-1:
            if not "cid" in keys:
                counter += 1

    print("Part 1 solution %d" % counter)


def part_2(passports: List[Dict[str, str]]) -> None:
    counter = 0

    for passport in passports:
        if isvalid(passport):
            counter += 1

    print("Part 2 solution %d" % counter)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        passports = [{}]
        for line in f.readlines():
            if line.strip() == "":
                passports.append({})
            else:
                for part in line.split():
                    key, value = part.split(":")
                    passports[-1][key] = value
        part_1(passports)
        part_2(passports)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
