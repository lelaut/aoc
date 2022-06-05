"""
Solution to day 19 of Advent of Code
link: https://adventofcode.com/2021/day/19
"""

from __future__ import annotations
from typing import List, Tuple
from math import sqrt


TOBE_SAME = 12


class Beacon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "%d,%d,%d" % (self.x, self.y, self.z)

    def __eq__(self, __o) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z

    def dst(self, other: Beacon) -> float:
        return sqrt(
            (self.x-other.x) ** 2
            + (self.y-other.y) ** 2
            + (self.z-other.z) ** 2)

    def dsts(self, others: List[Beacon]) -> List[float]:
        return [self.dst(beacon) for beacon in others]

    def same_bdsts(dbase: List[float], dother: List[float]) -> bool:
        counter = 0
        for i in range(len(dbase)):
            for j in range(len(dother)):
                if dbase[i] == dother[j]:
                    counter += 1
                    if counter == TOBE_SAME:
                        return True
        return counter == len(dbase)


def print_scanners(*scanners: List[List[Beacon]]) -> None:
    for scanner in scanners:
        print("Scanner")
        print("\n".join([str(b) for b in scanner]))
        print()


def part_1(scanners: List[List[Beacon]]) -> None:
    # 1. Get scanner beacons to be ground truth
    truth = scanners.pop()
    dtruth = [beacon.dsts(truth) for beacon in truth]
    rm = []

    def getGroundTruthBeacon(scanner: List[Beacon], skip: int) -> Tuple[Beacon, int]:
        for beacon in scanner:
            dbeacon = beacon.dsts(scanner)
            for it in range(len(dtruth)):
                if Beacon.same_bdsts(dtruth[it], dbeacon):
                    if skip == 0:
                        return beacon, it
                    skip -= 1
        return None, -1

    while len(scanners) > 0:
        # 2. For each beacon of each scanner after the first one, try to add as
        # truth:
        for scanner in scanners:
            ba, igtb = getGroundTruthBeacon(scanner, 0)
            bb, jgtb = getGroundTruthBeacon(scanner, 1)

            print(igtb, jgtb)
            input()
            if ba == None or bb == None:
                break

            ox = (ba.x - bb.x) - \
                (truth[igtb].x - truth[jgtb].x)
            oy = (ba.y - bb.y) - \
                (truth[igtb].y - truth[jgtb].y)
            oz = (ba.z - bb.z) - \
                (truth[igtb].z - truth[jgtb].z)

            for jb in scanner:
                b = Beacon(
                    truth[igtb].x + (jb.x - ba.x) - ox,
                    truth[igtb].y + (jb.y - ba.y) - oy,
                    truth[igtb].z + (jb.z - ba.z) - oz)

                if not b in truth:
                    truth.append(b)
            dtruth = [a.dsts(truth) for a in truth]

            # for beacon in scanner:

            # # 2.1 Try to see if distance between other beacons are equal to
            # # ground truth
            # dbeacon = beacon.dsts(scanner)

            # # 2.2 If it is then all other beacons have the position computed
            # # using the real position and the relative current scanner
            # # distances
            # for it in range(len(dtruth)):
            #     if Beacon.same_bdsts(dtruth[it], dbeacon):
            #         # FIXME: I need to rotate scanner back to the
            #         # direction used in the ground truth? That is `jb`
            #         # and `scanner[ib]` needs to be in the same
            #         # direction than `truth[it]`
            #         otherBeacon = truth[it-1]
            #         ox = (beacon.x - otherBeacon.x) - \
            #             (truth[it].x - truth[it-1].x)
            #         oy = (beacon.y - otherBeacon.y) - \
            #             (truth[it].y - truth[it-1].y)
            #         oz = (beacon.z - otherBeacon.z) - \
            #             (truth[it].z - truth[it-1].z)

            #         for jb in scanner:
            #             b = Beacon(
            #                 truth[it].x + (jb.x - beacon.x) - ox,
            #                 truth[it].y + (jb.y - beacon.y) - oy,
            #                 truth[it].z + (jb.z - beacon.z) - oz)

            #             if not b in truth:
            #                 truth.append(b)
            #         founded = True
            #         dtruth = [a.dsts(truth) for a in truth]
            #         break

            # if founded:
            #     break

            # 2.3 If found than remove scanner
            # if founded:
            rm.append(scanner)

        # 3 After that we shall try to discover the beacons stored in `nf`
        # 3.1 Check again for the first one using the ground truth(it will have
        # more beacons than last time)
        # 3.2 Keep going back to the begining until all are found it
        for remove in rm:
            scanners.remove(remove)
        rm.clear()

    # 4. Return the amount of beacons founded
    # FIXME: 877 is too high
    print("Part 1 solution: %d" % len(truth))


def part_2(scanners: List[List[Beacon]]) -> None:
    pass


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        scanners = []
        for line in f.readlines():
            if line.startswith("---"):
                scanners.append([])
            elif len(line.strip()) > 0:
                scanners[-1].append(Beacon(*list(map(int, line.split(",")))))
    part_1(scanners)
    part_2(scanners)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    # print("With large input data")
    # solve("large.txt")


if __name__ == "__main__":
    main()
