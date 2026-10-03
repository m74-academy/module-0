from __future__ import annotations

from chapter_01.lesson_08 import group_by_sequence


def test_lesson_example():
    """Group and sort, skipping the note."""
    assert group_by_sequence(["SH010_comp_v002.1002.exr", "notes.txt", "SH010_comp_v002.1001.exr"]) == {
        "SH010_comp_v002": [1001, 1002]}


def test_sample_listing():
    """The lesson folder's three sequences."""
    names = ["SH010_comp_v002.1001.exr", "SH010_comp_v002.1002.exr", "SH010_comp_v002.1004.exr",
             "SH010_roto_v001.1002.exr", "SH010_roto_v001.1001.exr", "SH020_comp_v001.1000.exr",
             "SH020_comp_v001.0998.exr", "SH020_preview.mov", "notes.txt"]
    assert group_by_sequence(names) == {
        "SH010_comp_v002": [1001, 1002, 1004],
        "SH010_roto_v001": [1001, 1002],
        "SH020_comp_v001": [998, 1000],
    }


def test_nothing_to_group():
    """No frames, no groups."""
    assert group_by_sequence(["notes.txt", "thumbnail.exr"]) == {}
    assert group_by_sequence([]) == {}
