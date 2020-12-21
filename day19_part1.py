#!/usr/bin/env python

import re
from itertools import combinations

from rule import RuleLexer, RuleParser
from aoc_input import read_full_text


def main():
    text = read_full_text(2020, 19)

    [rules, messages] = text.split("\n\n")
    rules = rules.splitlines()
    # Need to slightly change formatting so precedence rules work.
    # Space cannot be both an operator and space - it just doesn't make sense,
    # so remove spaces around |, which are just for display.
    rules = {int(index): rule.replace(" | ", "|").strip() for [index, rule] in [rule.split(':') for rule in rules]}
    messages = messages.splitlines()

    lexer = RuleLexer()
    parser = RuleParser()

    for rule in rules:
        rules[rule] = parser.parse(lexer.tokenize(rules[rule]))

    regex = re.compile("^" + generate_regex(rules, 0) + "$")
    count = 0

    for message in messages:
        if regex.match(message):
            count += 1

    print(count)


def generate_regex(rules, rule):
    if isinstance(rule, int):
        return generate_regex(rules, rules[rule])
    elif isinstance(rule, str):
        return rule
    elif isinstance(rule, tuple):
        first, op, second = rule

        if op == "or":
            return "(?:" + generate_regex(rules, first) + "|" + generate_regex(rules, second) + ")"
        elif op == "then":
            return  "(?:" + generate_regex(rules, first) + generate_regex(rules, second) + ")"

if __name__ == "__main__":
    main()
