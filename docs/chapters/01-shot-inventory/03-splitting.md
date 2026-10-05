---
icon: lucide/book-open
---

# Lesson 1.3 — Splitting a Name into Parts

The folder gives you names, not facts. To group files or find gaps, you need the parts back: which shot, which sequence, which frame. Python strings come with **methods** that take text apart.

## split and rsplit

`split(".")` cuts at every dot and returns a list of the pieces:

```python
name = "SH010_comp_v002.1001.exr"
print(name.split("."))
print(name.split(".")[0].split("_"))
```

```text
['SH010_comp_v002', '1001', 'exr']
['SH010', 'comp', 'v002']
```

Some names contain extra dots, such as `SH010_comp_v002.denoise.1001.exr`. The frame and extension are always the *last* two parts, so `rsplit(".", 2)` splits from the right, at most twice:

```python
print("SH010_comp_v002.denoise.1001.exr".rsplit(".", 2))
```

```text
['SH010_comp_v002.denoise', '1001', 'exr']
```

## Checking the end

`name.lower().endswith((".exr", ".dpx"))` asks whether a name is an image, in any letter case. `lower()` returns a lowercase *copy*; the original name doesn't change.

!!! question "Think"

    What does `"notes.txt".rsplit(".", 2)` return, and what happens if your code then asks for the third piece?

??? success "Answer"

    `['notes', 'txt']`: only two pieces. Asking for index `2` raises an `IndexError`. Before taking a name apart, check that it has the shape you expect.

## Assignment

Open `src/chapter_01/lesson_03.py`.

**1. `is_image(name)`** returns `True` for `.exr` and `.dpx` files in any letter case.

> Expected: `is_image("a.0001.DPX")` → `True`

**2. `split_frame_name(name)`** returns a dict for an image named `SEQUENCE.FRAME.ext`, all values as text. Return `None` when the name isn't an image or doesn't have at least two dots.

> Expected: `split_frame_name("SH010_comp_v002.1001.exr")` → `{"sequence": "SH010_comp_v002", "frame": "1001", "extension": ".exr"}`

Check your work:

```console
academy test 1 3
```
