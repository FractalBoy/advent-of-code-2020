#!/usr/bin/env python

import re

from aoc_input import read_input


def main():
    rules = get_rules()
    print(count_bags(rules, "shiny gold"))


def count_bags(rules, search_color):
    def _contains_bag(rules, color):
        if color == search_color:
            return True

        for key in rules[color].keys():
            if _contains_bag(rules, key):
                return True

        return False

    bags = 0

    for key in rules.keys():
        if key == search_color:
            continue
        if _contains_bag(rules, key):
            bags += 1

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
