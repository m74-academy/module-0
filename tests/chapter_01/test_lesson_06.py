from __future__ import annotations

import pytest

from chapter_01.lesson_06 import extra_frames, missing_frames

CASES = [
    pytest.param([1001, 1002, 1003, 1004], [1001, 1002, 1004, 1005], [1003], [1005], id="lesson example"),
    pytest.param([1001, 1002], [1002, 1001, 1001], [], [], id="complete with duplicates"),
    pytest.param([3, 1, 2], [], [1, 2, 3], [], id="nothing found, sorted"),
    pytest.param([9, 7, 7, 8], [], [7, 8, 9], [], id="missing, duplicates, sorted"),
    pytest.param([], [9, 7, 7], [], [7, 9], id="nothing expected"),
]


@pytest.mark.parametrize("expected, found, missing, extra", CASES)
def test_missing_frames(expected: list[int], found: list[int], missing: list[int], extra: list[int]):
    """Compare as sets, return a sorted list without duplicates."""
    assert missing_frames(expected, found) == missing


@pytest.mark.parametrize("expected, found, missing, extra", CASES)
def test_extra_frames(expected: list[int], found: list[int], missing: list[int], extra: list[int]):
    """Compare as sets, return a sorted list without duplicates."""
    assert extra_frames(expected, found) == extra
