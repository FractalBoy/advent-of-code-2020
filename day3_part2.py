#!/usr/bin/env python

from itertools import compress, cycle

from aoc_input import read_input


def main():
    matrix = read_map_into_matrix()
    answer = (
        ski(matrix, 1, 1)
        * ski(matrix, 3, 1)
        * ski(matrix, 5, 1)
        * ski(matrix, 7, 1)
        * ski(matrix, 1, 2)
    )
    print(answer)


def ski(matrix, right, down):
    """
    Ski down the slope in the matrix, using the provided slope.

    Returns the number of trees hit.
    """
    matrix = [cycle(line) for line in matrix]
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
        matrix.append(list(line))

    return matrix


if __name__ == "__main__":
    main()
