from __future__ import annotations


def is_image(name: str) -> bool:
    """Return True for .exr and .dpx files in any letter case."""
    pass


def split_frame_name(name: str) -> dict[str, str] | None:
    """Return sequence, frame, and extension of an image named SEQUENCE.FRAME.ext, or None."""
    pass
