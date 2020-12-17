#!/usr/bin/env python

import re
from functools import reduce
from itertools import chain
from operator import mul

from aoc_input import read_full_text


def main():
    text = read_full_text(2020, 16)

    fields = get_fields(text)
    nearby_tickets = get_tickets("nearby", text)
    your_ticket = get_tickets("your", text)[0]

    invalid_values = []
    all_fields = set(chain.from_iterable(fields.values()))

    valid_tickets = []

    for ticket in nearby_tickets:
        if all([value in all_fields for value in ticket]):
            valid_tickets.append(ticket)

    # List of each column of the CSV.
    column_values = list(zip(*valid_tickets))
    # Dictionary of field name to potential indices.
    field_indices = {field: set(range(len(valid_tickets[0]))) for field in fields.keys()}

    # Remove column numbers for each field that does not match the ranges.
    for i in range(len(column_values)):
        for field, range_ in fields.items():
            values_in_range = [value for value in column_values[i] if value in range_]

            if len(values_in_range) != len(column_values[i]):
                field_indices[field].remove(i)

    # Whiddle down indices by setting an int for any field that has only one possible index,
    # then remove that index from all other fields, since it can only be used once.
    #
    # Repeat until all fields have been resolved.
    while True:
        for field, values in field_indices.items():
            if isinstance(values, set) and len(values) == 1:
                field_indices[field] = list(values)[0]

                for values_ in field_indices.values():
                    if isinstance(values_, set) and field_indices[field] in values_:
                        values_.remove(field_indices[field])

        if all(isinstance(_values, int) for _values in field_indices.values()):
            break


    print(
        reduce(
            mul,
            [
                your_ticket[index]
                for field, index in field_indices.items()
                if field.startswith("departure")
            ],
        )
    )


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
        fields[field[0]] = set(
            chain.from_iterable(
                [
                    range(int(field[1]), int(field[2]) + 1),
                    range(int(field[3]), int(field[4]) + 1),
                ]
            )
        )

    return fields


if __name__ == "__main__":
    main()
