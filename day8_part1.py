#!/usr/bin/env python

from aoc_input import read_input
from game_console import GameConsole


def main():
    code = read_input(2020, 8)
    game_console = GameConsole.from_code(code)
    game_console.run()
    print(game_console.acc)


if __name__ == "__main__":
    main()
