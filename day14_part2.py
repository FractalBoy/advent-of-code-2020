#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations
import re

from aoc_input import read_input


def main():
    mem = defaultdict(lambda: 0)

    for line in read_input(2020, 14):
        [command, value] = line.split(" = ")
        if command == "mask":
            mask = value
        else:
            match = re.search(r"mem\[(\d+)\]", command)
            if match:
                loc = bin(int(match.group(1))).replace("0b", "")
                loc = ("0" * 36) + loc
                loc = list(loc[-36:])

            for i, bit in enumerate(mask):
                if bit == "0":
                    continue
                else:
                    loc[i] = bit

            loc = "".join(loc)

            for address in get_all_addresses(loc):
                mem[address] = int(value)

    print(sum(mem.values()))


def get_all_addresses(address):
    addresses = []
    floating_bits = len([bit for bit in address if bit == "X"])

    for i in range(2 ** floating_bits):
        binary = bin(i).replace("0b", "")
        binary = ("0" * floating_bits) + binary
        binary = binary[-floating_bits:]
        curr_address = address

        for bit in binary:
            curr_address = curr_address.replace("X", bit, 1)

        addresses.append(int(curr_address, 2))

    return addresses


if __name__ == "__main__":
    main()
