#!/usr/bin/env python

from aoc_input import read_input
from game_console import GameConsole, JmpInstruction, NopInstruction


def main():
    code = read_input(2020, 8)
    game_console = GameConsole.from_code(code)

    for i in range(len(game_console.instructions)):
        old_instruction = None
        game_console.reset()

        if isinstance(game_console.instructions[i], JmpInstruction):
            old_instruction = game_console.instructions[i]
            game_console.instructions[i] = NopInstruction(old_instruction.value)
        elif isinstance(game_console.instructions[i], NopInstruction):
            old_instruction = game_console.instructions[i]
            game_console.instructions[i] = JmpInstruction(old_instruction.value)

        game_console.run()

        if not game_console.infinite_loop:
            break

        if old_instruction is not None:
            game_console.instructions[i] = old_instruction

    print(game_console.acc)

if __name__ == "__main__":
    main()
