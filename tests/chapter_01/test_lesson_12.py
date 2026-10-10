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
        "SH010_comp_v002": {"frames": "1001-1004", "missing": [1003], "count": 3},
        "SH010_roto_v001": {"frames": "1001-1002", "missing": [], "count": 2},
        "SH020_comp_v001": {"frames": "998-1001", "missing": [], "count": 4},
    },
    "other": ["SH020_preview.mov", "notes.txt"],
}
REPORT = [
    "SH010_comp_v002: 1001-1004 (missing 1003)",
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


def _sample(tmp_path: Path) -> Path:
    """A copy of the lesson's folder without hidden files, such as the .DS_Store macOS Finder may add."""
    return shutil.copytree(SAMPLE, tmp_path / "dump", ignore=shutil.ignore_patterns(".*"))


def test_sample_inventory(tmp_path: Path):
    """The lesson's folder, exactly."""
    assert inventory(str(_sample(tmp_path))) == EXPECTED


def test_sample_report():
    """The lesson's report, exactly."""
    assert report_lines(EXPECTED) == REPORT


def test_rules(tmp_path: Path):
    """Case, odd names, a non-digit frame, duplicates by extension, one frame, a wide gap, and subfolders."""
    folder = _make(tmp_path / "d", "A_x_v001.0005.EXR", "A_x_v001.0007.dpx", "A_x_v001.0007.exr",
                   "A_x_v001.abcd.exr", "thumbnail.exr", "readme", "B_y_v001.0010.exr",
                   "C_z_v001.1001.exr", "C_z_v001.1040.exr")
    _make(folder / "old", "A_x_v001.0006.exr")
    assert inventory(str(folder)) == {
        "sequences": {
            "A_x_v001": {"frames": "5-7", "missing": [6], "count": 2},
            "B_y_v001": {"frames": "10", "missing": [], "count": 1},
            "C_z_v001": {"frames": "1001-1040", "missing": list(range(1002, 1040)), "count": 2},
        },
        "other": ["A_x_v001.abcd.exr", "readme", "thumbnail.exr"],
    }


def test_report_several_missing():
    """Several missing frames are joined by a comma."""
    result = {"sequences": {"S_c_v001": {"frames": "1-5", "missing": [2, 4], "count": 3}}, "other": []}
    assert report_lines(result) == ["S_c_v001: 1-5 (missing 2, 4)", "Other: none"]


def test_report_sorts_sequences():
    """Sequences are reported in sorted order, whatever order the dict holds them in."""
    result = {"sequences": {"S_b_v001": {"frames": "1-2", "missing": [], "count": 2},
                            "S_a_v001": {"frames": "1-3", "missing": [2], "count": 2}}, "other": []}
    assert report_lines(result) == ["S_a_v001: 1-3 (missing 2)", "S_b_v001: 1-2 (complete)", "Other: none"]


def test_empty_folder(tmp_path: Path):
    """Nothing in the folder."""
    result = inventory(str(tmp_path))
    assert result == {"sequences": {}, "other": []}
    assert report_lines(result) == ["Other: none"]


def test_main_writes_json_and_leaves_folder_alone(tmp_path: Path, capsys):
    """Print the report, save the inventory, return 1 for missing frames, change nothing."""
    folder = _sample(tmp_path)
    before = _digests(folder)
    output = tmp_path / "shots.json"
    assert main([str(folder), str(output)]) == 1
    assert capsys.readouterr().out == "\n".join(REPORT) + "\n"
    assert json.loads(output.read_text(encoding="utf-8")) == EXPECTED
    assert _digests(folder) == before


def test_main_complete(tmp_path: Path, capsys):
    """No holes: print the report, save the inventory, exit 0."""
    folder = _make(tmp_path / "d", "S_c_v001.0001.exr", "S_c_v001.0002.exr")
    output = tmp_path / "out.json"
    assert main([str(folder), str(output)]) == 0
    assert capsys.readouterr().out == "S_c_v001: 1-2 (complete)\nOther: none\n"
    assert json.loads(output.read_text(encoding="utf-8")) == {
        "sequences": {"S_c_v001": {"frames": "1-2", "missing": [], "count": 2}},
        "other": [],
    }


@pytest.mark.parametrize("case", ["no arguments", "one argument", "three arguments", "missing folder", "file as folder"])
def test_main_bad_input(tmp_path: Path, capsys, case: str):
    """Bad input is 2, with a message, and nothing written into the folder."""
    folder = _make(tmp_path / "d", "S_c_v001.0001.exr")
    gone = str(tmp_path / "gone")
    image = str(folder / "S_c_v001.0001.exr")
    output = str(folder / "o.json")
    usage = "usage: shot-inventory FOLDER OUTPUT"
    argv = {
        "no arguments": [],
        "one argument": [str(folder)],
        "three arguments": [str(folder), output, "extra"],
        "missing folder": [gone, output],
        "file as folder": [image, output],
    }[case]
    message = {
        "no arguments": usage,
        "one argument": usage,
        "three arguments": usage,
        "missing folder": f"error: {gone} is not a folder",
        "file as folder": f"error: {image} is not a folder",
    }[case]
    assert main(argv) == 2
    assert capsys.readouterr().out == message + "\n"
    assert sorted(p.name for p in folder.iterdir()) == ["S_c_v001.0001.exr"]


def test_run_as_a_script(tmp_path: Path):
    """Running the file exits with main's result."""
    result = subprocess.run([sys.executable, "-m", "chapter_01.lesson_12", str(_sample(tmp_path)),
                             str(tmp_path / "s.json")],
                            capture_output=True, text=True, check=False)
    assert result.returncode == 1, result.stderr
    assert result.stdout.splitlines() == REPORT
