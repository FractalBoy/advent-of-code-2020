#!/usr/bin/env python

from itertools import combinations

from aoc_input import read_input_into_ints

PREAMBLE_SIZE = 25


def main():
    numbers = list(read_input_into_ints(2020, 9))

    for i in range(len(numbers)):
        if i < PREAMBLE_SIZE:
            continue

        sums = get_sums(numbers[i - PREAMBLE_SIZE : i])

        if numbers[i] not in sums:
            target = numbers[i]
            break

    group = []
    total = 0

    for number in numbers:
        total += number
        group.append(number)

        while total > target:
            total -= group[0]
            del group[0]

        if total == target:
            break

    print(min(group) + max(group))


def get_sums(preamble):
    sums = set()

    for a, b in combinations(preamble, 2):
        sums.add(a + b)

    return sums


if __name__ == "__main__":
    main()
