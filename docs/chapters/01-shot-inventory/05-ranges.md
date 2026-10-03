# Lesson 1.5 — Frame Ranges and List Comprehensions

A sequence that runs from 1001 to 1004 should have four frames. Before you can say one is missing, you need the full list of what *should* be there. Python's `range()` produces the numbers, and a **list comprehension** turns them into names.

## range() stops early

```python
print(list(range(1001, 1004)))
print(list(range(1001, 1004 + 1)))
```

```text
[1001, 1002, 1003]
[1001, 1002, 1003, 1004]
```

`range(start, stop)` stops *before* `stop`. Visual-effects ranges include the last frame, so add `1`.

> **Common trap:** Forget the `+ 1`, and a check of frames 1001–1100 never asks about frame 1100. If it's missing, nobody notices.

## A comprehension builds a list in one line

```python
names = [f"SH010_comp_v002.{frame:04d}.exr" for frame in range(1001, 1004)]
print(names)
```

```text
['SH010_comp_v002.1001.exr', 'SH010_comp_v002.1002.exr', 'SH010_comp_v002.1003.exr']
```

Read it as "a list of *this* for each *item* in *that*". Add `if` at the end to keep only some items: `[n for n in names if n.endswith(".exr")]`.

> **Think:** How would you write the `names` list with a `for` loop and `append`?

<details markdown="1"><summary>Answer</summary>

```python
names = []
for frame in range(1001, 1004):
    names.append(f"SH010_comp_v002.{frame:04d}.exr")
```

Both build the same list; the comprehension says it in one line.

</details>

## Assignment

Open `src/chapter_01/lesson_05.py`.

**1. `frame_list(first, last)`**: every frame from `first` to `last`, **including** `last`, as a list.

**2. `expected_names(sequence, first, last, extension)`**: every filename of a sequence, in frame order, frames padded to 4 digits.

```text
expected_names("SH010_comp_v002", 1001, 1002, ".exr")
→ ["SH010_comp_v002.1001.exr", "SH010_comp_v002.1002.exr"]
```

```console
academy test 1 5
```

Next: [Lesson 1.6 — Sets: Finding Missing Frames](06-sets.md).
