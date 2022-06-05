"""
Solution to day 8 of Advent of Code
link: https://adventofcode.com/2021/day/8
"""


from typing import List

lookupNameToNumber = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}
letters = ["a", "b", "c", "d", "e", "f", "g"]


def part_1(signals: List[List[str]], display: List[List[str]]) -> None:
    unique_sizes = [2, 3, 4, 7]
    counter = 0

    for d in display:
        for i in range(len(d)):
            if len(d[i]) in unique_sizes:
                counter += 1

    print("Part 1 solution:", counter)


def except_in(letter: str, signals: List[str]) -> List[str]:
    exception = []
    for signal in signals:
        if not letter in signal:
            exception.append(signal)
    return exception


def find_letter_in_everyone(jump: int, signals: List[str]) -> List[str]:
    result = []
    for letter in letters:
        counter = 0
        for signal in signals:
            if not letter in signal:
                counter += 1
        if counter == jump:
            result.append(letter)
    return result


def find_unique_signal(unique_size: int, signals: List[str]) -> str:
    for signal in signals:
        if len(signal) == unique_size:
            return signal
    raise Exception("Value %d is not an unique size!" % unique_size)


def find_unknown_letter(signal: str, known: List[str]) -> str:
    for letter in signal:
        if not letter in known:
            return letter
    raise Exception("Signal `%s` is fully known:\n%s" % (signal, known))


def count_unknown_letters(signal: str, known: List[str]) -> int:
    counter = 0
    for letter in signal:
        if not letter in known:
            counter += 1
    return counter


def signal_to_number(signal: str) -> int:
    for name in lookupNameToNumber.keys():
        same = True
        if len(name) != len(signal):
            same = False
        else:
            for letter in signal:
                if not letter in name:
                    same = False
                    break
        if same:
            return lookupNameToNumber[name]
    raise Exception("Signal %s don't exists" % signal)


# b => f T
# e => b T
# a => c T
# d => a T
# f => d T
# c => g T
# g => e T

# 0. cagedb => gcebaf => abcefg
# 1. ab => cf => cf
# 2. gcdfa => egadc => acdeg
# 3. fbcad => dfgca => acdfg
# 4. eafb => bcdf => bcdf
# 5. cdfbe => gadfb => abdfg
# 6. cdfgeb =>  => abdefg
# 7. dab =>  => acf
# 8. acedgfb =>  => abcdefg
# 9. cefabd =>  => abcdfg


def part_2(signals: List[List[str]], display: List[List[str]]) -> None:
    solution = 0

    for i in range(len(signals)):
        real_to_fake = {}
        two_exception = {}

        # Letter `real(f)` is in everyone except one number(`acdeg`), as is
        # letter `real(b)` for four(`cf`,`acdeg`,`acdfg`,`acf`) numbers.
        for letter in letters:
            e = except_in(letter, signals[i])
            l = len(e)
            if l == 1:
                real_to_fake['f'] = find_letter_in_everyone(l, signals[i])[0]
            elif l == 4:
                real_to_fake['b'] = find_letter_in_everyone(l, signals[i])[0]

        # Letter `real(c)` can be discover because is used in an unique together
        # with already known letter `real(f)`
        unique_signal = find_unique_signal(2, signals[i])
        real_to_fake['c'] = find_unknown_letter(
            unique_signal, list(real_to_fake.values()))

        # After knowing `real(c)` the letter `real(a)` can be discover because
        # it appers in everyone except two, being together with letter
        # `real(c)` with is already known.
        except_two = find_letter_in_everyone(
            2, signals[i])
        except_two.remove(real_to_fake['c'])
        real_to_fake['a'] = except_two[0]

        # Letter `real(d)` can be discover with number `4(bcdf)` as all other
        # letters are already known.
        unique_four = find_unique_signal(4, signals[i])
        real_to_fake['d'] = find_unknown_letter(
            unique_four, list(real_to_fake.values()))

        # Letter `real(g)` can be discover using number `9(abcdfg)`, as it is
        # the only one with size 6 and only one number unknown(g).
        six_size = []
        for signal in signals[i]:
            if len(signal) == 6:
                six_size.append(signal)
        for isignal in range(len(six_size)):
            counter = count_unknown_letters(
                six_size[isignal], list(real_to_fake.values()))
            if counter == 1:
                real_to_fake['g'] = find_unknown_letter(
                    six_size[isignal], list(real_to_fake.values()))
                e_signal = six_size[(isignal+1) % len(six_size)]
                break

        # The remaining letter is `real(e)`
        real_to_fake['e'] = find_unknown_letter(
            e_signal, list(real_to_fake.values()))

        # Sum display number to final solution
        fake_to_real = {}
        for real in real_to_fake.keys():
            fake_to_real[real_to_fake[real]] = real
        n = 0
        for j in range(len(display[i])):
            real_signal = ""
            for letter in display[i][j]:
                real_signal += fake_to_real[letter]
            n += signal_to_number(real_signal) * \
                (10 ** (len(display[i]) - j - 1))
        solution += n

    print("Part 2 solution:", solution)


def solve(input_path: str) -> None:
    with open(input_path, "r") as f:
        signals = []
        display = []
        for line in f.readlines():
            s, d = line.split(" | ")
            signals.append(s.split())
            display.append(d.split())
        part_1(signals, display)
        part_2(signals, display)


def main() -> None:
    print("With small input data")
    solve("small.txt")
    print("With large input data")
    solve("large.txt")


if __name__ == "__main__":
    main()
