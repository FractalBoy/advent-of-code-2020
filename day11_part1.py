#!/usr/bin/env python

from copy import deepcopy
from os import environ

from aoc_input import read_input

DEBUG = bool(int(environ.get("DEBUG", 0)))

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def main():
    grid = get_seat_grid()

    num_rounds = 0
    prev_seats = 0

    while True:
        grid = simulate_round(grid)
        if DEBUG:
            display_grid(grid)

        num_rounds += 1
        curr_seats = get_occupied_seats(grid)

        if prev_seats == curr_seats:
            break

        prev_seats = curr_seats

    print(prev_seats)


def get_seat_grid():
    if DEBUG:
        return [list(line) for line in test_input.strip().split("\n")]
    else:
        return [list(line) for line in read_input(2020, 11)]


def simulate_round(grid):
    width = len(grid[0])
    height = len(grid)

    new_grid = deepcopy(grid)

    for y in range(height):
        for x in range(width):
            adjacent = get_adjacent_seats(grid, x, y)
            num_occupied = len([seat for seat in adjacent if seat == "#"])

            if grid[y][x] == "L" and num_occupied == 0:
                new_grid[y][x] = "#"
            elif grid[y][x] == "#" and num_occupied >= 4:
                new_grid[y][x] = "L"

    return new_grid


def get_occupied_seats(grid):
    return sum(len([col for col in row if col == "#"]) for row in grid)


def get_adjacent_seats(grid, x, y):
    width = len(grid[0])
    height = len(grid)
    coords = [
        (x - 1, y - 1),
        (x - 1, y),
        (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
    ]
    coords = ((x, y) for x, y in coords if 0 <= x < width and 0 <= y < height)
    return map(lambda xy: grid[xy[1]][xy[0]], coords)


def display_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")

        print()

    print()


if __name__ == "__main__":
    main()
