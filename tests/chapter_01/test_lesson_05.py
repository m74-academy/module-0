from __future__ import annotations

import pytest

from chapter_01.lesson_05 import expected_names, frame_list


@pytest.mark.parametrize("first, last, expected", [
    (1001, 1004, [1001, 1002, 1003, 1004]), (1001, 1001, [1001]), (0, 2, [0, 1, 2]), (1003, 1001, []),
])
def test_frame_list(first: int, last: int, expected: list[int]):
    """Include the last frame; a backwards range is empty."""
    assert frame_list(first, last) == expected


def test_expected_names():
    """Build every name, in order."""
    assert expected_names("SH010_comp_v002", 1001, 1002, ".exr") == [
        "SH010_comp_v002.1001.exr", "SH010_comp_v002.1002.exr"]


@pytest.mark.parametrize("first, last, expected", [
    pytest.param(998, 1000, ["SH020_comp_v001.0998.dpx", "SH020_comp_v001.0999.dpx", "SH020_comp_v001.1000.dpx"],
                 id="three-digit frames"),
    pytest.param(9, 10, ["SH020_comp_v001.0009.dpx", "SH020_comp_v001.0010.dpx"], id="one- and two-digit frames"),
])
def test_expected_names_padding(first: int, last: int, expected: list[str]):
    """Short frame numbers are padded to 4 digits."""
    assert expected_names("SH020_comp_v001", first, last, ".dpx") == expected
