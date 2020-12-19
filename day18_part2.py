#!/usr/bin/env python

import sys

from aoc_input import read_input
from calc import CalcLexer, AdvancedCalcParser


def main():
    lexer = CalcLexer()
    parser = AdvancedCalcParser()

    sum_ = 0

    for line in read_input(2020, 18):
        sum_ += parser.parse(lexer.tokenize(line))

    print(sum_)


if __name__ == "__main__":
    main()
