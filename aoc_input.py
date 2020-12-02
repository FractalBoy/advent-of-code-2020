import fileinput
from typing import List

def read_input_into_list() -> List[str]:
    """Read input from stdin or a file, line by line, into a list of strings."""
    return [line.strip() for line in fileinput.input()]

def read_input_into_int_list() -> List[int]:
    """Read input from stdin or a file, line by line, into a list of integers."""
    return [int(line) for line in read_input_into_list()]

def read_input_into_float_list() -> List[float]:
    """Read input from stdin or a file, line by line, into a list of floats."""
    return [float(line) for line in read_input_into_list()]
