#!/usr/bin/env python

import re

from aoc_input import read_input


def main():
    rules = get_rules()
    tree = build_bag_tree(rules, "shiny gold")
    print(len(tree.keys()))


def build_bag_tree(rules, search_color):
    def _build_bag_tree(rules, color):
        if color == search_color:
            return True

        tree = {}

        for key in rules[color].keys():
            value = _build_bag_tree(rules, key)
            if value:
                tree[key] = value

        if not len(tree.keys()):
            return False

        return tree

    tree = {}

    for color in rules.keys():
        tree[color] = _build_bag_tree(rules, color)

    tree = {key: value for key, value in tree.items() if value}
    del tree[search_color]
    return tree


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
