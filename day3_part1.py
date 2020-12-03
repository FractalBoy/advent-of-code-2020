#!/usr/bin/env python

from itertools import cycle, compress, count

from aoc_input import read_input


def main():
    print(ski(3, 1))


def ski(right, down):
    """
    Ski down the slope provided by stdin, using the provided slope.

    Returns the number of trees hit.
    """
    matrix = read_map_into_matrix()
    outer_selector = (i % down == 0 for i in range(len(matrix)))

    column = 1
    trees = 0

    for row in compress(matrix, outer_selector):
        inner_selector = (i == column - 1 for i in range(column))

        col = next(compress(row, inner_selector))

        if col == "#":
            trees += 1

        column += right

    return trees


def read_map_into_matrix():
    """Read input into a usable map matrix."""
    matrix = []

    for line in read_input(2020, 3):
        matrix.append(cycle(line))

    return matrix


if __name__ == "__main__":
    main()
