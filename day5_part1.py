#!/usr/bin/env python

from typing import Iterator, List, Tuple

from aoc_input import read_input


def main():
    print(
        max(find_seat_id(boarding_pass, 7) for boarding_pass in get_boarding_passes())
    )


def get_boarding_passes() -> Iterator[str]:
    return read_input(2020, 5)


def find_seat_id(boarding_pass: str, row_chars: int) -> int:
    row_section = boarding_pass[0:row_chars]
    col_section = boarding_pass[row_chars:]
    return find_row(row_section) * (row_chars + 1) + find_column(col_section)


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
