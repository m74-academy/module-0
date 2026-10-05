from __future__ import annotations

import pytest

from chapter_01.lesson_02 import frame_filename, sequence_name


@pytest.mark.parametrize("args, expected", [
    pytest.param(("SH010", "comp", 2, 1001, ".exr"), "SH010_comp_v002.1001.exr", id="lesson example"),
    pytest.param(("SH010", "comp", 2, 7, ".exr"), "SH010_comp_v002.0007.exr", id="single-digit frame"),
    pytest.param(("SH010", "comp", 2, 0, ".exr"), "SH010_comp_v002.0000.exr", id="frame zero"),
    pytest.param(("SH020", "roto", 12, 1001, ".dpx"), "SH020_roto_v012.1001.dpx", id="dpx and two-digit version"),
    pytest.param(("SH010", "comp", 2, 12345, ".exr"), "SH010_comp_v002.12345.exr", id="width is a minimum"),
])
def test_frame_filename(args: tuple, expected: str):
    """Pad the version to 3 digits and the frame to 4."""
    assert frame_filename(*args) == expected


@pytest.mark.parametrize("args, expected", [
    pytest.param(("SH010", "comp", 2), "SH010_comp_v002", id="lesson example"),
    pytest.param(("SH999", "lgt", 120), "SH999_lgt_v120", id="three-digit version"),
])
def test_sequence_name(args: tuple, expected: str):
    """The shared part of every frame name."""
    assert sequence_name(*args) == expected
