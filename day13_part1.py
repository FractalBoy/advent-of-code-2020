#!/usr/bin/env python

from math import modf

from aoc_input import read_input


def main():
    lines = read_input(2020, 13)
    departure_time = int(next(lines))
    buses = map(lambda x: int(x), filter(lambda x: x != "x", next(lines).split(",")))

    best_bus = next(buses)
    _, smallest_fractional_part = modf(float(departure_time) / best_bus)

    for bus in buses:
        _, fractional_part = modf(float(departure_time) / bus)

        if fractional_part < smallest_fractional_part:
            best_bus = bus
            smallest_fractional_part = fractional_part

    best_time = 0

    while best_time < departure_time:
        best_time += best_bus

    waiting_time = best_time - departure_time

    print(waiting_time * best_bus)


if __name__ == "__main__":
    main()
