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

With text, `+` joins. `int()` turns the text into a number, and then `+` adds. `int("0007")` is `7`: the zeros disappear, and you add them back with a format spec when you build a name.

A version such as `"v002"` starts with a letter, so `int("v002")` fails. Cut the letter off first with a **slice**: `version[1:]` means "from the second character to the end".

```python
version = "v002"
number = int(version[1:])
print(number, f"v{number + 1:03d}")
```

```text
2 v003
```

!!! question "Think"

    As text, is `"999"` smaller than `"1000"`?

??? success "Answer"

    No. Text is compared one character at a time, and `"9"` comes after `"1"`, so `"999" > "1000"` is `True`. As numbers, `999 > 1000` is `False`. That's why frames are compared as numbers.

## Assignment

Open `src/chapter_01/lesson_04.py`.

**1. `frame_number(name)`** returns the frame of a filename as a number.

> Expected: `frame_number("SH010_comp_v002.0007.exr")` → `7`

**2. `version_number(version)`**: the version as a number.

> Expected: `version_number("v002")` → `2`

**3. `next_version(version)`**: the next version, with at least three digits.

> Expected: `next_version("v999")` → `"v1000"`

Check your work:

```console
academy test 1 4
```
