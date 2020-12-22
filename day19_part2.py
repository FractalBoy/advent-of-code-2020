#!/usr/bin/env python

import re
import subprocess
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
    rules = {
        int(index): rule.replace(" | ", "|").strip()
        for [index, rule] in [rule.split(":") for rule in rules]
    }
    messages = messages.splitlines()

    lexer = RuleLexer()
    parser = RuleParser()

    for rule in rules:
        rules[rule] = parser.parse(lexer.tokenize(rules[rule]))

    rule_res = {}
    for rule in sorted(rules.keys()):
        if rule == 0 or rule == 8 or rule == 11:
            continue
        rule_res[rule] = generate_regex(rules, rule)

    # Pattern 8 is just pattern 42 one or more times
    rule_res[8] = f"(?:{rule_res[42]}+)"
    # Pattern 11 needs to specifically use a recursive regex
    rule_res[
        11
    ] = f"(?:({rule_res[42]}{rule_res[31]}|{rule_res[42]}(?-1){rule_res[31]}))"
    # Now that we have patterns 8 and 11 we can build pattern 0
    rule_res[0] = f"^(?:{rule_res[8]}{rule_res[11]})$"

    count = 0

    for message in messages:
        # Need to use perl because Python does not have recursive regex
        # (could use the regex module but don't feel like it)
        proc = subprocess.run(
            f"perl -e 'print \"{message}\" =~ /{rule_res[0]}/ ? 1 : 0'",
            capture_output=True,
            shell=True,
        )
        if int(proc.stdout) == 1:
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
            return f"(?:{generate_regex(rules, first)}|{generate_regex(rules, second)})"
        elif op == "then":
            return f"(?:{generate_regex(rules, first)}{generate_regex(rules, second)})"


if __name__ == "__main__":
    main()
