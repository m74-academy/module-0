---
icon: lucide/book-open
---

# Lesson 1.8 — Dictionaries: Grouping by Sequence

The folder is one long list of names from several sequences. To check each sequence on its own, you first sort the names into groups: all the `SH010_comp_v002` frames together, all the `SH020_comp_v001` frames together. A **dictionary** maps each group's name to its contents.

## Building groups

```python
names = ["SH010_comp_v002.1002.exr", "SH020_comp_v001.0998.exr", "SH010_comp_v002.1001.exr"]
groups = {}
for name in names:
    sequence, frame, extension = name.rsplit(".", 2)
    if sequence not in groups:  # first frame of this sequence: start its list
        groups[sequence] = []
    groups[sequence].append(int(frame))
print(groups)
for sequence in groups:
    groups[sequence].sort()
print(groups)
```

```text
{'SH010_comp_v002': [1002, 1001], 'SH020_comp_v001': [998]}
{'SH010_comp_v002': [1001, 1002], 'SH020_comp_v001': [998]}
```

The first time a sequence appears, it isn't a key of `groups` yet, so the loop gives it an empty list. (`in` on a dictionary checks keys, not values.) Then `.append` adds the frame to that sequence's list. After the loop, every sequence has its frames, in the order the names came.

To sort each list, loop over the dictionary: a `for` loop over a dictionary gives you its keys. `.sort()` changes each list in place, as in Lesson 1.7, so you don't assign its result.

!!! question "Think"

    What happens if you delete the two `if` lines? On which name does it fail, and why?

??? success "Answer"

    It fails with `KeyError` on the very first name. `groups[sequence]` reads a key that doesn't exist yet, because `groups` is still empty. The `if` creates each sequence's list once. Then the `append` runs for every frame, the first one included.

!!! question "Think"

    Why does the loop unpack three values from `rsplit(".", 2)` and ignore the extension?

??? success "Answer"

    `rsplit(".", 2)` always gives three pieces for a frame name: the sequence, the frame, and the extension. Unpacking them into three names makes the code say what each piece is. The extension isn't needed for grouping: `.exr` and `.dpx` frames of one sequence go in the same group.

## Assignment

Open `src/chapter_01/lesson_08.py`.

**`group_by_sequence(names)`** returns a dict from each sequence name to its frame numbers, sorted from smallest to largest.

- Only frame images count: names that your Lesson 1.3 `split_frame_name` accepts. Skip every other name, such as `notes.txt` and `SH020_preview.0001.mov`.
- Skip a name whose frame part isn't digits, such as `SH010_comp_v002.abcd.exr`. `"1001".isdigit()` is `True`; `"abcd".isdigit()` is `False`.
- List each frame of a sequence once, whatever its extension: `a.0007.exr` and `a.0007.dpx` give `[7]`.

You can reuse your Lesson 1.3 function: `from chapter_01.lesson_03 import split_frame_name`. It returns `None` for a name to skip; otherwise, read `parts["sequence"]` and `parts["frame"]`.

> Expected: `group_by_sequence(["SH010_comp_v002.1002.exr", "notes.txt", "SH010_comp_v002.1001.exr"])` → `{"SH010_comp_v002": [1001, 1002]}`

Check your work:

```console
academy test 1 8
```
