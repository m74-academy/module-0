# Lesson 1 — Names Carry Data

**You will produce:** a short written answer about a messy folder. **Where to write:** open `answers/chapter_01/lesson_01.md` in VS Code, write under its headings, and save. This lesson has no code and no automated grade.

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

The [sample folder](sample/dump/) contains:

```text
SH010_comp_v002.1001.exr    SH020_comp_v001.0998.exr
SH010_comp_v002.1002.exr    SH020_comp_v001.0999.exr
SH010_comp_v002.1004.exr    SH020_comp_v001.1000.exr
SH010_roto_v001.1001.exr    SH020_comp_v001.1001.exr
SH010_roto_v001.1002.exr    SH020_preview.mov
notes.txt
```

> **Think:** How many sequences are in this folder, and does any of them have a hole?

<details markdown="1"><summary>Answer</summary>

Three: `SH010_comp_v002` (frames 1001, 1002, 1004), `SH010_roto_v001` (1001, 1002), and `SH020_comp_v001` (998 to 1001). The comp of SH010 is missing frame 1003. `SH020_preview.mov` follows a different pattern and isn't a frame; `notes.txt` is a note, and it explains the hole.

</details>

## Assignment — Read the folder

Open `answers/chapter_01/lesson_01.md` and answer under each heading:

1. List each sequence and the frames it has.
2. Which frames are missing inside a sequence, and how did you decide?
3. Which files are not frames, and what would you do with each?
4. Name one thing the filenames *cannot* tell you, however carefully you read them.

<details markdown="1"><summary>Check your answer (open after writing it)</summary>

The three sequences are above. Frame 1003 of `SH010_comp_v002` is missing: the numbers jump from 1002 to 1004. `SH020_preview.mov` and `notes.txt` aren't frames; keep them, but report them separately. Names can't tell you whether an image is correct, or whether frames *outside* the range you see were expected, such as 997 for SH020.

</details>

You did by eye what the rest of this chapter teaches Python to do, for any folder, in a fraction of a second. Save your file. `academy test 1 1` only reminds you where to write.

Next: [Lesson 2 — Building Names with f-strings](02-f-strings.md).
