#!/usr/bin/env python

from collections import defaultdict
import re

from aoc_input import read_input


def main():
    mem = defaultdict(lambda: 0)

    for line in read_input(2020, 14):
        [command, value] = line.split(" = ")
        if command == "mask":
            or_mask = int(value.replace("X", "0"), 2)
            and_mask = int(value.replace("X", "1"), 2)
            continue
        else:
            match = re.search(r"mem\[(\d+)\]", command)
            if match:
                loc = int(match.group(1))

            mem[loc] = int(value) & and_mask | or_mask

    print(sum(mem.values()))


if __name__ == "__main__":
    main()
