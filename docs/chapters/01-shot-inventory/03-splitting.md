---
icon: lucide/book-open
tags:
  - Dictionary
---

# Lesson 1.3 — Splitting a Name into Parts

The folder gives you names, not facts. To group files or find gaps, you need the parts back: which shot, which image sequence, which frame. Python strings come with **methods** that split text into parts.

## `split` and `rsplit`

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

`[0]` picks the first piece of the list, so `stem` is the text before the first dot. The [Python tutorial](https://docs.python.org/3/tutorial/introduction.html#lists) covers list indexing if you need a refresher.

Some names contain extra dots, such as `SH010_comp_v002.denoise.1001.exr`. The frame and extension are always the *last* two parts, so `rsplit(".", 2)` splits from the right, at most twice, and gives fewer pieces when the name has fewer dots:

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

    `split(".")` gives four pieces, so `info` holds `"SH010_comp_v002"`, `"denoise"`, and `".1001"`: every value is wrong. The `sequence` value lost `.denoise`, the frame is the word `denoise`, and the extension is the frame number. Change the first line to `rsplit(".", 2)`. The image sequence's name can contain dots, but the frame and extension are always the last two pieces, so you count from the end.

!!! question "Think"

    What does `"notes.txt".rsplit(".", 2)` return, and what happens if your code then asks for the third piece?

??? success "Answer"

    `['notes', 'txt']`: only two pieces. Asking for index `2` raises an `IndexError`, because the list has no third piece. After splitting, check that you got the number of pieces you expect: `len(parts)` tells you how many there are. The [Python tutorial](https://docs.python.org/3/tutorial/introduction.html#text) shows `len` and `IndexError` on strings; lists work the same way.

## Naming the parts with a dictionary

A list numbers its pieces; a **dictionary** names them. Each entry pairs a key with a value, and you read a value by its key:

```python
info = {"shot": "SH010", "fps": 24}
print(info["shot"], info["fps"])
```

```text
SH010 24
```

Here `"fps"` is frames per second: how many frames make one second of film. [Lesson 1.8](08-grouping.md) builds dictionaries step by step; for now, writing one out as above is enough.

## Checking the end

`name.lower().endswith((".exr", ".dpx"))` asks whether a name is an image, in any letter case. `lower()` returns a lowercase *copy*; the original name doesn't change. The inner parentheses group the endings: `endswith` returns `True` if the name ends with any of them.

```python
print("a.0001.DPX".lower().endswith((".exr", ".dpx")))
print("exr_notes.txt".lower().endswith((".exr", ".dpx")))
print("a.0001.DPX".endswith((".exr", ".dpx")))
```

```text
True
False
False
```

The second name contains `exr`, but it ends with `.txt`. The third line skips `lower()`, so `.DPX` doesn't match `.dpx`.

## Assignment

Open `src/chapter_01/lesson_03.py`.

**1. `is_image(name)`** returns `True` for `.exr` and `.dpx` files in any letter case.

> Expected: `is_image("a.0001.DPX")` → `True`

**2. `split_frame_name(name)`** returns a dictionary for an image named `SEQUENCE.FRAME.ext`, all values as text.

- Keys: `sequence`, `frame`, `extension`.
- Keep the extension as written, with its dot.
- Return `None` when the name isn't an image.
- Return `None` when the name doesn't have at least two dots, as in `a.exr`: an image, but with no frame number.

> Expected: `split_frame_name("SH010_comp_v002.1001.exr")` → `{"sequence": "SH010_comp_v002", "frame": "1001", "extension": ".exr"}`

Check your work:

```console
academy test 1 3
```

## Further reading

- [`str.rsplit`](https://docs.python.org/3/library/stdtypes.html#str.rsplit) (Python reference): how `maxsplit` limits the cuts to the rightmost ones.
- [`str.endswith`](https://docs.python.org/3/library/stdtypes.html#str.endswith) (Python reference): the tuple of endings, and the optional start and end positions.
- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) (Python tutorial): keys, values, and what you can use as a key.
- [Learn Python in Y Minutes](https://learnxinyminutes.com/python/) (Learn X in Y Minutes): one page of short examples for strings, lists, `len`, `IndexError`, and dictionaries.
