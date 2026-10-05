---
icon: lucide/book-open
---

# Lesson 1.7 — Sorting Frames as Numbers

A report should list frames in order, and it should be short. Nobody wants to read 200 frame numbers; a coordinator wants `1001-1004`. This lesson sorts names by the number inside them, and writes a range of frames as text.

## Sorting with `key=`

`sorted()` compares text one character at a time, which puts `"10"` before `"9"`. `key=` tells it what to compare instead: a function that turns each item into the value to sort by.

```python
names = ["a.10.exr", "a.9.exr", "a.100.exr"]
print(sorted(names))
print(sorted(names, key=lambda name: int(name.rsplit(".", 2)[1])))
```

```text
['a.10.exr', 'a.100.exr', 'a.9.exr']
['a.9.exr', 'a.10.exr', 'a.100.exr']
```

`lambda name: ...` is a small function written in place. The names come back unchanged, in the order of their frame numbers.

## A new list, not a changed one

`sorted()` returns a new list and leaves the original alone. A list's own `.sort()` method changes that list in place and returns `None`.

!!! question "Think"

    `sort_by_frame` gets a list from the code that calls it. Why should it use `sorted()` and not `names.sort()`?

??? success "Answer"

    `names.sort()` would reorder the caller's list behind its back, and the function would return `None` unless you return `names` yourself. `sorted()` gives back a new list, and the caller's list stays as it was.

## Assignment

Open `src/chapter_01/lesson_07.py`.

**1. `sort_by_frame(names)`**: a new list of frame filenames, sorted by frame number.

> Expected: `sort_by_frame(["a.10.exr", "a.9.exr"])` → `["a.9.exr", "a.10.exr"]`

**2. `format_run(start, end)`**: a range of frames as text. A single frame, where `start` equals `end`, stays a number; a longer range becomes `start-end`.

> Expected: `format_run(1001, 1004)` → `"1001-1004"`

Check your work:

```console
academy test 1 7
```
