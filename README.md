# M74 Academy — Module 0

A free, self-paced introduction to [M74 Academy](https://github.com/m74-academy): eleven short lessons that teach the Python behind a small visual-effects tool, and a project where you build it. You read a lesson, write a function, and run a check that tells you whether it works. That loop is how M74 Academy lessons work; Module 0 lets you try it on your own computer, with no instructor and no deadline.

**What you build:** *Shot Inventory*, a script that looks at a messy folder of image frames from several shots, groups the files into sequences, finds the frames that are missing, prints a report, and saves it as JSON. It reads the folder and never changes it.

**What you need:** a computer with macOS, Windows, or Linux; a free [GitHub account](https://github.com/signup); and some Python basics: variables, `if`, `for`, lists, and functions. No visual-effects experience.

## Start here

1. **Install the tools**, once: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Git](https://git-scm.com/downloads), the [GitHub CLI](https://cli.github.com/) (then run `gh auth login`), and [VS Code](https://code.visualstudio.com/). Step by step, with every system's commands: [Set up your computer](docs/setup/install-uv-and-git.md). Then install the course command:

   ```console
   uv tool install git+https://github.com/m74-academy/academy-cli
   ```

2. **Get your own copy.** In a terminal, in the folder where you keep projects:

   ```console
   gh repo fork m74-academy/module-0 --clone
   ```

   This creates your fork on GitHub, downloads it into a `module-0` folder, and links it to the course for updates. Your fork is public, like this repository; see [Use terms](#use-terms).

3. **Open the folder** in VS Code (**File → Open Folder** → `module-0`), then **Terminal → New Terminal**, and install the project:

   ```console
   uv sync --locked
   ```

4. **Check your setup:** `academy health`. The last line says `Setup looks good.`; a `FAIL` line comes with its fix.

5. **Open the course:** `academy docs` opens the lessons in your browser. Keep that terminal open.

6. **Check a lesson** in a second terminal:

   ```console
   academy test 1 2
   ```

   It fails until you solve the lesson; that is expected. Lesson 1.1 is written: `academy test 1 1` names the file to write in. From Lesson 1.2 on, you write functions in `src/chapter_01/`.

`academy --help` lists every command.

## How a lesson works

Each lesson page explains one idea with an example you can run, then gives you a function to write in `src/chapter_01/lesson_NN.py`. The file has the function's name and a one-line description; you replace `pass` with your code. `academy test 1 NN` runs the lesson's checks and tells you which case failed and what your function returned. Fix, run again, and move on when it passes. To run a worked example, paste it into `uv run python` in the `module-0` folder, or save it in a file and run `uv run python FILE`. The checks include cases the lesson doesn't show, so a passing function works, not just the example.

## Course contents

[Chapter 1 — Shot Inventory](docs/chapters/01-shot-inventory/README.md): names that carry data, building and splitting names, numbers in text, ranges, sets, sorting, dictionaries, folders, JSON, a runnable script, and the project. An optional extension asks questions about your inventory with an AI model you connect yourself.

## Updates

Commit your work, then update:

```console
git add -A
git commit -m "Save my work"
academy update
git push
```

The [changelog](CHANGELOG.md) lists what each release changes. If an update stops, [Get course updates](docs/setup/course-updates.md) explains what to do.

## After Module 0

Module 0 is a sample of M74 Academy's course material. The full course adds instructor-led labs, peer review, and project review.

## Use terms

Copyright © 2026 M74. All rights reserved for M74-authored material; [LICENSE](LICENSE) restates these terms. Third-party material retains its own rights and license terms.

You may use this material for your own learning, keep a copy, and keep a public GitHub fork of this repository for your exercises. You may not republish or redistribute it elsewhere, or use it to teach or sell a course. You own the work you write yourself and may show it in a portfolio, as long as it does not reproduce course material such as lesson text, starter code, or answer files.
