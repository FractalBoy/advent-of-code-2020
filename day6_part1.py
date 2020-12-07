#!/usr/bin/env python

from aoc_input import read_full_text


def main():
    print(sum(len(get_unique_answers(group)) for group in get_passenger_groups()))


def get_unique_answers(passenger_group):
    passenger_group = (set(passenger) for passenger in passenger_group)
    first_passenger = next(passenger_group)
    return first_passenger.union(*passenger_group)


def get_passenger_groups():
    return (
        group.strip().split("\n") for group in read_full_text(2020, 6).split("\n\n")
    )


if __name__ == "__main__":
    main()
