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

A set keeps one copy of each value. `x in frames` is `True` or `False`, and a set answers it very quickly. `sorted()` returns a new list of the values in order. A set has no order of its own:

```python
print({9, 8, 7})
```

```text
{8, 9, 7}
```

Small numbers can look sorted by chance; never rely on it. Sort a set when you show it or return it.

`{}` on its own is an empty dictionary; an empty set is `set()`.

`set()` turns a list into a set:

```python
print(sorted(set(["blue", "red", "blue"])))
```

```text
['blue', 'red']
```

## Comparing two sets

```python
expected = {1001, 1002, 1003, 1004}
found = {1001, 1002, 1004, 1005}
print(sorted(expected - found))
print(sorted(found - expected))
print(sorted(expected & found))
```

```text
[1003]
[1005]
[1001, 1002, 1004]
```

`expected - found` is what should be there and isn't: **missing**. `found - expected` arrived without being expected: **extra**. `expected & found` is what's in both.

!!! question "Think"

    The folder has four files and four were expected. Can a frame still be missing?

??? success "Answer"

    Yes, exactly as above: frame 1003 is missing and 1005 is extra, and the counts are equal. Comparing counts hides both problems; comparing sets finds them.

!!! question "Think"

    `found` is `[1001, 1001, 1002]`, and frames 1001 to 1003 were expected. The counts match. What does `set(found)` show that `len(found)` hides?

??? success "Answer"

    `set(found)` is `{1001, 1002}`. The duplicate made the count look complete, and `set(expected) - set(found)` shows that 1003 is missing.

## Assignment

Open `src/chapter_01/lesson_06.py`.

**1. `missing_frames(expected, found)`**: the sorted list of frames, each once, in `expected` that aren't in `found`. Both arguments are lists and may contain duplicates.

> Expected: `missing_frames([1001, 1002, 1003, 1004], [1001, 1002, 1004, 1005])` → `[1003]`

**2. `extra_frames(expected, found)`**: the sorted list of frames in `found` that aren't in `expected`.

> Expected: `extra_frames([], [9, 7, 7])` → `[7, 9]`

Check your work:

```console
academy test 1 6
```
