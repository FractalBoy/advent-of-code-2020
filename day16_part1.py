#!/usr/bin/env python

import re
from itertools import chain

from aoc_input import read_full_text


def main():
    text = read_full_text(2020, 16)

    fields = get_fields(text)
    nearby_tickets = get_tickets("nearby", text)
    your_tickets = get_tickets("your", text)

    invalid_values = []
    all_values = list(chain.from_iterable(nearby_tickets))
    all_fields = set(chain.from_iterable(chain.from_iterable(fields.values())))

    for value in all_values:
        if value not in all_fields:
            invalid_values.append(value)

    print(sum(invalid_values))


def get_tickets(type_, text):
    matches = re.search(rf"{type_} tickets?:\n(?:(?:\d+,)*\d+\n?)+", text, re.MULTILINE)

    if matches:
        ticket_text = matches.group(0).strip().split("\n")[1:]

        tickets = []
        for ticket in ticket_text:
            tickets.append(tuple(map(int, ticket.split(","))))

        return tickets

    return ""


def get_fields(text):
    matches = re.findall(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", text)

    if not matches:
        return {}

    fields = {}

    for field in matches:
        fields[field[0]] = [
            set(range(int(field[1]), int(field[2]) + 1)),
            set(range(int(field[3]), int(field[4]) + 1)),
        ]

    return fields


if __name__ == "__main__":
    main()
