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

    validation_table = {
        "byr": validate_byr,
        "iyr": validate_iyr,
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid,
        "cid": validate_cid,
    }

    for key, value in passport.items():
        if not validation_table[key](value):
            return False

    return True


def validate_byr(byr):
    return validate_yr(byr, 1920, 2002)


def validate_iyr(iyr):
    return validate_yr(iyr, 2010, 2020)


def validate_eyr(eyr):
    return validate_yr(eyr, 2020, 2030)


def validate_yr(yr, low, high):
    if re.fullmatch(r"\d{4}", yr) is None:
        return False

    yr = int(yr)

    if yr < low or yr > high:
        return False

    return True


def validate_hgt(hgt):
    match = re.fullmatch(r"(?:(\d{3})cm)|(?:(\d{2})in)", hgt)

    if match is None:
        return False

    value_cm, value_in = match.groups()
    if value_cm is not None:
        value_cm = int(value_cm)
    if value_in is not None:
        value_in = int(value_in)

    if value_cm is not None and (value_cm < 150 or value_cm > 193):
        return False
    if value_in is not None and (value_in < 59 or value_in > 76):
        return False

    return True


def validate_hcl(hcl):
    return re.fullmatch(r"#[0-9a-f]{6}", hcl) is not None


def validate_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(pid):
    return re.fullmatch(r"\d{9}", pid) is not None


def validate_cid(cid):
    return True


if __name__ == "__main__":
    main()
