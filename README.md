# M74 Academy — Module 0

A free, self-paced introduction to [M74 Academy](https://github.com/m74-academy): eleven short lessons that teach the Python behind a small visual-effects tool, and a project where you build it. You read a lesson, write a function, and run a check that tells you whether it works. That loop is how M74 Academy lessons work; Module 0 lets you try it on your own computer, with no instructor and no deadline.

**What you build:** *Shot Inventory*, a script that looks at a messy folder of image frames from several shots, groups the files into sequences, finds the frames that are missing, prints a report, and saves it as JSON. It reads the folder and never changes it.

**What you need:** a computer with macOS, Windows, or Linux; a free [GitHub account](https://github.com/signup); and some Python basics: variables, `if`, `for`, lists, and functions. No visual-effects experience.

## Start here

1. **Install the tools**, once: [`uv`](https://docs.astral.sh/uv/getting-started/installation/), [Git](https://git-scm.com/downloads), the [GitHub CLI](https://cli.github.com/) (then run `gh auth login`), and [VS Code](https://code.visualstudio.com/). Step by step, with every system's commands: [Install the software](https://github.com/m74-academy/community/blob/main/guides/install-uv-and-git.md). Then install the course command:

   ```console
   uv tool install git+https://github.com/m74-academy/academy-cli
   ```

2. **Get your own copy.** In a terminal, in the folder where you keep projects:

   ```console
   gh repo fork m74-academy/module-0 --clone
   ```

   This creates your fork on GitHub, downloads it into a `module-0` folder, and links it to the course for updates. Your fork is public, like this repository; see [Use terms](#use-terms).

3. **Open the folder** in VS Code (**File → Open Folder** → `module-0`), click **Install** when it offers the recommended extensions, then **Terminal → New Terminal**, and install the project:

   ```console
   uv sync --locked
   ```

4. **Check your setup:** `academy health`. The last line says `Setup looks good.`; a `FAIL` line comes with its fix.

5. **Open the course:** `academy docs` opens the lessons in your browser. Keep that terminal open.

6. **Check a lesson** in a second terminal:

   ```console
   academy test 1 2
   ```

   It fails until you solve the lesson; that is expected. Lesson 1.1 is reading only, with nothing to check. From Lesson 1.2 on, you write functions in `src/chapter_01/`.

`academy --help` lists every command.

## How a lesson works

Each lesson page explains one idea with an example you can run, then gives you a function to write in `src/chapter_01/lesson_NN.py`. The file has the function's name and a one-line description; you replace `pass` with your code. `academy test 1 NN` runs the lesson's checks and tells you which case failed and what your function returned. Fix, run again, and move on when it passes. To try an example or your own function, [run Python](https://github.com/m74-academy/community/blob/main/guides/fork-clone-setup.md#run-python) through `uv` in the `module-0` folder. The checks include cases the lesson doesn't show, so a passing function works, not just the example.

Step by step, with what a failing and a passing check look like: [Read, edit, and check a lesson](https://github.com/m74-academy/community/blob/main/guides/lesson-loop.md).

## How the course works

Module 0 is one chapter of lessons and a capstone, the project you build at the end. The full M74 Academy course uses the same lesson loop across five modules, adds optional Gold lessons and labs, and ends each module with a capstone you build in your own repository. [How the course works](https://github.com/m74-academy/community/blob/main/guides/how-the-course-works.md) explains it all.

## Course contents

[Chapter 1 — Shot Inventory](docs/chapters/01-shot-inventory/README.md): names that carry data, building and splitting names, numbers in text, ranges, sets, sorting, dictionaries, folders, JSON, a runnable script, and the project.

## Updates

When `academy health` says a newer release is available, run `academy update`. If the release changes a lesson you already solved, it keeps your code and lists that lesson: read the [changelog](CHANGELOG.md), then run the lesson's checks again.

## Getting help

Questions about a lesson or a setup step go in [Discussions](https://github.com/m74-academy/module-0/discussions); search first, and don't post solutions to the project. A mistake in a lesson, or a setup step that fails? [Open an issue](https://github.com/m74-academy/module-0/issues/new/choose) and pick the matching template. Include the command you ran, its full output, your operating system, and the lesson you were on.

## After Module 0

Module 0 is a sample of M74 Academy's course material, and a readiness check. M74 Academy is not a first Python course: it is for people who can already program and want to move into VFX pipeline TD work. If these lessons felt easy, you're ready for Module 1. If the Python itself was new, start with a free introduction such as [Harvard's CS50P](https://cs50.harvard.edu/python/), then come back.

## Use terms

Copyright © 2026 M74. All rights reserved for M74-authored material; [LICENSE](LICENSE) restates these terms. Third-party material retains its own rights and license terms.

You may use this material for your own learning, keep a copy, and keep a public GitHub fork of this repository for your exercises. You may not republish or redistribute it elsewhere, or use it to teach or sell a course. You own the work you write yourself and may show it in a portfolio, as long as it does not reproduce course material such as lesson text, starter code, or answer files.
