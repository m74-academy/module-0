from __future__ import annotations

import pytest

from chapter_01.lesson_03 import is_image, split_frame_name


@pytest.mark.parametrize("name, expected", [
    ("SH010_comp_v002.1001.exr", True), ("a.0001.DPX", True), ("a.0001.Exr", True),
    ("notes.txt", False), ("exr_notes.txt", False), ("SH020_preview.mov", False),
])
def test_is_image(name: str, expected: bool):
    """Recognize images by the end of the name, in any case."""
    assert is_image(name) is expected


@pytest.mark.parametrize("name, expected", [
    pytest.param("SH010_comp_v002.1001.exr", {"sequence": "SH010_comp_v002", "frame": "1001", "extension": ".exr"},
                 id="lesson example"),
    pytest.param("SH010_comp_v002.denoise.0007.DPX",
                 {"sequence": "SH010_comp_v002.denoise", "frame": "0007", "extension": ".DPX"}, id="extra dot"),
])
def test_split_frame_name(name: str, expected: dict[str, str]):
    """Split from the right; keep the extension's dot and case."""
    assert split_frame_name(name) == expected


@pytest.mark.parametrize("name", ["notes.txt", "thumbnail.exr", "SH020_preview.mov"])
def test_not_a_frame(name: str):
    """Names that aren't frame images give None."""
    assert split_frame_name(name) is None
