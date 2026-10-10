from __future__ import annotations

import builtins
import json
from pathlib import Path

import pytest

from chapter_01 import lesson_10
from chapter_01.lesson_10 import load_json, save_json

SHOT = {"sequence": "SH010_comp_v002", "frames": [1001, 1002, 1004], "complete": False, "note": None}


@pytest.mark.parametrize(("data", "text"), [
    ({"shot": "SH010"}, '{\n  "shot": "SH010"\n}'),
    (SHOT, json.dumps(SHOT, indent=2)),
])
def test_file_format(tmp_path: Path, data, text):
    """Indented by 2, replacing what the file held before; a final newline is fine."""
    path = tmp_path / "shots.json"
    save_json([1], str(path))
    save_json(data, str(path))
    assert path.read_text(encoding="utf-8").removesuffix("\n") == text


@pytest.mark.parametrize("data", [
    SHOT, [], {"artist": "José", "frames": {"first": 998}}, [1, "two", 3.5, True],
])
def test_round_trip(tmp_path: Path, data):
    """What save_json writes, load_json reads back."""
    path = tmp_path / "data.json"
    save_json(data, str(path))
    assert load_json(str(path)) == data


@pytest.fixture
def ascii_computer(monkeypatch):
    """A computer whose default text encoding is not UTF-8, as on many Windows setups."""
    def open_ascii_default(file, mode="r", buffering=-1, encoding=None, *args, **kwargs):
        if "b" not in mode and encoding is None:
            encoding = "ascii"
        return builtins.open(file, mode, buffering, encoding, *args, **kwargs)

    monkeypatch.setattr(lesson_10, "open", open_ascii_default, raising=False)


@pytest.mark.parametrize("data", [
    {"shot": "SH010"}, {"shot": "SH010", "frames": [1001]}, {"artist": "José"},
])
def test_load_written_by_hand(tmp_path: Path, ascii_computer, data):
    """Load UTF-8 JSON that another program wrote."""
    path = tmp_path / "m.json"
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    assert load_json(str(path)) == data
