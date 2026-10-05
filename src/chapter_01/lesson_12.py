from __future__ import annotations

import os
import sys
from typing import Any


def inventory(folder: str) -> dict[str, Any]:
    """Return the sequences (frames, missing, count) and other files directly inside folder."""
    pass


def report_lines(result: dict[str, Any]) -> list[str]:
    """Return the report: one line per sequence, sorted, then the other files."""
    pass


def main(args: list[str]) -> int:
    """Print the report for FOLDER, save the inventory to OUTPUT; return 0, 1 (missing frames), or 2."""
    pass


# TODO: the guard: when this file is run directly, unpack sys.argv and exit with main(args)
