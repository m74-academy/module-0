---
icon: lucide/book-open
---

# Lesson 1.9 — Listing a Folder with `os`

So far the names were typed into Python. Now they come from a real folder. Python's `os` module asks the computer what's inside it.

Run the examples from the `module-0` folder, the one with `pyproject.toml`.

## What's in a folder

`os.listdir(folder)` gives the name of every entry directly inside a folder, files and folders alike, in no particular order:

```python
import os

folder = "docs/chapters/01-shot-inventory/sample/dump"
print(len(os.listdir(folder)))
```

```text
11
```

## Files, not folders

`os.listdir` gives only names. To ask whether a name is a file, join it to its folder with `os.path.join`, which puts the right separator between them on every operating system, then ask `os.path.isfile`. `os.path.isdir` asks the same for a folder. Sort the names so the result is the same every time:

```python
import os

folder = "docs/chapters/01-shot-inventory/sample/dump"
names = []
for name in os.listdir(folder):
    path = os.path.join(folder, name)
    if os.path.isfile(path):
        names.append(name)
names.sort()
print(len(names), names[0], names[-1])
```

```text
11 SH010_comp_v002.1001.exr notes.txt
```

`os.listdir` doesn't look inside subfolders. A tool that only checks the delivery folder itself should stay that way: a subfolder of old renders isn't part of the delivery.

!!! question "Think"

    Why does `notes.txt` sort after every `SH…` name?

??? success "Answer"

    Text sorts by character code, and every uppercase letter comes before every lowercase one. `S` is uppercase, `n` is lowercase. The order is consistent, which is what a report needs, but it isn't alphabetical in the everyday sense.

## Assignment

Open `src/chapter_01/lesson_09.py`.

**1. `list_files(folder)`**: the sorted names of the regular files directly inside `folder`. Skip subfolders and what's in them.

> Expected, for a folder with `b.1002.exr`, `a.1001.EXR`, `notes.txt`, and `old/a.1000.exr`: `list_files(folder)` → `["a.1001.EXR", "b.1002.exr", "notes.txt"]`

**2. `image_files(folder)`**: the same, but only `.exr` and `.dpx` files in any letter case.

> Expected, for the same folder: `image_files(folder)` → `["a.1001.EXR", "b.1002.exr"]`

Check your work:

```console
academy test 1 9
```
