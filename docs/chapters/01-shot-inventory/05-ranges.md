---
icon: lucide/book-open
---

# Lesson 1.5 — Frame Ranges and List Comprehensions

A sequence that runs from 1001 to 1004 should have four frames. Before you can say one is missing, you need the full list of what *should* be there. Python's `range()` produces the numbers, and a **list comprehension** turns them into names.

## `range()` stops early

```python
print(list(range(1001, 1004)))
print(list(range(1001, 1004 + 1)))
print(range(1001, 1004 + 1))
```

```text
[1001, 1002, 1003]
[1001, 1002, 1003, 1004]
range(1001, 1005)
```

`range(start, stop)` stops *before* `stop`. Visual-effects ranges include the last frame, so pass `last + 1` as `stop`.

`range()` is not a list: it hands out the numbers one at a time. `list()` collects them, which is why the examples wrap it.

!!! question "Think"

    `range(1001, 1004)` has three numbers. Without listing them, how many numbers does `range(first, stop)` give? How many frames does `range(first, last + 1)` give?

??? success "Answer"

    `range(first, stop)` gives `stop - first` numbers. So `range(first, last + 1)` gives `last - first + 1` frames: 1001 to 1004 is 4 frames.

!!! warning "Common trap"

    Forget the `+ 1`, and the last frame disappears:

    ```python
    def frame_list(first, last):
        return list(range(first, last))

    print(frame_list(1001, 1004))   # [1001, 1002, 1003]
    ```

    A check of frames 1001–1100 built this way never asks about frame 1100. If it's missing, nobody notices.

## A comprehension builds a list in one line

```python
names = [f"SH010_comp_v002.{frame:04d}.exr" for frame in range(1001, 1003 + 1)]
print(names)
```

```text
['SH010_comp_v002.1001.exr', 'SH010_comp_v002.1002.exr', 'SH010_comp_v002.1003.exr']
```

Read it as "a list of *this* for each *item* in *that*". Add `if` at the end to keep only some items:

```python
files = ["SH010_comp_v002.1001.exr", "notes.txt", "SH010_comp_v002.1002.exr"]
print([n for n in files if n.endswith(".exr")])
```

```text
['SH010_comp_v002.1001.exr', 'SH010_comp_v002.1002.exr']
```

!!! question "Think"

    How would you write the `names` list with a `for` loop and `append`?

??? success "Answer"

    ```python
    names = []
    for frame in range(1001, 1003 + 1):
        names.append(f"SH010_comp_v002.{frame:04d}.exr")
    ```

    Both build the same list; the comprehension says it in one line. The f-string is written first, but it runs once for each `frame`, like the loop body. The `for` part is the loop header.

!!! tip "Comprehension or loop?"

    Use a comprehension when you build one list from another: each item becomes one new item, perhaps with an `if` to skip some. Use a `for` loop when each step does more than that: several statements, a `print`, updating two things at once, or stopping early with `break`. If the comprehension no longer reads easily on one line, write the loop. Speed is not the reason to choose: the difference is small.

## Assignment

Open `src/chapter_01/lesson_05.py`.

**1. `frame_list(first, last)`**: every frame from `first` to `last`, as a list.

- The list includes `last`.
- If `last` is before `first`, the list is empty.

> Expected: `frame_list(1001, 1004)` → `[1001, 1002, 1003, 1004]`

**2. `expected_names(sequence, first, last, extension)`**: every filename of a sequence, in frame order, frames padded to 4 digits.

> Expected: `expected_names("SH010_comp_v002", 1001, 1002, ".exr")` → `["SH010_comp_v002.1001.exr", "SH010_comp_v002.1002.exr"]`

Check your work:

```console
academy test 1 5
```
