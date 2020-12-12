#!/usr/bin/env python

from copy import deepcopy
from os import environ
from itertools import repeat

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
            occupied_seats = 0

            for func in [
                get_east_coords,
                get_west_coords,
                get_north_coords,
                get_south_coords,
                get_northeast_coords,
                get_northwest_coords,
                get_southeast_coords,
                get_southwest_coords,
            ]:
                for next_x, next_y in func(x, y, width, height):
                    if grid[next_y][next_x] == "L":
                        # stop as soon as we hit any seat in this direction
                        break
                    if grid[next_y][next_x] == "#":
                        occupied_seats += 1
                        # stop as soon as we hit any seat in this direction
                        break

            if grid[y][x] == "L" and occupied_seats == 0:
                new_grid[y][x] = "#"
            elif grid[y][x] == "#" and occupied_seats >= 5:
                new_grid[y][x] = "L"

    return new_grid


def get_occupied_seats(grid):
    return sum(len([col for col in row if col == "#"]) for row in grid)


def get_east_coords(x, y, w, h):
    return get_coords(x, y, w, h, 1, 0)


def get_west_coords(x, y, w, h):
    return get_coords(x, y, w, h, -1, 0)


def get_north_coords(x, y, w, h):
    return get_coords(x, y, w, h, 0, -1)


def get_south_coords(x, y, w, h):
    return get_coords(x, y, w, h, 0, 1)


def get_northeast_coords(x, y, w, h):
    return get_coords(x, y, w, h, 1, -1)


def get_northwest_coords(x, y, w, h):
    return get_coords(x, y, w, h, -1, -1)


def get_southeast_coords(x, y, w, h):
    return get_coords(x, y, w, h, 1, 1)


def get_southwest_coords(x, y, w, h):
    return get_coords(x, y, w, h, -1, 1)


def get_coords(x, y, w, h, step_x, step_y):
    x_coords = get_coords_one_dir(x, step_x, w)
    y_coords = get_coords_one_dir(y, step_y, h)

    return list(zip(x_coords, y_coords))


def get_coords_one_dir(p, step, limit):
    if step > 0:
        return range(p + 1, limit, step)
    elif step < 0:
        return reversed(range(0, p, -1 * step))
    else:
        return repeat(p)


def grid_to_string(grid):
    string = ""
    for row in grid:
        for col in row:
            string += col

        string += "\n"

    return string.strip()


def display_grid(grid):
    print(grid_to_string(grid))
    print()


if __name__ == "__main__":
    main()
