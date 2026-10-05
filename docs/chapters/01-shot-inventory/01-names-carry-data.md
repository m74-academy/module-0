---
icon: lucide/book-text
tags:
  - Frame
  - Sequence
  - Shot
  - Task
  - Version
---

# Lesson 1.1 — Names Carry Data

Imagine a production in a hurry. Artists on several shots have been saving their renders into one shared folder. Someone has to answer simple questions, and nobody can: which shots are in here? Is anything missing? Which file is the latest? The files aren't the problem. The problem is that nobody has read what their **names** already say.

## A filename is a record

A **shot** is one continuous piece of a film, such as `SH010`. Each shot is a series of still images, **frames**, numbered in order. Different people work on the same shot: a compositor (`comp`) combines the elements, a roto artist (`roto`) draws the shapes others need. Each time they deliver, the **version** goes up: `v001`, `v002`. A studio names every frame file by one rule:

```text
SH010_comp_v002.1001.exr
│     │    │    │    └── extension: the file type
│     │    │    └─────── frame number, padded to four digits
│     │    └──────────── version
│     └───────────────── task
└─────────────────────── shot
```

Everything before the frame number identifies a **sequence**: all the frames of one shot, task, and version. So the name alone says which shot, which job, which delivery, and which picture in the series.

## The folder

The sample folder, `docs/chapters/01-shot-inventory/sample/dump/` in your project, contains:

```text
SH010_comp_v002.1001.exr    SH020_comp_v001.0998.exr
SH010_comp_v002.1002.exr    SH020_comp_v001.0999.exr
SH010_comp_v002.1004.exr    SH020_comp_v001.1000.exr
SH010_roto_v001.1001.exr    SH020_comp_v001.1001.exr
SH010_roto_v001.1002.exr    SH020_preview.mov
notes.txt
```

!!! question "Think"

    Which part of `SH010_comp_v002.1001.exr` changes from one frame to the next, and which parts stay the same?

??? success "Answer"

    Only the frame number, `1001`, changes. The shot, task, version, and extension stay the same for every frame of the sequence. So two files belong to the same sequence when everything except the frame number matches.

!!! question "Think"

    Look at the sample folder. Which sequences does it hold, which frames are missing inside a sequence, and which files are not frames?

??? success "Answer"

    Three sequences: `SH010_comp_v002` (frames 1001, 1002, 1004), `SH010_roto_v001` (1001, 1002), and `SH020_comp_v001` (998 to 1001). Frame 1003 of `SH010_comp_v002` is missing: the numbers jump from 1002 to 1004. `SH020_preview.mov` and `notes.txt` aren't frames; keep them, but report them separately. `notes.txt` is worth reading: it explains the hole.

You did by eye what the rest of this chapter teaches Python to do, for any folder, in a fraction of a second.
