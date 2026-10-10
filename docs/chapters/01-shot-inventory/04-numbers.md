---
icon: lucide/book-open
---

# Lesson 1.4 — Numbers from Text

Splitting a name gives you text: `"1001"`, `"v002"`. But the questions are about numbers: which frame comes next? Which version is newer? Text can't answer them, so you **convert**.

## `int()` and `str()`

```python
frame = "1001"
print(frame + "1")
print(int(frame) + 1)
```

```text
10011
1002
```

With text, `+` joins. `int()` turns the text into a number, and then `+` adds. `"1001" + 1` raises a `TypeError`: Python won't mix text and a number, so convert first. `int("0007")` is `7`: the zeros disappear, and you add them back with a format spec when you build a name. `str()` goes the other way: `str(7)` gives `"7"`.

A shot such as `"SH010"` starts with letters, so `int("SH010")` raises a `ValueError`. Cut the letters off first with a **slice**: `shot[2:]` means "from the third character to the end".

```python
shot = "SH010"
number = int(shot[2:])
print(number, f"SH{number + 10:03d}")
```

```text
10 SH020
```

!!! question "Think"

    As text, is `"999"` smaller than `"1000"`? Why?

??? success "Answer"

    No. Text is compared one character at a time, and `"9"` comes after `"1"`, so `"999" > "1000"` is `True`. As numbers, `999 > 1000` is `False`. That's why frames are compared as numbers.

!!! question "Think"

    A tool takes the frame as "the four characters before `.exr`" (`name[-8:-4]`). It gives `1001` for `SH010_comp_v002.1001.exr`. What does it give for `SH010_comp_v002.10001.exr`, and why?

??? success "Answer"

    `1`. The four characters are `"0001"`. Padding sets a minimum width (Lesson 1.2), so frame `10001` keeps all five digits. Take the part between the last two dots, as in Lesson 1.3, and the frame can have any width. The same rule makes `f"v{1000:03d}"` give `v1000`.

## Assignment

Open `src/chapter_01/lesson_04.py`.

**1. `frame_number(name)`** returns the frame of a filename as a number.

- The frame is the part between the last two dots, with any number of digits.
- Some names have extra dots, as in Lesson 1.3.

> Expected: `frame_number("SH010_comp_v002.0007.exr")` → `7`

**2. `version_number(version)`**: the version as a number.

> Expected: `version_number("v002")` → `2`

**3. `next_version(version)`**: the next version, with at least three digits.

> Expected: `next_version("v999")` → `"v1000"`

Check your work:

```console
academy test 1 4
```
