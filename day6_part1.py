#!/usr/bin/env python

from aoc_input import read_full_text


def main():
    print(
        sum(
            sum(1 for answer in get_unique_answers(group))
            for group in get_passenger_groups()
        )
    )


def get_unique_answers(passenger_group):
    return set("".join(passenger_group))


def get_passenger_groups():
    return (
        group.strip().split("\n") for group in read_full_text(2020, 6).split("\n\n")
    )


if __name__ == "__main__":
    main()
