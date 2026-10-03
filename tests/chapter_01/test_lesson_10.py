from __future__ import annotations

import json
from pathlib import Path

import pytest

from chapter_01.lesson_10 import load_json, save_json

SHOT = {"sequence": "SH010_comp_v002", "frames": [
    1001, 1002, 1004], "complete": False, "note": None}


def test_file_format(tmp_path: Path):
    """Indented by 2, UTF-8, final newline."""
    path = tmp_path / "shots.json"
    save_json(SHOT, path)
    assert path.read_text(
        encoding="utf-8") == json.dumps(SHOT, indent=2) + "\n"


@pytest.mark.parametrize("data", [
    SHOT, [], {"artist": "José", "frames": {
        "first": 998}}, [1, "two", 3.5, True],
])
def test_round_trip(tmp_path: Path, data):
    """What save_json writes, load_json reads back."""
    path = tmp_path / "data.json"
    save_json(data, path)
    assert load_json(path) == data


def test_load_written_by_hand(tmp_path: Path):
    """Load JSON that another program wrote."""
    path = tmp_path / "m.json"
    path.write_text('{"shot": "SH010", "frames": [1001]}', encoding="utf-8")
    assert load_json(path) == {"shot": "SH010", "frames": [1001]}
