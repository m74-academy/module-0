from __future__ import annotations

import pytest

from chapter_01.lesson_04 import frame_number, next_version, version_number


@pytest.mark.parametrize("name, expected", [
    ("SH010_comp_v002.0007.exr", 7), ("SH010_comp_v002.1001.exr", 1001),
    ("SH020_comp_v001.0000.DPX", 0), ("SH010_comp_v002.denoise.1001.exr", 1001),
    ("SH010_comp_v002.10001.exr", 10001),
])
def test_frame_number(name: str, expected: int):
    """Return the frame as a number, not text."""
    result = frame_number(name)
    assert result == expected and isinstance(result, int)


@pytest.mark.parametrize("version, expected", [("v002", 2), ("v010", 10), ("v120", 120), ("v1000", 1000)])
def test_version_number(version: str, expected: int):
    """Drop the v and convert the rest to a number."""
    result = version_number(version)
    assert result == expected and isinstance(result, int)


@pytest.mark.parametrize("version, expected", [("v002", "v003"), ("v009", "v010"), ("v099", "v100"), ("v999", "v1000")])
def test_next_version(version: str, expected: str):
    """Add one, keep at least three digits."""
    assert next_version(version) == expected
