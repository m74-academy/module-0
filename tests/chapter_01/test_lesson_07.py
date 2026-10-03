from __future__ import annotations

import pytest

from chapter_01.lesson_07 import sort_by_frame, summarize


def test_sort_by_frame():
    """Sort by the number, not the text, and leave the input alone."""
    names = ["a.10.exr", "a.9.exr", "a.100.exr", "a.0001.exr"]
    assert sort_by_frame(names) == ["a.0001.exr", "a.9.exr", "a.10.exr", "a.100.exr"]
    assert names == ["a.10.exr", "a.9.exr", "a.100.exr", "a.0001.exr"]


@pytest.mark.parametrize("frames, expected", [
    pytest.param([1001, 1002, 1004], "1001-1002, 1004", id="lesson example"),
    pytest.param([1004, 1001, 1002, 1002], "1001-1002, 1004", id="unsorted with duplicates"),
    pytest.param([7], "7", id="single frame"),
    pytest.param([], "", id="no frames"),
    pytest.param([1, 3, 5], "1, 3, 5", id="all gaps"),
    pytest.param(list(range(998, 1002)), "998-1001", id="crossing a thousand"),
    pytest.param([1, 2, 5, 7, 8, 9], "1-2, 5, 7-9", id="several runs"),
])
def test_summarize(frames: list[int], expected: str):
    """Collapse runs; single frames stay single."""
    assert summarize(frames) == expected
