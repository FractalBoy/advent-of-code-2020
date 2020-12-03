import fileinput
from typing import Iterator

def read_input() -> Iterator[str]:
    """Read input from stdin or a file, line by line, into an iterator of strings."""
    return (line.strip() for line in fileinput.input())

def read_input_into_ints() -> Iterator[int]:
    """Read input from stdin or a file, line by line, into an iterator of integers."""
    return (int(line) for line in read_input())

def read_input_into_floats() -> Iterator[float]:
    """Read input from stdin or a file, line by line, into an iterator of floats."""
    return (float(line) for line in read_input())
