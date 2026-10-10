---
icon: lucide/book-open
tags:
  - Coordinator
---

# Lesson 1.7 — Sorting Frames as Numbers

A report should list frames in order, and it should be short. Nobody wants to read 200 frame numbers. A **coordinator**, the production person who tracks which frames have arrived, wants `1001-1004`. This lesson sorts names by the number inside them, and writes a range of frames as text.

## Sorting with `key=`

For strings, `sorted()` compares one character at a time. `"1"` comes before `"9"`, so `"10"` comes before `"9"`. `key=` tells `sorted()` what to compare instead: a function that turns each item into the value to sort by.

```python
def frame_number(name):
    return int(name.rsplit(".", 2)[1])

names = ["a.10.exr", "a.9.exr", "a.100.exr"]
print(sorted(names))
print(sorted(names, key=frame_number))
```

```text
['a.10.exr', 'a.100.exr', 'a.9.exr']
['a.9.exr', 'a.10.exr', 'a.100.exr']
```

`sorted()` calls `frame_number` on each name and compares the numbers it gets back. The names come back unchanged, in the order of their frame numbers. `rsplit(".", 2)` is the split from [Lesson 1.3](03-splitting.md), so a name with an extra dot, such as `SH010_comp_v002.denoise.1001.exr`, still gives the frame.

A key used once doesn't need a name. `lambda` writes the same function in place:

```python
names = ["a.10.exr", "a.9.exr", "a.100.exr"]
print(sorted(names, key=lambda name: int(name.rsplit(".", 2)[1])))
```

```text
['a.9.exr', 'a.10.exr', 'a.100.exr']
```

`lambda name:` takes the argument `name`. The expression after the colon is the value it returns; there is no `return`.

!!! question "Think"

    [Lesson 1.2](02-f-strings.md) pads every frame to at least four digits. Would `sorted(names)` without `key=` already put padded names in frame order? When would it still go wrong?

??? success "Answer"

    Yes, when every frame has the same width. `"0998"` comes before `"1001"` one character at a time, just as 998 comes before 1001. It goes wrong when the widths differ: frame `10000` sorts before `9999`, and an unpadded `a.9.exr` sorts after a padded `a.0010.exr`. A `key=` that returns `int` is right in every case.

The key must give back a number, not just the frame part of the name:

```python
names = ["a.10.exr", "a.9.exr"]
print(sorted(names, key=lambda name: name.rsplit(".", 2)[1]))
```

```text
['a.10.exr', 'a.9.exr']
```

!!! question "Think"

    The key picks out the frame. Why is the order still wrong?

??? success "Answer"

    The key gives back the text `"10"` and `"9"`, and text still compares one character at a time. `int()` turns them into numbers, and numbers compare by value.

## A new list, not a changed one

`sorted()` returns a new list and leaves the original alone. A list's own `.sort()` method changes that list in place and returns `None`.

!!! question "Think"

    A caller has `shots = ["a.10.exr", "a.9.exr"]` and calls a version of `sort_by_frame` that uses `names.sort()`. What does `shots` hold afterwards, and what does the call return?

??? success "Answer"

    `shots` is now `["a.9.exr", "a.10.exr"]`: the function reordered the caller's list without the caller asking. The call returns `None`, unless the function returns `names` itself. With `sorted()`, the caller gets a new sorted list and `shots` stays as it was.

## Assignment

Open `src/chapter_01/lesson_07.py`.

**1. `sort_by_frame(names)`**: a new list of frame filenames, sorted by frame number.

> Expected: `sort_by_frame(["a.10.exr", "a.9.exr"])` → `["a.9.exr", "a.10.exr"]`

**2. `format_run(start, end)`**: a range of frames as text. A single frame, where `start` equals `end`, becomes that frame number as text; a longer range becomes `start-end`. The range gives only the first and last frame. It doesn't promise that every frame in between is there; [Lesson 1.6](06-sets.md) finds the missing ones.

> Expected: `format_run(1001, 1004)` → `"1001-1004"`, and `format_run(1004, 1004)` → `"1004"`

Check your work:

```console
academy test 1 7
```
