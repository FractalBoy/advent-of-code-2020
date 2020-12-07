#!/usr/bin/env python

import re

from aoc_input import read_input


def main():
    rules = get_rules()
    print(count_bags(rules, "shiny gold"))


def count_bags(rules, color):
    def _count_bags(color, amount):
        bags = 0

        for key in rules[color].keys():
            bags += _count_bags(key, rules[color][key] * amount)

        bags += amount

        return bags

    bags = 0

    for key in rules[color].keys():
        bags += _count_bags(key, rules[color][key])

    return bags


def get_rules():
    rules = {}

    for line in read_input(2020, 7):
        match = re.search(r"^([a-z]+ [a-z]+) bags", line)
        definition_name = match.group(1)
        matches = re.findall(r"(?:(no|\d+) ((?:[a-z]+ )?[a-z]+) bags?)+", line)
        matches = [match for match in matches if match[0] != "no"]
        rules[definition_name] = {color: int(number) for number, color in matches}

    return rules


if __name__ == "__main__":
    main()
