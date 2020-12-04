import io
from typing import Iterator

import dotenv
import requests


def read_input(year: int, day: int) -> Iterator[str]:
    """Read input from stdin or a file, line by line, into an iterator of strings."""
    return (line.strip() for line in get_input_from_aoc(year, day))


def read_input_into_ints(year: int, day: int) -> Iterator[int]:
    """Read input from stdin or a file, line by line, into an iterator of integers."""
    return (int(line) for line in read_input(year, day))


def read_input_into_floats(year: int, day: int) -> Iterator[float]:
    """Read input from stdin or a file, line by line, into an iterator of floats."""
    return (float(line) for line in read_input(year, day))


def read_full_text(year: int, day: int) -> str:
    return get_input_from_aoc(year, day).read()


def get_input_from_aoc(year: int, day: int) -> io.StringIO:
    session_id = dotenv.get_key(".env", "SESSION_ID")
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": session_id},
    )
    return io.StringIO(response.text, newline="\n")
