#!/usr/bin/env python

from aoc_input import read_input_into_ints


def main():
    print(get_joltage_count())


def get_joltage_count():
    joltages = set(read_input_into_ints(2020, 10))
    cache = {}

    def _get_next_joltage_count(curr_joltage, max_joltage):
        if curr_joltage in cache:
            return cache[curr_joltage]

        count = 0
        for joltage in map(lambda x: x + curr_joltage, [1, 2, 3]):
            if joltage in joltages:
                count += _get_next_joltage_count(joltage, max_joltage)

        cache[curr_joltage] = count
        return count

    max_joltage = max(joltages)
    cache[max_joltage] = 1
    return _get_next_joltage_count(0, max_joltage)


if __name__ == "__main__":
    main()
