#!/usr/bin/env python

from functools import reduce
from operator import mul
from typing import List

from aoc_input import read_input_into_ints


def main():
    numbers = list(read_input_into_ints(2020, 1))
    entries = find_two_entries(numbers, 2020)

    if entries is None:
        print("No two numbers sum to 2020")

    print()
    print(reduce(mul, entries))


def find_two_entries(numbers: List[int], sum: int):
    """Find the two entries in the given list that sum to the given number."""
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue

            if numbers[i] + numbers[j] == sum:
                return numbers[i], numbers[j]

    return None


if __name__ == "__main__":
    main()
