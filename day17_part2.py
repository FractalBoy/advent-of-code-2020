#!/usr/bin/env python

from aoc_input import read_full_text
from cube import Cube


def main():
    cube = Cube(read_full_text(2020, 17), 4)

    for _ in range(6):
        cube.simulate_cycle()

    print(cube.count_active())


if __name__ == "__main__":
    main()
