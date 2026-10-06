# Changelog

What changed in each release of Module 0. Get a new release with the steps in
[Updates](README.md#updates). The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.5] — 2026-10-06

### Fixed

- The old install and set-up page addresses open a short page that links to the M74 Academy guides; 0.2.4 removed them, so links from earlier releases ended in a 404.

## [0.2.4] — 2026-10-06

### Changed

- *Getting help* sends questions to this repository's Discussions and mistakes or setup failures to its issues.
- The install and set-up pages moved to the public M74 Academy guides; the old pages link to them.

## [0.2.3] — 2026-10-06

### Added

- A *Getting help* section in the README points to this repository's issues.

## [0.2.2] — 2026-10-05

### Changed

- Lesson 1.10 and the capstone no longer show a terminal recording; their worked example and sample report say the same.

## [0.2.1] — 2026-10-05

### Changed

- *Set up the module* covers the `origin remote is missing` and `origin is not a GitHub fork` health checks, and its last line points to your module's README.
- Lesson 1.2 no longer lists what its checks try; the check named "lesson example" is the frame-7 case the lesson shows.
- Lesson 1.11 asks you to create a `work` folder for experiments; `.gitignore` keeps `work/` and the capstone's `shots.json` out of your fork.

### Added

- Terminal recordings show JSON surviving between Python processes, script arguments and exit statuses, the finished Shot Inventory, and the difference between Python's prompt and the shell. The setup guide also shows the existing synthetic check–edit–check demo.

## [0.2.0] — 2026-10-05

### Changed

- The setup pages are the single setup guide for every M74 Academy module. The pages are renamed *Install the software* and *Set up the module*. *Set up the module* adds the setup recording, the fork and workspace illustrations, and an **Open it in VS Code** step; *Install the software* adds the sign-in illustration. The *Get course updates* page is gone: the start page and README say when to run `academy update`.
- *Set up the module* shows the course, your fork, and your clone as a diagram, with where each lives, its remote name, and how `git push` and `academy update` connect them. Course pages can now include Mermaid diagrams.
- The sidebar lists the start page and each chapter's overview as their own entries.
- *Set up the module* explains how to run Python in the module: interactively, a file, a lesson as a script, and your own lesson function.
- Lesson 1.5 adds a tip on when to write a comprehension and when a `for` loop.
- Every assignment function shows one example under its description, as `> Expected: call → result`, in the same form on every lesson.
- Each assignment introduces its `academy test` command with "Check your work:".
- Lesson 1.7 drops `summarize`: you write `sort_by_frame` and `format_run(start, end)`, and its Think question asks why `sorted()` beats `.sort()` there.
- The capstone reports each sequence as a range plus its missing frames: `SH010_comp_v002: 1001-1004 (missing 1003)`. In the JSON, `"frames"` is the range and `"missing"` a list of frames.
- *Set up the module* adds **When a check fails**: read the `E` lines, and add a `print` to see a value; its output shows under **Captured stdout call**. Lesson 1.2 links to it.
- Lesson 1.8 builds groups with `if sequence not in groups:` instead of `setdefault`, so each step is visible.
- Lesson 1.9 lists a folder with `os.listdir` and `os.path.isfile` instead of `pathlib`, and is renamed *Listing a Folder with os*. Starters and examples through the capstone take folder and file paths as text.
- Code in headings, titles, and prose is in backticks, such as `os`, `uv`, and `pytest`.
- Lesson 1.10 shows how to read a JSON file back, and `save_json` no longer needs a final newline.
- Lesson 1.11 teaches the script in three short steps, each with its output: `script, *args = sys.argv`, `main(args)` returning a status, and the guard. Messages print normally; stderr is no longer part of Module 0. Running the finished lesson with `uv run python -m` comes after the checks, with a line on `-m`.
- The optional *Ask Your Inventory* AI extension is removed: it needed a paid API key in a public fork. The capstone's "What next" points to Module 5 instead.
- The capstone shows how `", ".join` joins the missing frames and other files, the one step no lesson taught. Lesson 1.11 suggests reusing `image_files`.
- The capstone is simpler to read and asks only what the lessons taught: `main` is a table of situations, `1` is explained, the plan names the functions to reuse, and the checks come before running it. A frame image no longer needs digits as its frame, and the tool no longer refuses an `OUTPUT` inside `FOLDER`.
- `.vscode/extensions.json` recommends the Python extension when you open the folder in VS Code.
- `.gitattributes` lets `academy update` keep your lesson code when a course release changes the same lesson, and list it so you can recheck that lesson. Run `uv tool upgrade m74-academy-cli` **before** this update, so it runs with `academy` 0.4.2 or later.
- The README's **After Module 0** section presents Module 0 as a readiness check: if it felt easy, Module 1 is next; if Python itself was new, start with a free introduction such as CS50P.

## [0.1.1] — 2026-10-03

### Added

- Setup pages in `docs/setup/`: set up your computer, fork and clone, and get course updates. `academy health` and `academy update` link to them.
- A `LICENSE` file that restates the use terms.

### Changed

- The README says eleven lessons, explains how to run a worked example, and describes the full course without an enrollment claim.
- Lesson 1.1's Think question no longer gives away the assignment; its answer moved to the self-check.
- Sample-folder links name the folder in your project, so they work in the course preview.
- Lesson headings and references are numbered by chapter, as in the menu and `academy test`: `Lesson 1.2`, `Lesson 1.12`.
- Text uses US spelling throughout.

## [0.1.0] — 2026-10-03

### Added

- Chapter 1 — Shot Inventory: eleven lessons, the Shot Inventory project, and an optional AI extension.
