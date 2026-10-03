from __future__ import annotations


def frame_number(name: str) -> int:
    """Return the frame of a filename as a number, e.g. "SH010_comp_v002.0007.exr" -> 7."""
    pass


def version_number(version: str) -> int:
    """Return the number of a version, e.g. "v002" -> 2."""
    pass


def next_version(version: str) -> str:
    """Return the next version with at least three digits, e.g. "v002" -> "v003"."""
    pass
