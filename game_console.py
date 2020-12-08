from abc import abstractmethod, ABC
from collections import defaultdict
from typing import Iterator, List


class GameConsole:
    def __init__(self, instructions: List['Instruction']):
        self.instructions = instructions
        self.visited_count = defaultdict(lambda: 0)
        self.pc = 0
        self.acc = 0
        self.exit = False

    def run(self):
        while self.pc < len(self.instructions) and not self.exit:
            self.execute_instruction()

    def execute_instruction(self):
        if self.visited_count[self.pc] > 0:
            print("Status before repeated instruction:")
            print(f"acc: {self.acc} pc: {self.pc}")
            self.exit = True

        self.visited_count[self.pc] += 1
        acc, pc = self.instructions[self.pc].execute()

        self.acc += acc
        self.pc += pc if pc != 0 else 1

    @classmethod
    def from_code(cls, code: Iterator[str]) -> "GameConsole":
        instructions = []

        for line in code:
            [name, value] = line.split(" ")

            value = int(value)

            if name == "acc":
                instructions.append(AccInstruction(value))
            elif name == "jmp":
                instructions.append(JmpInstruction(value))
            elif name == "nop":
                instructions.append(NopInstruction())

        return GameConsole(instructions)


class Instruction(ABC):
    @abstractmethod
    def execute(self):
        pass


class NopInstruction(Instruction):
    def execute(self):
        return 0, 0


class JmpInstruction(Instruction):
    def __init__(self, offset):
        self.offset = offset

    def execute(self):
        return 0, self.offset


class AccInstruction(Instruction):
    def __init__(self, value):
        self.value = value

    def execute(self):
        return self.value, 0
