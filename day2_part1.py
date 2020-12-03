#!/usr/bin/env python

from typing import Iterator, Tuple, Dict, Union

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
    """Evaluate the password against its policy."""
    count = len([letter for letter in password if letter == policy["letter"]])

    return count >= policy["range"]["start"] and count <= policy["range"]["end"]


def get_passwords_and_policies() -> Iterator[
    Tuple[str, Dict[str, Union[str, Dict[str, int]]]]
]:
    """Get all of the passwords and their associated policies from the input text."""
    for line in read_input(2020, 2):
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
