---
icon: lucide/book-open
---

# Lesson 1.9 — Listing a Folder with `os`

So far the names were typed into Python. Now they come from a real folder. Python's `os` module asks the computer what's inside it.

Run the examples from the `module-0` folder, the one with `pyproject.toml`. A folder path like `docs/...` is looked up from the folder you run Python in, not from where your code file is.

## What's in a folder

`os.listdir(folder)` gives the name of every entry directly inside a folder, files and folders alike, in no particular order. The `sample` folder holds one folder, `dump`, and `dump` holds the delivery:

```python
import os

print(os.listdir("docs/chapters/01-shot-inventory/sample"))
print(len(os.listdir("docs/chapters/01-shot-inventory/sample/dump")))
```

```text
['dump']
11
```

`os.listdir` also lists hidden files, whose names start with `.`. Some file browsers don't show them. For example, macOS Finder may add a `.DS_Store` file to a folder you open in it. Then you see `12` here, not `11`.

## Files, not folders

`os.listdir` gives only names, not paths. To ask about a name, first join it to its folder with `os.path.join`. It puts the right separator between them on every operating system. Then `os.path.isfile(path)` asks whether the path is a file, and `os.path.isdir(path)` asks whether it is a folder:

```python
import os

folder = "docs/chapters/01-shot-inventory/sample"
for name in os.listdir(folder):
    path = os.path.join(folder, name)
    print(name, os.path.isfile(path), os.path.isdir(path))
```

```text
dump False True
```

So a loop that keeps only files drops `dump`. Sort the names, so the result is the same every time:

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

Here is the same loop with one change. It gives no error, but it returns an empty list:

```python
for name in os.listdir(folder):
    if os.path.isfile(name):
        names.append(name)
```

!!! question "Think"

    Which line is wrong, and why is there no error?

??? success "Answer"

    `os.path.isfile(name)`. `name` is only a name, such as `notes.txt`. Python looks for it in the folder you run Python in. It isn't there, so `isfile` answers `False` for every name. That is a normal answer, not an error. `path` tells Python which folder to look in.

!!! question "Think"

    Why does `notes.txt` sort after every `SH…` name?

??? success "Answer"

    Text sorts by character code, and every uppercase letter comes before every lowercase one. `S` is uppercase, `n` is lowercase. The order is consistent, which is what a report needs, but it isn't alphabetical in the everyday sense.

## Assignment

Open `src/chapter_01/lesson_09.py`.

**1. `list_files(folder)`**: the sorted names of the files (not folders) directly inside `folder`. Skip subfolders and what's in them.

> Expected, for a folder with `b.1002.exr`, `a.1001.EXR`, `notes.txt`, and `old/a.1000.exr`: `list_files(folder)` → `["a.1001.EXR", "b.1002.exr", "notes.txt"]`

**2. `image_files(folder)`**: the same, but only `.exr` and `.dpx` files in any letter case. You can reuse `list_files` and your Lesson 1.3 `is_image`: `from chapter_01.lesson_03 import is_image`.

> Expected, for the same folder: `image_files(folder)` → `["a.1001.EXR", "b.1002.exr"]`

Check your work:

```console
academy test 1 9
```
