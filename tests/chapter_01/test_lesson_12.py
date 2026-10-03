from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from chapter_01.lesson_12 import inventory, main, report_lines

SAMPLE = Path(__file__).resolve().parents[2] / "docs/chapters/01-shot-inventory/sample/dump"

EXPECTED = {
    "sequences": {
        "SH010_comp_v002": {"frames": "1001-1002, 1004", "missing": "1003", "count": 3},
        "SH010_roto_v001": {"frames": "1001-1002", "missing": "", "count": 2},
        "SH020_comp_v001": {"frames": "998-1001", "missing": "", "count": 4},
    },
    "other": ["SH020_preview.mov", "notes.txt"],
}
REPORT = [
    "SH010_comp_v002: 1001-1002, 1004 (missing 1003)",
    "SH010_roto_v001: 1001-1002 (complete)",
    "SH020_comp_v001: 998-1001 (complete)",
    "Other: SH020_preview.mov, notes.txt",
]


def _digests(folder: Path) -> dict[str, str]:
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.iterdir() if p.is_file()}


def _make(folder: Path, *names: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for name in names:
        (folder / name).write_text("fixture\n", encoding="utf-8")
    return folder


def test_sample_inventory():
    """The lesson's folder, exactly."""
    assert inventory(SAMPLE) == EXPECTED


def test_sample_report():
    """The lesson's report, exactly."""
    assert report_lines(EXPECTED) == REPORT


def test_rules(tmp_path: Path):
    """Case, odd names, duplicates by extension, and subfolders."""
    folder = _make(tmp_path / "d", "A_x_v001.0005.EXR", "A_x_v001.0007.dpx", "A_x_v001.0007.exr",
                   "thumbnail.exr", "A_x_v001.v2.exr", "readme")
    _make(folder / "old", "A_x_v001.0006.exr")
    assert inventory(folder) == {
        "sequences": {"A_x_v001": {"frames": "5, 7", "missing": "6", "count": 2}},
        "other": ["A_x_v001.v2.exr", "readme", "thumbnail.exr"],
    }


def test_empty_folder(tmp_path: Path):
    """Nothing in the folder."""
    result = inventory(tmp_path)
    assert result == {"sequences": {}, "other": []}
    assert report_lines(result) == ["Other: none"]


def test_main_writes_json_and_leaves_folder_alone(tmp_path: Path, capsys):
    """Print the report, save the inventory, return 1 for missing frames, change nothing."""
    folder = shutil.copytree(SAMPLE, tmp_path / "dump")
    before = _digests(folder)
    output = tmp_path / "shots.json"
    assert main([str(folder), str(output)]) == 1
    assert capsys.readouterr().out == "\n".join(REPORT) + "\n"
    assert json.loads(output.read_text(encoding="utf-8")) == EXPECTED
    assert _digests(folder) == before


def test_main_complete(tmp_path: Path, capsys):
    """No holes, exit 0."""
    folder = _make(tmp_path / "d", "S_c_v001.0001.exr", "S_c_v001.0002.exr")
    assert main([str(folder), str(tmp_path / "out.json")]) == 0


@pytest.mark.parametrize("case", ["no arguments", "missing folder", "output inside folder"])
def test_main_bad_input(tmp_path: Path, capsys, case: str):
    """Bad input is 2, with a message on stderr, and nothing written into the folder."""
    folder = _make(tmp_path / "d", "S_c_v001.0001.exr")
    argv = {"no arguments": [], "missing folder": [str(tmp_path / "gone"), str(tmp_path / "o.json")],
            "output inside folder": [str(folder), str(folder / "shots.json")]}[case]
    assert main(argv) == 2
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err
    assert sorted(p.name for p in folder.iterdir()) == ["S_c_v001.0001.exr"]


def test_run_as_a_script(tmp_path: Path):
    """Running the file exits with main's result."""
    result = subprocess.run([sys.executable, "-m", "chapter_01.lesson_12", str(SAMPLE), str(tmp_path / "s.json")],
                            capture_output=True, text=True, check=False)
    assert result.returncode == 1, result.stderr
    assert result.stdout.splitlines() == REPORT
