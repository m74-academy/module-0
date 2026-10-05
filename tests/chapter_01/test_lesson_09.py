from __future__ import annotations

from pathlib import Path

from chapter_01.lesson_09 import image_files, list_files

SAMPLE = Path(__file__).resolve().parents[2] / "docs/chapters/01-shot-inventory/sample/dump"


def _make(folder: Path, *names: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for name in names:
        (folder / name).write_text("fixture\n", encoding="utf-8")
    return folder


def test_sample_folder():
    """The lesson's folder has eleven files, nine of them images."""
    assert len(list_files(SAMPLE)) == 11
    assert len(image_files(SAMPLE)) == 9


def test_direct_files_only(tmp_path: Path):
    """Subfolders and their contents are skipped; names are sorted."""
    _make(tmp_path, "b.1002.exr", "a.1001.EXR", "notes.txt")
    _make(tmp_path / "old", "a.1000.exr")
    assert list_files(tmp_path) == ["a.1001.EXR", "b.1002.exr", "notes.txt"]
    assert image_files(tmp_path) == ["a.1001.EXR", "b.1002.exr"]


def test_empty_folder(tmp_path: Path):
    """Nothing in, nothing out."""
    assert list_files(tmp_path) == [] and image_files(tmp_path) == []
