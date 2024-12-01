from pathlib import Path
from typing import Final

URL: Final[str] = "https://adventofcode.com/2024"


def get_input() -> str:
    """ Get input from folder name. """
    return Path("input").read_text()
