from abc import abstractmethod, ABC
from collections import defaultdict
from typing import Iterator, List


class GameConsole:
    def __init__(self, instructions: List["Instruction"]):
        self.instructions = instructions
        self.reset()

    def reset(self):
        self.pc = 0
        self.acc = 0
        self.infinite_loop = False
        self.visited_count = defaultdict(lambda: 0)

    def run(self):
        while self.pc < len(self.instructions) and not self.infinite_loop:
            self.execute_instruction()

    def execute_instruction(self):
        if self.visited_count[self.pc] > 0:
            self.infinite_loop = True
            return

        self.visited_count[self.pc] += 1
        acc, pc = self.instructions[self.pc].execute()

        self.acc += acc
        self.pc += pc if pc != 0 else 1

    @classmethod
    def from_code(cls, code: Iterator[str]) -> "GameConsole":
        instructions = []

        dispatch_table = {
            "acc": AccInstruction,
            "jmp": JmpInstruction,
            "nop": NopInstruction,
        }

        for line in code:
            [name, value] = line.split(" ")

            value = int(value)

            instructions.append(dispatch_table[name](value))

        return GameConsole(instructions)


class Instruction(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def execute(self):
        pass


class NopInstruction(Instruction):
    def execute(self):
        return 0, 0


class JmpInstruction(Instruction):
    def execute(self):
        return 0, self.value


class AccInstruction(Instruction):
    def execute(self):
        return self.value, 0
