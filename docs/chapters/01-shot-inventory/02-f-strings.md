---
icon: lucide/book-open
tags:
  - f-string
  - Frame padding
---

# Lesson 1.2 — Building Names with f-strings

Before Python can check a folder, it needs to know which names to look for. Those names are built from a few facts: shot, task, version, frame. If one character is wrong, such as a missing zero or a missing dot, a frame that is there looks "missing".

## Values inside text

An **f-string** has an `f` before the quote; anything inside `{}` is replaced by its value:

```python
shot, task = "SH010", "comp"
print(f"{shot}_{task}")
```

```text
SH010_comp
```

## Padding numbers

Frame `7` is saved as `0007`, so every frame up to `9999` has the same four-digit width. A **format spec** after a colon asks for that. Read `{frame:04d}` from left to right:

```text
{frame:04d}
       │││
       ││└── d: a whole number
       │└─── 4: at least 4 characters wide
       └──── 0: fill the empty places with 0
```

```python
version, frame = 2, 7
print(f"SH010_comp_v{version:03d}.{frame:04d}.exr")
```

```text
SH010_comp_v002.0007.exr
```

`d` works only on numbers. Text such as `"7"` must become a number first; [Lesson 1.4](04-numbers.md) shows how.

!!! question "Think"

    A tool looks for `SH010_comp_v002.0007.exr` in a folder that holds `SH010_comp_v002.7.exr`. What does it report, and why?

??? success "Answer"

    It reports frame 7 as missing. To a computer they are two different names. A tool looking for `0007` doesn't find `7`, even though the image is there.

The width is a minimum: `f"{12345:04d}"` gives `12345`. Python never cuts a number.

!!! question "Think"

    Why is it safer for Python to give `12345` than to cut it to four digits?

??? success "Answer"

    Cutting `12345` to four digits gives `2345`. That is another real frame, so two different frames would get the same name, and the name would point to the wrong image.

The `0` matters too. Leave it out, and Python fills the empty places with spaces:

```python
frame = 7
print(f"SH010_comp_v002.{frame:4d}.exr")
```

```text
SH010_comp_v002.   7.exr
```

!!! question "Think"

    A tool builds the names it looks for with `{frame:4d}`. Which frames that are in the sample folder of [Lesson 1.1](01-names-carry-data.md#the-folder) does it wrongly report missing?

??? success "Answer"

    Only `0998` and `0999` of `SH020_comp_v001`. The tool looks for `SH020_comp_v001. 998.exr`, with a space, and doesn't find it. (It reports 1003 too, but 1003 really is missing.) Frames from 1000 up already fill all four places, so `4d` and `04d` give the same name for them. That is why the bug can hide: most frames still look right.

## Assignment

Open `src/chapter_01/lesson_02.py`.

**1. `sequence_name(shot, task, version)`** returns the part every frame of an image sequence shares, with the version padded to 3 digits.

> Expected: `sequence_name("SH010", "comp", 2)` → `"SH010_comp_v002"`

**2. `frame_filename(shot, task, version, frame, extension)`** returns the filename for one frame.

- `version` and `frame` are numbers. Pad the version to 3 digits and the frame to 4.
- `extension` includes its dot, such as `".exr"`.
- Everything before the dot and frame number is the `sequence_name` of item 1, so you can reuse it.

> Expected: `frame_filename("SH010", "comp", 2, 7, ".exr")` → `"SH010_comp_v002.0007.exr"`

Check your work:

```console
academy test 1 2
```

## Further reading

- [Formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) (Python tutorial): f-strings from the start, with more examples of a width after the colon.
- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language) (Python reference): every option after the colon, such as the `0` fill, the width, and `d`.
- [Python f-string cheat sheet](https://fstring.help/cheat/) (fstring.help): short examples of each format spec with its result, to look one up quickly.
