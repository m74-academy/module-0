from __future__ import annotations

import pytest

from chapter_01.lesson_07 import format_run, sort_by_frame


def test_sort_by_frame():
    """Sort by the number, not the text, and leave the input alone."""
    names = ["a.10.exr", "a.9.exr", "a.100.exr", "a.denoise.2.exr", "a.0001.exr"]
    assert sort_by_frame(names) == ["a.0001.exr", "a.denoise.2.exr", "a.9.exr", "a.10.exr", "a.100.exr"]
    assert names == ["a.10.exr", "a.9.exr", "a.100.exr", "a.denoise.2.exr", "a.0001.exr"]


@pytest.mark.parametrize("start, end, expected", [
    pytest.param(1004, 1004, "1004", id="single frame"),
    pytest.param(1001, 1004, "1001-1004", id="lesson example"),
    pytest.param(998, 1001, "998-1001", id="crossing a thousand"),
    pytest.param(0, 0, "0", id="frame zero"),
])
def test_format_run(start: int, end: int, expected: str):
    """One frame stays a number; a range becomes start-end."""
    assert format_run(start, end) == expected


def test_sort_by_frame_mixed_sequences():
    """Only the frame decides, even when the names come from two image sequences."""
    names = ["SH010_comp_v002.1001.exr", "SH020_comp_v001.0998.exr", "SH010_comp_v002.0999.exr"]
    assert sort_by_frame(names) == ["SH020_comp_v001.0998.exr", "SH010_comp_v002.0999.exr", "SH010_comp_v002.1001.exr"]
