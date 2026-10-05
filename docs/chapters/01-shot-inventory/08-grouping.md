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
```

```text
{'SH010_comp_v002': [1002, 1001], 'SH020_comp_v001': [998]}
```

The first time a sequence appears, it isn't in `groups` yet, so the loop gives it an empty list. Then `.append` adds the frame to that sequence's list. After the loop, every sequence has its frames.

!!! question "Think"

    Why does the loop unpack three values from `rsplit(".", 2)` and ignore the extension?

??? success "Answer"

    `rsplit(".", 2)` always gives three pieces for a frame name: the sequence, the frame, and the extension. Unpacking them into three names makes the code say what each piece is. The extension isn't needed for grouping here, but a real tool might keep `.exr` and `.dpx` frames of one sequence apart.

## Assignment

Open `src/chapter_01/lesson_08.py`.

**`group_by_sequence(names)`** returns a dict from sequence name to its frame numbers, **sorted**. Only image names of the form `SEQUENCE.FRAME.ext` count; skip everything else, such as `notes.txt` and `SH020_preview.mov`. You can reuse your Lesson 1.3 function: `from chapter_01.lesson_03 import split_frame_name`.

> Expected: `group_by_sequence(["SH010_comp_v002.1002.exr", "notes.txt", "SH010_comp_v002.1001.exr"])` → `{"SH010_comp_v002": [1001, 1002]}`

Check your work:

```console
academy test 1 8
```
