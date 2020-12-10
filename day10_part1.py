#!/usr/bin/env python

from itertools import groupby

from aoc_input import read_input_into_ints


def main():
    distribution = get_joltage_difference_distribution()
    distribution_dict = get_distribution_dict(distribution)
    print(distribution_dict[1] * distribution_dict[3])


def get_joltage_difference_distribution():
    joltages = set(read_input_into_ints(2020, 10))
    differences = []

    next_joltages = [1, 2, 3]
    previous_joltage = 0

    while len(joltages):
        for next_joltage in next_joltages:
            if next_joltage in joltages:
                differences.append(next_joltage - previous_joltage)
                joltages.remove(next_joltage)
                previous_joltage = next_joltage
                next_joltages = map(lambda x: x + previous_joltage, [1, 2, 3])
                break

    differences.append(3)

    return sorted(differences)


def get_distribution_dict(distribution):
    return {k: len(list(v)) for k, v in groupby(distribution)}


if __name__ == "__main__":
    main()
