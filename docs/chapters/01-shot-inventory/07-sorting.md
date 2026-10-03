# Lesson 1.7 — Sorting Frames as Numbers

A report should list frames in order, and it should be short. Nobody wants to read 200 frame numbers; a coordinator wants `1001-1002, 1004`, where the gap jumps out. This lesson sorts names by the number inside them, and summarizes a list of frames.

## Sorting with key=

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

## Collapsing runs

To summarize frames, walk through them in order and remember where the current run started. When the next frame isn't one more than the previous, the run has ended.

> **Think:** For `1001, 1002, 1004`, which two values do you need to remember while you walk through the list?

<details markdown="1"><summary>Answer</summary>

The **start** of the current run and the **previous** frame. At 1004, the previous frame is 1002, so the run `1001-1002` ends and a new one starts at 1004. After the loop, don't forget the last run.

</details>

## Assignment

Open `src/chapter_01/lesson_07.py`.

**1. `sort_by_frame(names)`**: a new list of frame filenames, sorted by frame number.

**2. `summarize(frames)`**: a summary such as `"1001-1002, 1004"`. Consecutive frames collapse into `first-last`, a frame on its own stays a single number, runs are joined by `", "`, input order and duplicates don't matter, and no frames give `""`.

```console
academy test 1 7
```

Next: [Lesson 1.8 — Dictionaries: Grouping by Sequence](08-grouping.md).
