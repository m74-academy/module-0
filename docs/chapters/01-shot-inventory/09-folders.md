# Lesson 1.9 — Listing a Folder with pathlib

So far the names were typed into Python. Now they come from a real folder. Python's `pathlib` module turns a path into an object that knows its parts and can ask the computer what's inside.

Run the examples from the `module-0` folder, the one with `pyproject.toml`.

## Paths and their parts

```python
from pathlib import Path

path = Path("docs/chapters/01-shot-inventory/sample/dump/SH010_comp_v002.1001.exr")
print(path.name, path.suffix, path.parent.name)
```

```text
SH010_comp_v002.1001.exr .exr dump
```

`/` joins paths, whatever the operating system writes between folders: `Path("sample") / "dump"`.

## What's in a folder

`folder.iterdir()` gives every entry directly inside a folder, files and folders alike, in no particular order. `path.is_file()` tells a file from a folder. Sort the names so the result is the same every time:

```python
from pathlib import Path

folder = Path("docs/chapters/01-shot-inventory/sample/dump")
names = sorted(path.name for path in folder.iterdir() if path.is_file())
print(len(names), names[0], names[-1])
```

```text
11 SH010_comp_v002.1001.exr notes.txt
```

`iterdir()` doesn't look inside subfolders. A tool that only checks the delivery folder itself should stay that way: a subfolder of old renders isn't part of the delivery.

> **Think:** Why does `notes.txt` sort after every `SH…` name?

<details markdown="1"><summary>Answer</summary>

Text sorts by character code, and every uppercase letter comes before every lowercase one. `S` is uppercase, `n` is lowercase. The order is consistent, which is what a report needs, but it isn't alphabetical in the everyday sense.

</details>

## Assignment

Open `src/chapter_01/lesson_09.py`.

**1. `list_files(folder)`**: the sorted names of the regular files directly inside `folder`. Skip subfolders and what's in them.

**2. `image_files(folder)`**: the same, but only `.exr` and `.dpx` files in any letter case.

```console
academy test 1 9
```

The checks build small folders of their own, with a subfolder, an uppercase `.EXR`, and an empty folder.

Next: [Lesson 1.10 — JSON as Memory](10-json.md).
