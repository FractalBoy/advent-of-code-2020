#!/usr/bin/env python

from functools import reduce
from itertools import count

from aoc_input import read_input


def main():
    lines = read_input(2020, 13)
    _ = next(lines)
    buses = next(lines).split(",")

    increment = int(buses[0])
    common = 0

    for i in range(1, len(buses)):
        if buses[i] == "x":
            continue

        while True:
            common += increment

            # We found the correct number
            if (common + i) % int(buses[i]) == 0:
                # Start incrementing by the product of the current increment
                # and this bus - the next common time must be a multiple of this number
                increment *= int(buses[i])
                break

    print(common)


if __name__ == "__main__":
    main()
