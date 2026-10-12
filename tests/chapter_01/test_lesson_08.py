from __future__ import annotations

import pytest

from chapter_01.lesson_08 import group_by_sequence


def test_lesson_example():
    """Group and sort, skipping the note."""
    assert group_by_sequence(["SH010_comp_v002.1002.exr", "notes.txt", "SH010_comp_v002.1001.exr"]) == {
        "SH010_comp_v002.exr": [1001, 1002]}


def test_sample_listing():
    """Four image sequences mixed with other files."""
    names = ["SH010_comp_v002.1001.exr", "SH010_comp_v002.1002.exr", "SH010_comp_v002.1004.exr",
             "SH010_roto_v001.1002.exr", "SH010_roto_v001.1001.exr", "SH020_comp_v001.1000.exr",
             "SH020_comp_v001.0998.exr", "SH020_preview.mov", "SH020_preview.0001.mov", "notes.txt",
             "SH010_comp_v002.denoise.1001.exr"]
    assert group_by_sequence(names) == {
        "SH010_comp_v002.exr": [1001, 1002, 1004],
        "SH010_roto_v001.exr": [1001, 1002],
        "SH020_comp_v001.exr": [998, 1000],
        "SH010_comp_v002.denoise.exr": [1001],
    }


@pytest.mark.parametrize(
    ("names", "expected"),
    [
        pytest.param(["a.1000.exr", "a.999.exr"], {"a.exr": [999, 1000]}, id="unpadded-frames-sort-as-numbers"),
        pytest.param(["a.abcd.exr", "a.1001.exr"], {"a.exr": [1001]}, id="non-digit-frame-skipped"),
        pytest.param(["a.abcd.exr"], {}, id="only-non-digit-frame"),
        pytest.param(["a.-001.exr", "a.0003.exr"], {"a.exr": [3]}, id="sign-is-not-a-digit"),
        pytest.param(["a.0007.exr", "a.0007.dpx"], {"a.exr": [7], "a.dpx": [7]}, id="each-extension-its-own-sequence"),
        pytest.param(["a.0001.EXR", "a.0002.exr"], {"a.EXR": [1], "a.exr": [2]}, id="upper-case-extension"),
        pytest.param(["a. 12.exr", "a.+13.exr", "a.0003.exr"], {"a.exr": [3]}, id="only-digits-count"),
        pytest.param(["a.0007.exr", "a.7.exr"], {"a.exr": [7]}, id="two-paddings-one-frame"),
    ],
)
def test_edge_cases(names, expected):
    """Numeric order, digit-only frames, one group per extension, and each frame listed once."""
    assert group_by_sequence(names) == expected


def test_nothing_to_group():
    """No frames, no groups."""
    assert group_by_sequence(["notes.txt", "thumbnail.exr"]) == {}
    assert group_by_sequence([]) == {}
