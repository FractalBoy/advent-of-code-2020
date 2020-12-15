#!/usr/bin/env python

from collections import defaultdict

from aoc_input import read_input


def main():
    numbers = [int(number) for number in next(read_input(2020, 15)).split(",")]
    numbers_occurrences = {number: index + 1 for index, number in enumerate(numbers)}
    del numbers_occurrences[numbers[-1]]

    index = len(numbers) + 1

    while index <= 30000000:
        last_number = numbers[-1]

        if last_number not in numbers_occurrences:
            numbers.append(0)
        else:
            numbers.append(index - 1 - numbers_occurrences[last_number])

        numbers_occurrences[last_number] = index - 1
        index += 1

    print(numbers[-1])


if __name__ == "__main__":
    main()
