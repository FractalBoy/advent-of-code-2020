#!/usr/bin/env python

from typing import Iterator, List, Tuple, Set

from aoc_input import read_input


def main():
    print(find_my_seat())


def get_boarding_passes() -> Iterator[str]:
    return read_input(2020, 5)


def find_my_seat() -> int:
    missing_numbers = set(range(1023)).difference(get_seat_ids())

    for missing_number in missing_numbers:
        if (
            missing_number + 1 not in missing_numbers
            and missing_number - 1 not in missing_numbers
        ):
            return missing_number


def get_seat_ids() -> Iterator[int]:
    return set(find_seat_id(boarding_pass) for boarding_pass in get_boarding_passes())


def find_seat_id(boarding_pass: str) -> int:
    row_section = boarding_pass[0:7]
    col_section = boarding_pass[7:]
    return find_row(row_section) * 8 + find_column(col_section)


def find_row(boarding_pass: Iterator[str]) -> int:
    row = 0

    for section in boarding_pass:
        row <<= 1

        if section == "F":
            row |= 0
        if section == "B":
            row |= 1

    return row


def find_column(boarding_pass: List[str]) -> int:
    col = 0

    for section in boarding_pass:
        col <<= 1

        if section == "L":
            col |= 0
        if section == "R":
            col |= 1

    return col


if __name__ == "__main__":
    main()
