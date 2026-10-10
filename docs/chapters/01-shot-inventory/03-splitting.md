---
icon: lucide/book-open
tags:
  - Dictionary
---

# Lesson 1.3 — Splitting a Name into Parts

The folder gives you names, not facts. To group files or find gaps, you need the parts back: which shot, which sequence, which frame. Python strings come with **methods** that take text apart.

## split and rsplit

`split(".")` cuts at every dot and returns a list of the pieces:

```python
name = "SH010_comp_v002.1001.exr"
print(name.split("."))
stem = name.split(".")[0]
print(stem.split("_"))
```

```text
['SH010_comp_v002', '1001', 'exr']
['SH010', 'comp', 'v002']
```

`[0]` picks the first piece of the list, so `stem` is the text before the first dot.

Some names contain extra dots, such as `SH010_comp_v002.denoise.1001.exr`. The frame and extension are always the *last* two parts, so `rsplit(".", 2)` splits from the right, at most twice:

```python
print("SH010_comp_v002.denoise.1001.exr".rsplit(".", 2))
```

```text
['SH010_comp_v002.denoise', '1001', 'exr']
```

!!! question "Think"

    This code uses `split(".")` instead. Which value comes out wrong, and which line would you change?

    ```python
    parts = "SH010_comp_v002.denoise.1001.exr".split(".")
    info = {"sequence": parts[0], "frame": parts[1], "extension": "." + parts[2]}
    ```

??? success "Answer"

    `split(".")` gives four pieces, so `info` holds `"SH010_comp_v002"`, `"denoise"`, and `".1001"`: every value is wrong. Change the first line to `rsplit(".", 2)`. The sequence can contain dots, but the frame and extension are always the last two pieces, so you count from the end.

!!! question "Think"

    What does `"notes.txt".rsplit(".", 2)` return, and what happens if your code then asks for the third piece?

??? success "Answer"

    `['notes', 'txt']`: only two pieces. Asking for index `2` raises an `IndexError`. Before taking a name apart, check that it has the shape you expect: `len(parts)` tells you how many pieces you got.

## Naming the parts with a dictionary

A list numbers its pieces; a **dictionary** names them. Each entry pairs a key with a value, and you read a value by its key:

```python
plate = {"shot": "SH010", "fps": 24}
print(plate["shot"], plate["fps"])
```

```text
SH010 24
```

Lesson 1.8 builds dictionaries step by step; for now, writing one out as above is enough.

## Checking the end

`name.lower().endswith((".exr", ".dpx"))` asks whether a name is an image, in any letter case. `lower()` returns a lowercase *copy*; the original name doesn't change. The inner parentheses group the endings: `endswith` returns `True` if the name ends with any of them.

## Assignment

Open `src/chapter_01/lesson_03.py`.

**1. `is_image(name)`** returns `True` for `.exr` and `.dpx` files in any letter case.

> Expected: `is_image("a.0001.DPX")` → `True`

**2. `split_frame_name(name)`** returns a dictionary for an image named `SEQUENCE.FRAME.ext`, all values as text.

- Keep the extension as written, with its dot.
- Return `None` when the name isn't an image.
- Return `None` when the name doesn't have at least two dots.

> Expected: `split_frame_name("SH010_comp_v002.1001.exr")` → `{"sequence": "SH010_comp_v002", "frame": "1001", "extension": ".exr"}`

Check your work:

```console
academy test 1 3
```
