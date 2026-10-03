# Lesson 8 — Dictionaries: Grouping by Sequence

The folder is one long list of names from several sequences. To check each sequence on its own, you first sort the names into groups: all the `SH010_comp_v002` frames together, all the `SH020_comp_v001` frames together. A **dictionary** maps each group's name to its contents.

## Building groups

```python
names = ["SH010_comp_v002.1002.exr", "SH020_comp_v001.0998.exr", "SH010_comp_v002.1001.exr"]
groups = {}
for name in names:
    sequence, frame, extension = name.rsplit(".", 2)
    groups.setdefault(sequence, []).append(int(frame))
print(groups)
```

```text
{'SH010_comp_v002': [1002, 1001], 'SH020_comp_v001': [998]}
```

`groups.setdefault(key, [])` returns the list for `key`, creating an empty one the first time. Then `.append` adds the frame. After the loop, every sequence has its frames.

> **Think:** Why does the loop unpack three values from `rsplit(".", 2)` and ignore the extension?

<details markdown="1"><summary>Answer</summary>

`rsplit(".", 2)` always gives three pieces for a frame name: the sequence, the frame, and the extension. Unpacking them into three names makes the code say what each piece is. The extension isn't needed for grouping here, but a real tool might keep `.exr` and `.dpx` frames of one sequence apart.

</details>

## Assignment

Open `src/chapter_01/lesson_08.py`.

**`group_by_sequence(names)`** returns a dict from sequence name to its frame numbers, **sorted**. Only image names of the form `SEQUENCE.FRAME.ext` count; skip everything else, such as `notes.txt` and `SH020_preview.mov`. You can reuse your Lesson 3 function: `from chapter_01.lesson_03 import split_frame_name`.

```text
group_by_sequence(["SH010_comp_v002.1002.exr", "notes.txt", "SH010_comp_v002.1001.exr"])
→ {"SH010_comp_v002": [1001, 1002]}
```

```console
academy test 1 8
```

Next: [Lesson 9 — Listing a Folder with pathlib](09-folders.md).
