from __future__ import annotations

from pathlib import Path

import pytest

from chapter_01.lesson_09 import image_files, list_files

SAMPLE = Path(__file__).resolve().parents[2] / "docs/chapters/01-shot-inventory/sample/dump"


def _make(folder: Path, *names: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for name in names:
        (folder / name).write_text("fixture\n", encoding="utf-8")
    return folder


def _visible(names: list[str]) -> list[str]:
    """Drop hidden names, such as a `.DS_Store` that macOS may add."""
    return [name for name in names if not name.startswith(".")]


def test_sample_folder():
    """The lesson's folder has eleven files, nine of them images, sorted by character code."""
    files = _visible(list_files(str(SAMPLE)))
    assert len(files) == 11
    assert files[-1] == "notes.txt"
    assert len(_visible(image_files(str(SAMPLE)))) == 9


@pytest.mark.parametrize(
    ("files", "subfolder", "listed", "images"),
    [
        (
            ("b.1002.exr", "a.1001.EXR", "notes.txt"),
            "old",
            ["a.1001.EXR", "b.1002.exr", "notes.txt"],
            ["a.1001.EXR", "b.1002.exr"],
        ),
        (
            ("notes.exr.txt", "a.1001.dpx", "C.1003.DPX"),
            "old.v001",
            ["C.1003.DPX", "a.1001.dpx", "notes.exr.txt"],
            ["C.1003.DPX", "a.1001.dpx"],
        ),
    ],
)
def test_direct_files_only(
    tmp_path: Path, files: tuple[str, ...], subfolder: str, listed: list[str], images: list[str]
):
    """Subfolders and their contents are skipped; names are sorted; images match by extension."""
    _make(tmp_path, *files)
    _make(tmp_path / subfolder, "a.1000.exr")
    assert list_files(str(tmp_path)) == listed
    assert image_files(str(tmp_path)) == images


def test_empty_folder(tmp_path: Path):
    """Nothing in, nothing out."""
    assert list_files(str(tmp_path)) == [] and image_files(str(tmp_path)) == []
