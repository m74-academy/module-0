---
icon: lucide/book-open
tags:
  - Set
---

# Lesson 1.6 — Sets: Finding Missing Frames

You have the frames that *should* be there and the frames that *are* there. The question "which are missing?" is a comparison of two groups, and Python has a type made for it: the **set**.

## A set holds each value once

```python
frames = {1001, 1002, 1002, 1004}
print(sorted(frames), 1003 in frames)
```

```text
[1001, 1002, 1004] False
```

A set ignores duplicates and answers `in` very quickly. It has no order, so sort it when you show it.

## Comparing two sets

```python
expected = {1001, 1002, 1003, 1004}
found = {1001, 1002, 1004, 1005}
print(sorted(expected - found))
print(sorted(found - expected))
```

```text
[1003]
[1005]
```

`expected - found` is what should be there and isn't: **missing**. `found - expected` arrived without being expected: **extra**. `&` gives what's in both.

!!! question "Think"

    The folder has four files and four were expected. Can a frame still be missing?

??? success "Answer"

    Yes, exactly as above: frame 1003 is missing and 1005 is extra, and the counts are equal. Comparing counts hides both problems; comparing sets finds them.

## Assignment

Open `src/chapter_01/lesson_06.py`.

**1. `missing_frames(expected, found)`**: the sorted list of frames in `expected` that aren't in `found`. Both arguments are lists and may contain duplicates.

> Expected: `missing_frames([1001, 1002, 1003, 1004], [1001, 1002, 1004, 1005])` → `[1003]`

**2. `extra_frames(expected, found)`**: the sorted list of frames in `found` that aren't in `expected`.

> Expected: `extra_frames([], [9, 7, 7])` → `[7, 9]`

Check your work:

```console
academy test 1 6
```
