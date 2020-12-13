#!/usr/bin/env python

from aoc_input import read_input
from ship import ComplexShip


def main():
    ship = ComplexShip()

    for instruction in read_input(2020, 12):
        direction, units = instruction[0], int(instruction[1:])
        ship.move(direction, units)

    print(sum(map(abs, ship.origin)))


if __name__ == "__main__":
    main()
