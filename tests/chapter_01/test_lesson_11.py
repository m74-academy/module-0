from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from chapter_01.lesson_11 import main

SAMPLE = Path(__file__).resolve().parents[2] / "docs/chapters/01-shot-inventory/sample/dump"


def test_sample(capsys):
    """Nine images in the lesson folder."""
    assert main([str(SAMPLE)]) == 0
    assert capsys.readouterr().out == "9 image files\n"


@pytest.mark.parametrize("argv", [[], ["a", "b"]])
def test_usage(capsys, argv: list[str]):
    """Exactly one argument, or a usage message and 2."""
    assert main(argv) == 2
    captured = capsys.readouterr()
    assert captured.out == "usage: count-frames FOLDER\n"


def test_counts_images_only(tmp_path: Path, capsys):
    """Both extensions in any case, directly inside the folder."""
    for name in ["a.1001.EXR", "b.1002.dpx", "notes.txt", "old/c.1003.exr"]:
        (tmp_path / name).parent.mkdir(exist_ok=True)
        (tmp_path / name).write_text("", encoding="utf-8")
    assert main([str(tmp_path)]) == 0
    assert capsys.readouterr().out == "2 image files\n"


@pytest.mark.parametrize("name", ["gone", "notes.txt"])
def test_not_a_folder(tmp_path: Path, capsys, name: str):
    """A missing path or a file is an error."""
    path = tmp_path / name
    if name == "notes.txt":
        path.write_text("", encoding="utf-8")
    assert main([str(path)]) == 2
    captured = capsys.readouterr()
    assert captured.out == f"error: {path} is not a folder\n"


def test_run_as_a_script():
    """Running the file exits with main's result."""
    result = subprocess.run([sys.executable, "-m", "chapter_01.lesson_11", str(SAMPLE)],
                            capture_output=True, text=True, check=False)
    assert (result.returncode, result.stdout) == (0, "9 image files\n"), result.stderr
    missing = subprocess.run([sys.executable, "-m", "chapter_01.lesson_11"],
                             capture_output=True, text=True, check=False)
    assert missing.returncode == 2
