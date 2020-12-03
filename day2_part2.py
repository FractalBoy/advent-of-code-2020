#!/usr/bin/env python

from typing import Iterable, Tuple, Dict, Union

from aoc_input import read_input


def main():
    valid = sum(
        1
        for password, policy in get_passwords_and_policies()
        if evaluate_password_with_policy(password, policy)
    )

    print()
    print(valid)


def evaluate_password_with_policy(password, policy):
    return (password[policy["range"]["start"] - 1] == policy["letter"]) ^ (
        password[policy["range"]["end"] - 1] == policy["letter"]
    )


def get_passwords_and_policies() -> Iterable[
    Tuple[str, Dict[str, Union[str, Dict[str, int]]]]
]:
    for line in read_input():
        parts = line.split()

        [range_start, range_end] = parts[0].split("-")
        letter = parts[1].replace(":", "")

        yield (
            parts[2],
            {
                "range": {"start": int(range_start), "end": int(range_end)},
                "letter": letter,
            },
        )


if __name__ == "__main__":
    main()
