# Lesson 12 — Project: Shot Inventory

No new concept. You'll combine the whole chapter into the tool from Lesson 1: point it at a messy folder, and it sorts the files into sequences, finds the holes, lists what doesn't belong, prints a report, and saves the inventory as JSON. It reads the folder and never changes it.

## The brief

Open `src/chapter_01/lesson_12.py` and write three functions. You can import your own earlier work, such as `from chapter_01.lesson_07 import summarize`, or copy what you need.

**1. `inventory(folder)`** returns a dict for the regular files directly inside `folder`:

```text
inventory(Path("docs/chapters/01-shot-inventory/sample/dump"))
→ {
    "sequences": {
      "SH010_comp_v002": {"frames": "1001-1002, 1004", "missing": "1003", "count": 3},
      "SH010_roto_v001": {"frames": "1001-1002", "missing": "", "count": 2},
      "SH020_comp_v001": {"frames": "998-1001", "missing": "", "count": 4},
    },
    "other": ["SH020_preview.mov", "notes.txt"],
  }
```

- A **frame image** is a `.exr` or `.dpx` file, in any case, named `SEQUENCE.FRAME.ext` with digits as the frame. Group frame images by sequence; `"frames"` summarises them as in Lesson 7.
- `"missing"` summarises the frames missing *between* a sequence's first and last frame.
- `"count"` is the number of distinct frames in the sequence.
- Every other file goes in `"other"`, sorted. Subfolders are skipped.

**2. `report_lines(result)`** turns that dict into lines for a person, sequences in sorted order, then the other files:

```text
SH010_comp_v002: 1001-1002, 1004 (missing 1003)
SH010_roto_v001: 1001-1002 (complete)
SH020_comp_v001: 998-1001 (complete)
Other: SH020_preview.mov, notes.txt
```

`Other: none` when there are no other files.

**3. `main(argv)`** for the command `shot-inventory FOLDER OUTPUT`: print the report lines, save the inventory to `OUTPUT` as JSON (Lesson 10), and return `1` if any sequence has missing frames, otherwise `0`. Return `2`, with a message on stderr, when the arguments aren't exactly two, `FOLDER` isn't a folder, or `OUTPUT` would be written inside `FOLDER`: the tool never adds a file to the folder it checks. Add the guard, as in Lesson 11.

```console
uv run python -m chapter_01.lesson_12 docs/chapters/01-shot-inventory/sample/dump shots.json
academy test 1 12
```

The checks run your tool on the sample, on folders they build, with bad arguments, and as a real script, and check that the folder is unchanged afterwards.

## Plan before you code

> **Think:** Which lesson answers each step: listing the files, telling frames from other files, grouping by sequence, finding the holes, summarising frames, saving the result, and running from the terminal?

<details markdown="1"><summary>Answer</summary>

- Listing the folder: Lesson 9.
- Frames versus other files, and taking names apart: Lessons 3 and 4.
- Grouping by sequence: Lesson 8.
- The frames between first and last, and the missing ones: Lessons 5 and 6.
- Summaries such as `1001-1002, 1004`: Lesson 7.
- Saving the inventory: Lesson 10.
- `main`, exit codes, and the guard: Lesson 11.

</details>

Run it on the sample, then make a copy of the sample folder, change it, and predict the report before you run the tool again.

## What next

Open the `shots.json` you saved. The optional extension, [Ask Your Inventory](extension-ask.md), lets an AI model answer questions about it, such as "which shot is incomplete?", using only the facts your code produced.

That's Module 0. If you enjoyed it, the full course builds on exactly this loop.
