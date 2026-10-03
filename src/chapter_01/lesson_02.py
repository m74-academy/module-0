from __future__ import annotations


def frame_filename(shot: str, task: str, version: int, frame: int, extension: str) -> str:
    """Return the filename for one frame, e.g. SH010_comp_v002.1001.exr."""
    pass


def sequence_name(shot: str, task: str, version: int) -> str:
    """Return the part every frame of a sequence shares, e.g. SH010_comp_v002."""
    pass
