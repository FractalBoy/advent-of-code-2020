#!/usr/bin/env python

import re
from typing import Dict, Iterator

from aoc_input import read_full_text


def main():
    print(sum(1 for passport in get_passports() if is_passport_valid(passport)))


def get_passport_chunks() -> Iterator[str]:
    """Read the input text into individual passport chunks."""
    text = read_full_text(2020, 4)
    return (re.sub(r"\s+", " ", chunk) for chunk in text.split("\n\n"))


def get_passports():
    return (
        dict(re.findall(r"(?:([a-z]{3}):([^\s]+))+", chunk))
        for chunk in get_passport_chunks()
    )


def is_passport_valid(passport: Dict[str, str]):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    keys = list(passport.keys())

    for field in required_fields:
        if field not in keys:
            return False

    return True


if __name__ == "__main__":
    main()
