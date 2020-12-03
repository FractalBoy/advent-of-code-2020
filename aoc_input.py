import fileinput
from typing import Iterable

def read_input() -> Iterable[str]:
    """Read input from stdin or a file, line by line, into a list of strings."""
    return (line.strip() for line in fileinput.input())

def read_input_into_ints() -> Iterable[int]:
    """Read input from stdin or a file, line by line, into a list of integers."""
    return (int(line) for line in read_input())

def read_input_into_floats() -> Iterable[float]:
    """Read input from stdin or a file, line by line, into a list of floats."""
    return (float(line) for line in read_input())
