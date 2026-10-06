---
icon: lucide/book-open
tags:
  - f-string
  - Frame padding
---

# Lesson 1.2 — Building Names with f-strings

Before Python can check a folder, it needs to know which names to look for. Those names are built from a few facts: shot, task, version, frame. Get one character wrong, a missing zero or a missing dot, and a perfectly good frame looks "missing".

## Values inside text

An **f-string** has an `f` before the quote; anything inside `{}` is replaced by its value:

```python
shot, task = "SH010", "comp"
print(f"{shot}_{task}")
```

```text
SH010_comp
```

## Padding numbers

Frame `7` is saved as `0007`, so every name in a sequence has the same width. A **format spec** after a colon asks for that: `{frame:04d}` means a whole number (`d`), at least 4 characters wide, filled with `0`.

```python
version, frame = 2, 7
print(f"SH010_comp_v{version:03d}.{frame:04d}.exr")
```

```text
SH010_comp_v002.0007.exr
```

The width is a minimum: `f"{12345:04d}"` gives `12345`. Python never cuts a number.

!!! question "Think"

    Without padding, would `SH010_comp_v002.7.exr` and `SH010_comp_v002.0007.exr` be the same file?

??? success "Answer"

    No. To a computer they are two different names. A tool looking for `0007` doesn't find `7`, and reports the frame as missing even though the image is there.

## Assignment

Open `src/chapter_01/lesson_02.py`.

**1. `frame_filename(shot, task, version, frame, extension)`**: `version` and `frame` are numbers. Pad the version to 3 digits and the frame to 4.

> Expected: `frame_filename("SH010", "comp", 2, 7, ".exr")` → `"SH010_comp_v002.0007.exr"`

**2. `sequence_name(shot, task, version)`**: the part every frame of a sequence shares.

> Expected: `sequence_name("SH010", "comp", 2)` → `"SH010_comp_v002"`

Check your work:

```console
academy test 1 2
```
