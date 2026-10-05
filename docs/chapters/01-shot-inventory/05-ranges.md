---
icon: lucide/book-open
---

# Lesson 1.5 — Frame Ranges and List Comprehensions

A sequence that runs from 1001 to 1004 should have four frames. Before you can say one is missing, you need the full list of what *should* be there. Python's `range()` produces the numbers, and a **list comprehension** turns them into names.

## `range()` stops early

```python
print(list(range(1001, 1004)))
print(list(range(1001, 1004 + 1)))
```

```text
[1001, 1002, 1003]
[1001, 1002, 1003, 1004]
```

`range(start, stop)` stops *before* `stop`. Visual-effects ranges include the last frame, so add `1`.

!!! warning "Common trap"

    Forget the `+ 1`, and a check of frames 1001–1100 never asks about frame 1100. If it's missing, nobody notices.

## A comprehension builds a list in one line

```python
names = [f"SH010_comp_v002.{frame:04d}.exr" for frame in range(1001, 1004)]
print(names)
```

```text
['SH010_comp_v002.1001.exr', 'SH010_comp_v002.1002.exr', 'SH010_comp_v002.1003.exr']
```

Read it as "a list of *this* for each *item* in *that*". Add `if` at the end to keep only some items: `[n for n in names if n.endswith(".exr")]`.

!!! question "Think"

    How would you write the `names` list with a `for` loop and `append`?

??? success "Answer"

    ```python
    names = []
    for frame in range(1001, 1004):
        names.append(f"SH010_comp_v002.{frame:04d}.exr")
    ```

    Both build the same list; the comprehension says it in one line.

!!! tip "Comprehension or loop?"

    Use a comprehension when you build one list from another: each item becomes one new item, perhaps with an `if` to skip some. Use a `for` loop when each step does more than that: several statements, a `print`, a `try`, updating two things at once, or stopping early with `break`. If the comprehension no longer reads easily on one line, write the loop. Speed is not the reason to choose: the difference is small.

## Assignment

Open `src/chapter_01/lesson_05.py`.

**1. `frame_list(first, last)`**: every frame from `first` to `last`, **including** `last`, as a list.

> Expected: `frame_list(1001, 1004)` → `[1001, 1002, 1003, 1004]`

**2. `expected_names(sequence, first, last, extension)`**: every filename of a sequence, in frame order, frames padded to 4 digits.

> Expected: `expected_names("SH010_comp_v002", 1001, 1002, ".exr")` → `["SH010_comp_v002.1001.exr", "SH010_comp_v002.1002.exr"]`

Check your work:

```console
academy test 1 5
```
